# texplt - LaTex-friendly matplotlib figures

*texplt* is a set of python scripts to prepare matplotlib figures for publishing. Tested with IEEE LaTex style. Based on latexify [1].

## Installation

Copy or symlink the **texplt/texplt** folder containing the python package into your project folder.

## Usage

First import the two functions texSaveFig and texFigure.

```python
from texplt import texSaveFig, texFigure
```

Use texFigure() instead of figure() and texSaveFig() instead of savefig(). Both functions are wrappers for their matplotlib counterparts and accept/return the same arguments.

## Examples

Minimal working example:

```python
from pylab import *
from texplt import texSaveFig, texFigure

texFigure()

plot(list(range(1, 10)))

texSaveFig("test.pdf")
```

## FAQ
**Linux: Why is the font in the PDF figure not Times New Roman?** 

You may have to install the msttcorefonts package:
```bash
sudo apt-get --reinstall install msttcorefonts
```

Afterwards you may have to clear your matplotlib font cache:

```bash
rm -r ~/.matplotlib/tex.cache/
rm -r ~/.cache/matplotlib/tex.cache/
```

## References

[1] http://nipunbatra.github.io/2014/08/latexify/
