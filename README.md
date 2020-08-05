# lpngram

[![Build Status](https://travis-ci.org/lingpy/lpngram.svg?branch=master)](https://travis-ci.org/lingpy/lpngram)
[![codecov](https://codecov.io/gh/lingpy/lpngram/branch/master/graph/badge.svg)](https://codecov.io/gh/lingpy/lpngram)
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

The library operates on any kind of Python iterable, such as strings, lists, and tuples.
Methods allow to collect normal ngrams, skip n-grams, and positional n-grams.
Different left and right orders can be specified, as well as different padding
symbols (if any).

The example below collects ngrams with a left order of at most 1 and a right order of
at most 2 from a short list with three country names.

```python
>>> import lpngram
>>> words = ['Germany', 'Italy', 'Brazil']
>>> model = lpngram.NgramModel(1, 2, sequences=words)
```

Even without smoothing, the model allows to query counters for specific contexts. Here
we investigate which characters are found preceding an `a`, which are found
between `G` and `r`, and the full list of characters with their counts:

```python
>>> model._ngrams['###', 'a']
Counter({'m': 1, 't': 1, 'r': 1})
>>> model._ngrams['G', '###', 'r']
Counter({'e': 1})
>>> model._ngrams['###',]
Counter({'a': 3, 'r': 2, 'y': 2, 'l': 2, 'G': 1, 'e': 1, 'm': 1, 'n': 1,
'I': 1, 't': 1, 'B': 1, 'z': 1, 'i': 1})
```

For most operations, smoothing is necessary or recommended. The library includes a
range on smoothing methods, including one developed for linguistic investigation
purposes and based on degree of certainty. Here we perform smoothing with Lidstone's,
method, a gamma of 0.1, no normalization:

```python
>>> model.train(method='lidstone', gamma=0.1)
>>> model._p['###', 'a']
{'m': -1.363304842895192, 't': -1.363304842895192, 'r': -1.363304842895192}
>>> model._p['G', '###', 'r']
{'e': -0.737598943130779}
>>> model._p['###',]
{'G': -2.864794916106515, 'e': -2.864794916106515, 'r': -2.2181677511814626,
'm': -2.864794916106515, 'a': -1.8287029844197393, 'n': -2.864794916106515,
'y': -2.2181677511814626, 'I': -2.864794916106515, 't': -2.864794916106515,
'l': -2.2181677511814626, 'B': -2.864794916106515, 'z': -2.864794916106515,
'i': -2.864794916106515}
```

The smoothed distribution allows to perform the main purpose of the library, which
is to score the likelihood of sequences:

```python
>>> model.score("Italy")
-35.461238155043674
>>> [model.score(word) for word in ["Italy", "Itazily", "France"]]
[-35.461238155043674, -106.65033225683297, -240.5559013433157]
```

We can also compute the internal measures of entropy and perplexity:

```python
>>> model.model_entropy()
62.59647855466861
>>> model.entropy('Itazil')
17.095797405180004
>>> model.perplexity('Itazil')
140070.86762308443
>>> [model.entropy(word) for word in ["Italy", "Itazily", "France"]]
[10.231950486012801, 21.980557922299024, 57.84146765409605]
>>> [model.perplexity(word) for word in ["Italy", "Itazily", "France"]]
[1202.6077837373584, 4138159.7865280183, 2.5823598282235027e+17]
```

With a smoothed distribution, we can use other methods such as generation of random
strings:

```python
>>> model.random_seqs(k=4)
[('B', 'r', 'a', 'z', 'i', 'l'), ('I', 't', 'a', 'z', 'i', 'l'),
('G', 'e', 'r', 'm', 'a', 'n', 'y'), ('I', 't', 'a', 'z', 'i', 'l', 'y')]
```

Detailed usage is demonstrated in the tests suits. Full documentation and examples will
be provided in future versions.

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
