def gen_rocky_svg()->str:
    def gen_hexes()->str:
        tmp = ""
        for i in range(7):
            for j in range(7):
                trsl_vector = f"""{100+215*i+108*(j%2)},{16+190*j}"""
                print(trsl_vector)
                one_hex = \
                f"""
                  <path
                       style=" fill:{get_css_color(32+32*i,32*j,31,.5)};
                               stroke:{get_css_color(32*j,32*(1+i),31,.5)};"
                       d="
                            M   0   0
                            a  40  40 0 0 1  40   0
                            l  70  40
                            a  40  40 0 0 1  20  36
                            l   0  80
                            a  40  40 0 0 1 -20  36
                            l -70  40
                            a  40  40 0 0 1 -40   0
                            l -70 -40
                            a  40  40 0 0 1 -20 -36
                            l   0 -80
                            a  40  40 0 0 1  20 -36
                            z" transform="translate({trsl_vector})">
                </path>
                """
                tmp += one_hex
        return tmp
    svg_plus_black_bg_intro = \
    """
    <!DOCTYPE html>
    <html>
    <head>
    <link rel="icon" type="image/png" href="favicon-32x32.png" sizes="32x32" />
    <link rel="icon" type="image/png" href="favicon-16x16.png" sizes="16x16" />
    <meta charset="UTF-8">
    <title>🖌️SVG Canvas🖼️</title>
    </head>
    <body>
    <svg xmlns="http://www.w3.org/2000/svg" width="90vw" height="95vh" margin="max(4px,1vh,1vw)" viewBox="0 0 2048 2048">"""
    fingerprint_svg_path = \
    f"""
    <path
      style=" fill:none;
                   stroke:{get_css_color(0,127,0)};
                   stroke-width:1"
    d = "M 3 15
         q 1 -2 1 -5
         q 0 -2 2 -4
         M 8 4
         a 8 8 0 0 1 12 6
         q 1 4 -2 9
         M 13 21
         q 2 -2 2 -5
         M 16 12
         v -1
         a 4 4 0 0 0 -8 0
         q 0 4 -3 7
         M 9 20
         q 3 -3 4 -9"
    >
    </path>
    """
    svg_outro = """</svg>
                    </body>
                    style type="text/css">
                       html {
                           background-color: #000;
                       }
                       body {
                           margin: 0;
                       }
                       svg {
                         display: block;
                         border: 1px solid #ccc;
                         position: absolute;
                         top: 5%;
                         left: 5%;
                         width: 90%;
                         height: 90%;
                         background: #000;
                       }
                    </style>
                    </html>"""
    svg_string = svg_plus_black_bg_intro + \
                   '\n' + \
                   gen_hexes() + \
                   '\n' + \
                   svg_outro
    #print(svg_string)
    print(); print(); print()
    import time
    fname = f'gen_svg_{time.strftime("%y%m%d_%H%M")}.html'
    print(f"++++ writing file: {fname} ++++")
    with open(fname,'w') as fi:
        fi.write(svg_string)
    return fname

def get_css_color(r:int,g:int,b:int,a:float=1)->str:
    return f"rgba({r},{g},{b},{a})"

if __name__=="__main__":
    import webbrowser
    fname = gen_rocky_svg()
    webbrowser.open(f"http://localhost:8080/{fname}")
