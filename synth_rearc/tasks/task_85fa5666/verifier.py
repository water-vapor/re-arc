from synth_rearc.core import *

from .helpers import corner_specs_85fa5666, paint_diagonal_ray_85fa5666


def verify_85fa5666(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, TWO)
    x2 = sizefilter(x1, FOUR)
    x3 = sfilter(x2, square)
    x4 = tuple(sorted(x3, key=ulcorner))
    x5 = canvas(ZERO, shape(I))
    for x6 in x4:
        x5 = fill(x5, TWO, x6)
    for x6 in x4:
        x7 = corner_specs_85fa5666(I, ulcorner(x6))
        for x8, x9, x10 in x7:
            x5 = paint_diagonal_ray_85fa5666(x5, x8, x10, x9)
    return x5
