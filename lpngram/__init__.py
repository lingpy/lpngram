# __init__.py

"""
lpngram __init__.py
"""

# Version of the ngesh package
__version__ = "0.1.1"
__author__ = "Tiago Tresoldi; Johann-Mattis-List"
__email__ = "tresoldi@shh.mpg.de"

# Build the namespace
from lpngram.ngrams import NgramModel
from lpngram.ngrams import (
    get_n_ngrams,
    get_all_ngrams_by_order,
    get_skipngrams,
    get_posngrams,
    get_all_posngrams,
)
from lpngram.ngrams import bigrams, trigrams, fourgrams
from lpngram.ngrams import get_all_ngrams

from lpngram.smoothing import smooth_dist
from lpngram.smoothing import (
    uniform_dist,
    random_dist,
    mle_dist,
    lidstone_dist,
    laplace_dist,
    ele_dist,
    wittenbell_dist,
    certaintydegree_dist,
    sgt_dist,
)
