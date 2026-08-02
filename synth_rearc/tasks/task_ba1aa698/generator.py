from synth_rearc.core import *

from .helpers import (
    HEIGHT_BA1AA698,
    INNER_WIDTH_CHOICES_BA1AA698,
    NONZERO_COLORS_BA1AA698,
    PANEL_COUNT_BOUNDS_BA1AA698,
    assemble_input_ba1aa698,
    build_panel_ba1aa698,
    motif_choices_ba1aa698,
)


STEP_BOUNDS_BA1AA698 = (ONE, THREE)


def _sample_colors_ba1aa698() -> Tuple:
    x0 = choice(NONZERO_COLORS_BA1AA698)
    x1 = choice(tuple(x2 for x2 in NONZERO_COLORS_BA1AA698 if x2 != x0))
    x2 = tuple(x3 for x3 in NONZERO_COLORS_BA1AA698 if x3 != x1)
    return x0, x1, choice(x2)


def _sample_layout_ba1aa698(
    diff_lb: float,
    diff_ub: float,
) -> Tuple:
    while True:
        x0 = unifint(diff_lb, diff_ub, PANEL_COUNT_BOUNDS_BA1AA698)
        x1 = choice(INNER_WIDTH_CHOICES_BA1AA698)
        x2 = choice(motif_choices_ba1aa698(x1))
        x3, x4, x5 = _sample_colors_ba1aa698()
        x6 = unifint(diff_lb, diff_ub, STEP_BOUNDS_BA1AA698)
        x7 = choice((NEG_ONE, ONE))
        x8 = multiply(x6, x7)
        x9 = height(x2)
        x10 = HEIGHT_BA1AA698 - x9 - TWO
        x11 = randint(TWO, x10)
        x12 = x11 - x0 * x8
        x13 = tuple(x12 + x14 * x8 for x14 in range(x0))
        if min(x13) < TWO or max(x13) > x10:
            continue
        return x1, x2, x3, x4, x5, x13, x11


def generate_ba1aa698(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0, x1, x2, x3, x4, x5, x6 = _sample_layout_ba1aa698(diff_lb, diff_ub)
        x7 = tuple(build_panel_ba1aa698(HEIGHT_BA1AA698, x0, x2, x3, x1, x4, x8) for x8 in x5)
        x8 = assemble_input_ba1aa698(x7)
        x9 = build_panel_ba1aa698(HEIGHT_BA1AA698, x0, x2, x3, x1, x4, x6)
        if x8 == x9:
            continue
        return {"input": x8, "output": x9}
