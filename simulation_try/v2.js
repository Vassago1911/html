
function bind_to_clock_tick(ticked_action, millisecond_step) {
    function tick() {
      // ticked_action -> bool (weitermachen oder nicht?)
      var cancel_tick = ticked_action(millisecond_step);
      var now = Date.now();
      if ( !cancel_tick ) {
        //if not cancelled, schedule next tick
        setTimeout(tick, millisecond_step - (now%millisecond_step));
      }
    }
    tick()
}

class verletable_handler {
    constructor() {
        this.verletables = []
        this.left_limit = 128 + 32
        this.right_limit = 2048 - 128 - 32
        this.low_limit = 2048 - 128
    }

    add_verletable(v) {
        this.verletables = this.verletables.concat([v])
    }

    clean_boundary_collisions() {
        for (v in this.verletables) {
            v = this.verletables[v]
            if ( v.current_position[0] < this.left_limit + v.radius ) {
                v.current_position[0] = this.left_limit + v.radius
            }
            if ( v.current_position[0] > this.right_limit - v.radius ) {
                v.current_position[0] = this.right_limit - v.radius
            }
            if ( v.current_position[1] > this.low_limit - v.radius ) {
                v.current_position[1] = this.low_limit - v.radius
            }
        }
    }

    clean_ball_ball_collisions() {
        for ( let i = 0; i < this.verletables.length; i++ ) {
            v = this.verletables[i]
            for ( let j = i+1; j < this.verletables.length; j++ ) {
                var w = this.verletables[j]
                var dx = v.current_position[0] - w.current_position[0]
                var dy = v.current_position[1] - w.current_position[1]
                var rr = Math.sqrt(dx**2 + dy**2)
                if ( rr < v.radius + w.radius ) {
                    var overlap = ( v.radius + w.radius - rr ) / 2
                    var d = [dx,dy]
                    d = [ overlap*dx/rr, overlap*dy/rr ]
                    v.current_position[0] = v.current_position[0] + d[0]
                    v.current_position[1] = v.current_position[1] + d[1]
                    w.current_position[0] = w.current_position[0] - d[0]
                    w.current_position[1] = w.current_position[1] - d[1]
                }
            }
        }
    }

    move_verletables(dt) {
        var SUBSTEP_MAX = 8;
        for ( let substep = 0; substep < SUBSTEP_MAX; substep++ ) {
            for ( v in this.verletables ) {
                v = this.verletables[v]
                v.move(dt/SUBSTEP_MAX)
            }
            this.clean_ball_ball_collisions()
            this.clean_boundary_collisions()
        }
        for (v in this.verletables) {
            this.verletables[v].move_sprite()
        }
    }
}

class verletable {
    constructor(sprite) {
        this.sprite = sprite

        var cx = 1*this.sprite.getAttribute("cx")
        var cy = 1*this.sprite.getAttribute("cy")
        var r = 1*this.sprite.getAttribute("r")

        this.radius = r
        this.current_position = [cx,cy]
        this.last_position = [cx,cy-1]
        this.acceleration = [0,.1] //tugging on the velocity
    }

    move(dt) {
        var velocity = [ this.current_position[0] - this.last_position[0], this.current_position[1] - this.last_position[1] ]
        var a = this.acceleration
        this.last_position = this.current_position
        this.current_position = [ this.current_position[0] + velocity[0] + a[0]*(dt/1000)**2,
                                  this.current_position[1] + velocity[1] + a[1]*(dt/1000)**2 ]
    }

    move_sprite() {
        this.sprite.setAttribute("cx",this.current_position[0])
        this.sprite.setAttribute("cy",this.current_position[1])
    }
}

function gen_ball(x,y) {
    var l0 = get_all_layers()[0]
    c = document.createElementNS("http://www.w3.org/2000/svg",'circle')
    c.setAttribute("r",64)
    c.setAttribute("cx",x)
    c.setAttribute("cy",y)
    c.setAttribute("fill",random_rgb())
    l0.appendChild(c)
    v = new verletable(c)
    verletables.add_verletable(v)
}

var verletables = new verletable_handler;

gen_ball(256,256)
gen_ball(364,512)



function get_all_layers(){
    return [...document.getElementsByClassName("layers")];
}

function gen_field() {
    var l0 = get_all_layers()[0];
    clr = random_rgb()
    re = document.createElementNS( "http://www.w3.org/2000/svg", "rect" )
    re.setAttribute("x",128-32); re.setAttribute("y",64); re.setAttribute("width",64);
    re.setAttribute("height",2048-64-64);
    re.setAttribute("fill",clr);
    re.classList.add("boundary");
    l0.appendChild(re);
    re = document.createElementNS( "http://www.w3.org/2000/svg", "rect" )
    re.setAttribute("x",2048-128-32); re.setAttribute("y",64); re.setAttribute("width",64);
    re.setAttribute("height",2048-64-64);
    re.setAttribute("fill",clr);
    re.classList.add("boundary");
    l0.appendChild(re);
    re = document.createElementNS( "http://www.w3.org/2000/svg", "rect" )
    re.setAttribute("x",128-32); re.setAttribute("y",2048-64-64); re.setAttribute("width",2048-128-128+64);
    re.setAttribute("height",64);
    re.setAttribute("fill",clr);
    re.classList.add("boundary");
    l0.appendChild(re);
}

gen_field()

function random_rgb() {
    var o = Math.round, r = Math.random, s = 32 ; offset=32;
    return 'rgb(' + o(r()*s + offset ) +
               ',' + o(r()*s + offset ) +
               ',' + o(r()*s + offset ) + ')';
}

function random_rgb_light() {
    var o = Math.round, r = Math.random, s = 32 ; offset=32;
    return 'rgba(' + o(r()*s + offset ) +
               ',' + o(r()*s + offset ) +
               ',' + o(r()*s + offset ) + ',.95)';
}

svg = document.getElementById("total_svg")
pt = svg.createSVGPoint();  // Created once for document
last_mouse_svg_coods = [0,0];
function get_mouse_svg_coods(evt) {
    pt.x = evt.clientX;
    pt.y = evt.clientY;
    // The cursor point, translated into svg coordinates
    var cursorpt =  pt.matrixTransform(svg.getScreenCTM().inverse());
    cursorpt.x = parseInt(cursorpt.x);
    cursorpt.y = parseInt(cursorpt.y);
    x = cursorpt.x;
    y = cursorpt.y;
    last_mouse_svg_coods = [x,y];
    //move_cursor(x,y)
    return x,y
}
svg.addEventListener('mousemove',get_mouse_svg_coods)

function physics_process(delta) {
    verletables.move_verletables(delta)
}

bind_to_clock_tick(physics_process,50)
