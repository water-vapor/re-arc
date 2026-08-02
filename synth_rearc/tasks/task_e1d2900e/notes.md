`arc2_opus46_summary.json` was the useful starting hint for `e1d2900e`: the rule is that a singleton `1` on one of a `2x2` block's two rows or two columns slides straight inward to the adjacent side cell of the nearest such block, while unaligned `1`s stay put.

The original second training output had an annotation error: the `1` at `(23, 13)` was left unchanged even though it is aligned with the lower-right block. The corrected output moves it to `(23, 19)`, consistently with every other official example and the generated task family.
