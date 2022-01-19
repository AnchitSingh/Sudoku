import cairocffi as cairo
def backtopng(fil,res):
    with cairo.SVGSurface(fil, 700, 700) as surface:
        context = cairo.Context(surface)
        context.rectangle(100, 100, 100, 100)
        context.rectangle(500, 100, 100, 100)
        x, y, x1, y1 = 0.1, 0.5, 0.4, 0.9
        x2, y2, x3, y3 = 0.4, 0.1, 0.9, 0.6
        context.scale(700, 700)
        context.set_line_width(0.04)
        context.move_to(x, y)
        context.curve_to(x1, y1, x2, y2, x3, y3)
        context.set_source_rgba(0.4, 1, 0.4, 1)
        context.stroke()
        surface.write_to_png(res)

backtopng('000_3.svg','000_4.png')