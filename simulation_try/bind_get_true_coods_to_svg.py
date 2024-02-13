import math
from browser import document #, svg, alert
SVGRoot = document["svg_root"]
svg_coods = SVGRoot.createSVGPoint()
def GetTrueCoords(evt):
  svg_coods.x = evt.clientX
  svg_coods.y = evt.clientY
  cursor_pt = svg_coods.matrixTransform(SVGRoot.getCTM().inverse())
  print(f"SVG click coods: {(int(cursor_pt.x),int(cursor_pt.y))}")
SVGRoot.bind('click',GetTrueCoords)