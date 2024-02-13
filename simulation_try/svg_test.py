import math
from browser import document, svg, alert
from random import randint

def random_colour():
    def inttohex(i:int)->str:
        i = i % 16
        if 0<=i<=9:
            return f"{i}"
        match i:
            case 10:
                return "A"
            case 11:
                return "B"
            case 12:
                return "C"
            case 13:
                return "D"
            case 14:
                return "E"
            case 15:
                return "F"
    return "#" +"".join([ inttohex(randint(0,16)) for _ in range(3) ])

def gen_test_ball_grid(Z,S):
    ball_lists = []
    for col in range(S):
        for row in range(Z):
            label = f"hole_{row}_{col}"
            x,y = 128+128*row,128+128*col
            res = add_ball_at(x,y,label)
            if res != None:
                ball_lists = ball_lists + [res,]
    #print(ball_lists)

def gen_bdy():
    bdy_colour = random_colour()

    SVGRoot <= svg.rect(
            id=f"left_bdy",
            x=bdy_size,
            y=bdy_size,
            width=bdy_size,
            height=Y-2*bdy_size,
            style={"fill":bdy_colour}
        )

    SVGRoot <= svg.rect(
            id=f"left_bdy",
            x=X-2*bdy_size,
            y=bdy_size,
            width=bdy_size,
            height=Y-2*bdy_size,
            style={"fill":bdy_colour}
        )

    SVGRoot <= svg.rect(
            id=f"left_bdy",
            x=bdy_size,
            y=Y-2*bdy_size,
            width=X-2*bdy_size,
            height=bdy_size,
            style={"fill":bdy_colour}
        )

SVGRoot = document["svg_root"]

viewport_size = 2048
X,Y = viewport_size, viewport_size
bdy_size = 64

def add_ball_at(x,y,label,colour=""):
    if colour == "":
        colour = random_colour()
    if ( 128+32 <= x <= 2048 - 128 - 32 ) \
    and ( 128+32 <= y <= 2048 - 128 - 32 ):
        c = \
        svg.circle(
            id = label,
            cx = x,
            cy = y,
            r = 32,
            style={"fill":colour}
            )
        c.classList.add("balls")
        SVGRoot <= c
        return c
    return None

gen_bdy()
#gen_test_ball_grid(15,15)

#SVGRoot.bind('click',add_ball_at)