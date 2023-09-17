b = document.getElementsByTagName("body")[0]
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
bg_clr.setAttribute("fill","#0c0a0c")
svg_frame.appendChild(bg_clr)

for ( let i = 0; i < layer_count; i++ ) {
    svg = document.createElementNS("http://www.w3.org/2000/svg","svg")
    svg.id = `layer_${i}`
    svg.setAttribute("viewBox",`0 0 ${vbx} ${vbx}`)
    svg.classList.add("layers")
    svg_frame.appendChild(svg)
    if ( i == 0 ) {
        first_layer = svg
    }
    if ( i == layer_count - 1 ) {
        last_layer = svg
    }
}

svg = document.createElementNS("http://www.w3.org/2000/svg","svg")
svg.id = 'cursor_layer'
svg.setAttribute("viewBox",`0 0 ${vbx} ${vbx}`)
svg.classList.add("layers")
svg_frame.appendChild(svg)

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
            c.setAttribute("r",24)
            c.setAttribute("fill",random_rgb_light())
            c.classList.add("cursor")
            d = document.createElementNS( "http://www.w3.org/2000/svg", "circle" )
            d.setAttribute("cx",x)
            d.setAttribute("cy",y)
            d.setAttribute("r",12)
            d.setAttribute("fill",random_rgb())
            d.classList.add("cursor")
            svg_frame = document.getElementById('cursor_layer')
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

function draw_classy_circle(cx,cy,r,cls,bg,clr){
    c = document.createElementNS( "http://www.w3.org/2000/svg", "circle" )
    c.setAttribute("cx",cx)
    c.setAttribute("cy",cy)
    c.setAttribute("r",r)
    if ( ( bg == undefined ) || !( bg ) ){
        if ( ( clr == undefined ) || !( clr )) {
            c.setAttribute("fill",random_rgb_light())
        } else {
            c.setAttribute("fill",clr)
        }
    } else {
        c.setAttribute("fill","#000")
    }
    c.classList.add(cls)
    last_layer.appendChild(c)
    return c;
}

function create_classy_line(x,y,u,v,cls,wdth,bg,clr) {
    l = document.createElementNS( "http://www.w3.org/2000/svg", "line" )
    l.setAttribute("x1",x)
    l.setAttribute("y1",y)
    l.setAttribute("x2",u)
    l.setAttribute("y2",v)
    l.setAttribute("stroke-linecap",'round')
    if ( ( bg != undefined ) && ( !(!bg) ) ) {
        l.setAttribute('stroke','#000')
    } else if ( ( clr != undefined ) && ( !(!clr) ) ) {
        l.setAttribute('stroke',clr)
    } else {
        l.setAttribute('stroke',random_rgb_light())
    }
    if ( wdth == undefined ) {
        wdth = 2
    }
    l.setAttribute('stroke-width',wdth)
    l.classList.add(cls)
    return l;
}

function draw_classy_line(x,y,u,v,cls,wdth,bg,clr) {
    l = create_classy_line(x,y,u,v,cls,wdth,bg,clr)
    first_layer.appendChild(l)
    return l;
}

function svg_group(xs){
    //TODO: return group g of svg elements xs
}

function draw_classy_arrow(x,y,u,v,cls,wdth) {
    g = document.createElementNS( "http://www.w3.org/2000/svg", "g" )
    g.classList.add(cls)
    dx = x-u; dy = y-v;
    d = Math.sqrt( dx**2 + dy**2 )
    dx = parseInt(32*dx/d); dy = parseInt(32*dy/d)
    x = x - 2*dx; y = y - 2*dy;
    u = u + 2*dx; v = v + 2*dy;
    nx = -dy; ny = dx;
    n = Math.sqrt( nx**2 + ny**2 )
    nx = parseInt(32*nx/n); ny = parseInt(32*ny/n)
    l1 = create_classy_line(parseInt(x),parseInt(y),
                     parseInt(u),parseInt(v),
                     cls,wdth,
                     true,false)
    l2 = create_classy_line(parseInt(u),parseInt(v),
                     parseInt(u+.5*nx+1.5*dx),
                     parseInt(v+.5*ny+1.5*dy),
                     cls,wdth,
                     true,false)
    l3 = create_classy_line(parseInt(u),parseInt(v),
                     parseInt(u-.5*nx+1.5*dx),
                     parseInt(v-.5*ny+1.5*dy),
                     cls,wdth,
                     true,false)
    w_offset = 6
    l4 = create_classy_line(
                     parseInt(x),parseInt(y),
                     parseInt(u),parseInt(v),
                     cls,wdth-w_offset,
                     false,false)
    clr = l4.getAttribute("stroke")
    l5 = create_classy_line(parseInt(u),parseInt(v),
                     parseInt(u+.5*nx+1.5*dx),
                     parseInt(v+.5*ny+1.5*dy),
                     cls,wdth-w_offset,
                     false,clr)
    l6 = create_classy_line(parseInt(u),parseInt(v),
                     parseInt(u-.5*nx+1.5*dx),
                     parseInt(v-.5*ny+1.5*dy),
                     cls,wdth-w_offset,
                     false,clr)
    ls = [l1,l2,l3,l4,l5,l6]
    for ( let i = 0; i < ls.length; i++ ){
        g.appendChild(ls[i])
    }
    first_layer.appendChild(g)
    return g
}

function draw_classy_square(x,y,width,cls,bg_clr) {
    if ( (bg_clr == undefined) ){
        bg_clr = "#805"
        first_offset=16
    } else {
        first_offset=10
    }
    width = width + first_offset
    height = width
    x_ = parseInt(x - width/2)
    y_ = parseInt(y - height/2)
    r = document.createElementNS("http://www.w3.org/2000/svg","rect")
    hover_square = r
    r.setAttribute("x",x_)
    r.setAttribute("y",y_)
    r.setAttribute("width",width)
    r.setAttribute("height",height)
    if ( (bg_clr == undefined) ){
        bg_clr = "#805"
    }
    r.setAttribute("fill",bg_clr)
    r.setAttribute("rx",20)
    r.classList.add(cls)
    r.style.display = 'none';
    r1 = r
    width = width - first_offset
    height = width
    x_ = parseInt(x - width/2)
    y_ = parseInt(y - height/2)
    r = document.createElementNS("http://www.w3.org/2000/svg","rect")
    r.setAttribute("x",x_)
    r.setAttribute("y",y_)
    r.setAttribute("width",width)
    r.setAttribute("height",height)
    r.setAttribute("fill","#000")
    r.setAttribute("rx",16)
    r.classList.add(cls)
    r2 = r
    bdy_offset = 24
    x_ = parseInt( x_ + bdy_offset/2 )
    y_ = parseInt( y_ + bdy_offset/2 )
    r = document.createElementNS("http://www.w3.org/2000/svg","rect")
    r.setAttribute("x",x_)
    r.setAttribute("y",y_)
    r.setAttribute("width",width-bdy_offset)
    r.setAttribute("height",height-bdy_offset)
    r.setAttribute("fill",random_rgb_light())
    r.setAttribute("rx",8)
    r.classList.add(cls)
    r3 = r
    g = document.createElementNS("http://www.w3.org/2000/svg","g")
    g.appendChild(r1)
    g.appendChild(r2)
    g.appendChild(r3)
    g.classList.add(cls)
    last_layer.appendChild(g)
    return g
}