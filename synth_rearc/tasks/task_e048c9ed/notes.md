The grid contains a `5` marker in the top row and horizontal bars below it. The marker's
column is the output column. A digit is added in that column on every bar's row.

Normally, sort the distinct bar lengths from shortest to longest and number them from 1.
The digit for a bar is the last digit of its squared number, giving the sequence
`1, 4, 9, 6` for the first four distinct lengths. Repeated lengths receive the same digit.

One official pair demonstrates an outlier variant. If exactly one length is repeated and
exactly one other length occurs once, a non-consecutive singleton is measured from the
repeated reference length. Its digit is the last digit of the squared length difference.
Thus the three length-2 bars in that pair receive `1`, while the sole length-5 bar is three
cells longer and receives `3^2 = 9`.

The generator uses consecutive length classes for ordinary ranking examples and sometimes
creates the repeated-reference/outlier arrangement. This avoids unsupported skipped ranks
such as two ordinary length classes being labeled with the first and third rank colors.
