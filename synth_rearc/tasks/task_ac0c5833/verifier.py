from synth_rearc.core import *

from .helpers import (
    extract_seed_data_ac0c5833,
    place_canonical_patch_ac0c5833,
)


def verify_ac0c5833(I: Grid) -> Grid:
    x0, _, _, x1 = extract_seed_data_ac0c5833(I)
    x2 = I
    for x3, x4, _ in x1:
        x5 = place_canonical_patch_ac0c5833(x0, x3, x4)
        x6 = recolor(TWO, x5)
        x2 = underpaint(x2, x6)
    return x2
