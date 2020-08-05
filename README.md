# lpngram

[![Build Status](https://travis-ci.org/lingpy/lpngram.svg?branch=master)](https://travis-ci.org/lingpy/lpngram)
[![codecov](https://codecov.io/gh/tresoldi/ngesh/branch/master/graph/badge.svg)](https://codecov.io/gh/tresoldi/ngesh)
[![PyPI](https://img.shields.io/pypi/v/lpngram.svg)](https://pypi.org/project/lpngram)

Python library for ngram collection and frequency smoothing.

`lpngram` is a pure-Python implementation of methods for ngram collection and frequency
smoothing, originally part of the [`lingpy`](http://lingpy.org/) library. It has no
dependencies, but will use `numpy` and `scipy`, if available, to speed smoothing
computations. It was designed to work on any kind of sequence, not just words, and
has been successfully used to collect phoneme n-grams.

## Changelog

Version 0.1:
  - First public release.

## Installation

In any standard Python environment, `lpngram` can be installed with:

```bash
pip install lpngram
```

The `pip` installation will also fetch the dependencies `numpy` and `scipy`. If those
are not desired, the library can be used by just copying the files in the
`lpngram` directory.

## How to use

Lorem ipsum

## Community guidelines

Contributing guidelines can be found in the `CONTRIBUTING.md` file.

## Authors and citation

The library is developed by Tiago Tresoldi (tresoldi@shh.mpg.de) and
Johann-Mattis List (list@shh.mpg.de).

The authors have received funding from the European Research Council (ERC) under the
European Union’s Horizon 2020 research and innovation programme (grant agreement
No. [ERC Grant #715618](https://cordis.europa.eu/project/rcn/206320/factsheet/en),
[Computer-Assisted Language Comparison](https://digling.org/calc/).

If you use `lpngram`, please cite it as:

> Tresoldi, Tiago; List, Johann-Mattis (2020). lpngram, a Python library for ngram
collection and frequency smoothing. Version 0.1. Jena: Max Planck Institute for the Science of Human History.
Available at: https://github.com/lingpy/lpngram

In BibTeX:

```
@misc{Tresoldi2020lpngram,
  author = {Tresoldi, Tiago; List, Johann-Mattis},
  title = {lpngram, a Python library for ngram collection and frequency smoothing. Version 0.1},
  howpublished = {\url{https://github.com/lingpy/lpngram}},
  address = {Jena},
  publisher = {Max Planck Institute for the Science of Human History},
  year = {2020},
}
```
