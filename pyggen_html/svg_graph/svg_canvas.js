b = document.getElementsByTagName("body")[0]

vbx = 2048

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