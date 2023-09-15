b = document.getElementsByTagName("body")[0]

vbx = 2048
layer_count = 5

svg_frame = document.createElementNS("http://www.w3.org/2000/svg","svg")
svg_frame.id = 'total_svg1'
svg_frame.setAttribute("width","90vw")
svg_frame.setAttribute("height","95vh")
svg_frame.setAttribute("margin","max(4px,1vh,1vw)")
svg_frame.setAttribute("viewBox",`0 0 ${vbx} ${vbx}`)
b.appendChild(svg_frame)

bg_clr = document.createElementNS("http://www.w3.org/2000/svg","rect")
bg_clr.setAttribute("x",0)
bg_clr.setAttribute("y",0)
bg_clr.setAttribute("width",`${vbx}`)
bg_clr.setAttribute("height",`${vbx}`)
bg_clr.setAttribute("fill","#111")
svg_frame.appendChild(bg_clr)

for ( let i = 0; i < layer_count; i++ ) {
    svg = document.createElementNS("http://www.w3.org/2000/svg","svg")
    svg.id = `layer_${i}`
    svg.setAttribute("viewBox",`0 0 ${vbx} ${vbx}`)
    svg.classList.add("layers")
    svg_frame.appendChild(svg)
}

function get_all_layers(){
    return [...document.getElementsByClassName("layers")];
}

svg = document.getElementById("total_svg1")
pt = svg.createSVGPoint();  // Created once for document
h = document.getElementsByTagName('html')[0]

function get_svg_xy_from_event(evt) {
    pt.x = evt.clientX;
    pt.y = evt.clientY;
    // The cursor point, translated into svg coordinates
    var cursorpt =  pt.matrixTransform(svg.getScreenCTM().inverse());
    cursorpt.x = parseInt(cursorpt.x);
    cursorpt.y = parseInt(cursorpt.y);
    x = cursorpt.x;
    y = cursorpt.y;
    return [x,y];
}

function get_mouse_svg_coods(evt) {
    function move_cursor(x,y) {
        cursors = document.getElementsByClassName("cursor")
        if ( cursors.length == 0 ) {
            c = document.createElementNS( "http://www.w3.org/2000/svg", "circle" )
            c.setAttribute("cx",x)
            c.setAttribute("cy",y)
            c.setAttribute("r",32)
            c.setAttribute("fill",random_rgb_light())
            c.classList.add("cursor")
            d = document.createElementNS( "http://www.w3.org/2000/svg", "circle" )
            d.setAttribute("cx",x)
            d.setAttribute("cy",y)
            d.setAttribute("r",20)
            d.setAttribute("fill",random_rgb())
            d.classList.add("cursor")
            svg_frame = get_all_layers()[0]
            svg_frame.appendChild(c)
            svg_frame.appendChild(d)
        }
        cursor = document.getElementsByClassName("cursor")[0]
        cursor.setAttribute("cx",x)
        cursor.setAttribute("cy",y)
        cursor = document.getElementsByClassName("cursor")[1]
        cursor.setAttribute("cx",x)
        cursor.setAttribute("cy",y)
    }
    tmp = get_svg_xy_from_event(evt)
    x = tmp[0]; y = tmp[1]
    if ((x <= 0) || (x>=4096) || (y <= 0) || (y>=4096)) {
        h.style.cursor = 'crosshair'
        return
    }
    h.style.cursor = 'none'
    last_mouse_svg_coods = [x,y];
    move_cursor(x,y)
}

svg.addEventListener('mousemove',get_mouse_svg_coods)