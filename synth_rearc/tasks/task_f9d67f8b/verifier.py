from synth_rearc.core import *


def verify_f9d67f8b(I: Grid) -> Grid:
    x0 = replace(I, NINE, ZERO)
    x1 = canvas(ZERO, (32, 32))
    x2 = paint(x1, asobject(x0))
    x3 = vmirror(x2)
    x4 = hmirror(x2)
    x5 = hmirror(x3)
    x6 = x2
    for x7 in interval(ONE, NINE, ONE):
        x8 = fill(x6, x7, ofcolor(x3, x7))
        x9 = fill(x8, x7, ofcolor(x4, x7))
        x6 = fill(x9, x7, ofcolor(x5, x7))
    x10 = crop(x6, ORIGIN, (30, 30))
    x11 = ofcolor(x10, ZERO)
    x12 = toobject(x11, dmirror(x10))
    x13 = paint(x10, x12)
    return x13
