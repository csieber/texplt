# texplt - LaTex-friendly matplotlib figures

*texplt* is a set of python scripts to prepare matplotlib figures for publishing. Tested with IEEE LaTex style.

## Usage

First import the two functions texSaveFig and texFigure.

```python
from texplt import texSaveFig, texFigure
```

Use texFigure() instead of figure() and texSaveFig() instead of savefig(). Both functions accept the same arguments as their matplotlib counterparts. 

## Examples

Minimal working example:

´´´python
from pylab import *
from texplt import texSaveFig, texFigure

texFigure()

plot(list(range(1, 10)))

texSaveFig("test.pdf")
´´´