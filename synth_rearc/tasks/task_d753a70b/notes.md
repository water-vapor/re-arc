The rule is color-dependent: diagonal diamond-outline components of color `2` contract by one Manhattan layer, components of color `5` expand by one Manhattan layer, and passive colors such as `8` and `9` stay unchanged.

The color-`5` bottom-border wedge in training pair 0 was an erroneous outlier: its expanded output had been shifted one column right. The official output was corrected to preserve the common diamond center, eliminating the task-specific verifier and generator exceptions.
