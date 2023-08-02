def gen_rocky_svg()->str:
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
    <svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024">
    """
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
    one_hex = \
    f"""
      <path
           style=" fill:{get_css_color(127,0,31)};
                   stroke:{get_css_color(0,127,31)};
                   stroke-width:16"
           d="
           M110 14
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
                z" transform="translate(42,12)">
    </path>
    """
    svg_outro = """</svg>
                    </body>
                    <style type="text/css">
                       html,body {
                          height: 100%;
                          width: 100%;
                          margin: 0;
                       }
                       body {
                          border: 2px solid;
                          border-color: #cc1199;
                       }
                       html {
                          background-color: #000;
                       }
                    </style>
                    </html>"""
    svg_string = svg_plus_black_bg_intro + \
                   '\n' + \
                   fingerprint_svg_path + \
                   '\n' + \
                   one_hex + \
                   '\n' + \
                   svg_outro
    print(svg_string)
    print(); print(); print()
    import time
    fname = f'gen_svg_{time.strftime("%y%m%d_%H%M")}.html'
    print(f"++++ writing file: {fname} ++++")
    with open(fname,'w') as fi:
        fi.write(svg_string)
    return fname

def get_css_color(r:int,g:int,b:int)->str:
    return f"rgb({r},{g},{b})"

if __name__=="__main__":
    import webbrowser
    fname = gen_rocky_svg()
    webbrowser.open(f"http://localhost:8080/{fname}")
