#!/usr/bin/env python3
# pylint: disable=no-self-use

"""
test_lpngram
============

Tests for the `lpngram` package.
"""

# Import Python libraries
import unittest
from collections import Counter
import itertools
import random
import string

# Import the library itself
# TODO: don't import with *
from lpngram import *

# Note on test implementation: we can't directly compare the reference list and the
# list of returned elements, as the lists might have
# different orders; we also cannot convert them to
# sets and compare the sets, as we would miss duplicates.
# The best solution is to make counters out of both lists
# and compare them (no problem as the iterator returns
# tuples, which are hasheable)
class TestLPNgram(unittest.TestCase):
    """
    Suite of tests for the `lpngram` library.
    """

    def test_get_n_grams(self):
        # String and list sequences
        str_seq = "A B C"
        lst_seq = str_seq.split()

        # The length of the collections of 0-grams must be zero
        assert len(list(get_n_ngrams(str_seq, 0))) == 0
        assert len(list(get_n_ngrams(lst_seq, 0))) == 0

        # Test monogram (no padding)
        ref = Counter([("A",), ("B",), ("C",)])
        assert ref == Counter(get_n_ngrams(str_seq, 1))
        assert ref == Counter(get_n_ngrams(lst_seq, 1))

        # Test large n-gram with padding
        ref = Counter(
            [
                ("$$$", "$$$", "$$$", "$$$", "A"),
                ("$$$", "$$$", "$$$", "A", "B"),
                ("$$$", "$$$", "A", "B", "C"),
                ("$$$", "A", "B", "C", "$$$"),
                ("A", "B", "C", "$$$", "$$$"),
                ("B", "C", "$$$", "$$$", "$$$"),
                ("C", "$$$", "$$$", "$$$", "$$$"),
            ]
        )
        assert ref == Counter(get_n_ngrams(str_seq, 5))
        assert ref == Counter(get_n_ngrams(lst_seq, 5))

    def test_bigrams(self):
        # String and list sequences
        str_seq = "A B C D E"
        lst_seq = str_seq.split()

        # Test with padding
        ref = Counter(
            [("$$$", "A"), ("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "$$$")]
        )
        assert ref == Counter(bigrams(str_seq))
        assert ref == Counter(bigrams(lst_seq))

        # Test without padding
        ref = Counter([("A", "B"), ("B", "C"), ("C", "D"), ("D", "E")])
        assert ref == Counter(bigrams(str_seq, pad_symbol=None))
        assert ref == Counter(bigrams(lst_seq, pad_symbol=None))

    def test_trigrams(self):
        # String and list sequences
        str_seq = "A B C D E"
        lst_seq = str_seq.split()

        # Test with padding
        ref = Counter(
            [
                ("$$$", "$$$", "A"),
                ("$$$", "A", "B"),
                ("A", "B", "C"),
                ("B", "C", "D"),
                ("C", "D", "E"),
                ("D", "E", "$$$"),
                ("E", "$$$", "$$$"),
            ]
        )
        assert ref == Counter(trigrams(str_seq))
        assert ref == Counter(trigrams(lst_seq))

        # Test without padding
        ref = Counter([("A", "B", "C"), ("B", "C", "D"), ("C", "D", "E")])
        assert ref == Counter(trigrams(str_seq, pad_symbol=None))
        assert ref == Counter(trigrams(lst_seq, pad_symbol=None))

    def test_fourgrams(self):
        # String and list sequences
        str_seq = "A B C D E"
        lst_seq = str_seq.split()

        # Test with padding
        ref = Counter(
            [
                ("$$$", "$$$", "$$$", "A"),
                ("$$$", "$$$", "A", "B"),
                ("$$$", "A", "B", "C"),
                ("A", "B", "C", "D"),
                ("B", "C", "D", "E"),
                ("C", "D", "E", "$$$"),
                ("D", "E", "$$$", "$$$"),
                ("E", "$$$", "$$$", "$$$"),
            ]
        )
        assert ref == Counter(fourgrams(str_seq))
        assert ref == Counter(fourgrams(lst_seq))

        # Test without padding
        ref = Counter([("A", "B", "C", "D"), ("B", "C", "D", "E")])
        assert ref == Counter(fourgrams(str_seq, pad_symbol=None))
        assert ref == Counter(fourgrams(lst_seq, pad_symbol=None))

    def test_get_all_ngrams_by_order(self):
        # String and list sequences
        str_seq = "A B C"
        lst_seq = str_seq.split()

        # Test with no value for `orders`
        ref = Counter(
            [
                ("A",),
                ("B",),
                ("C",),
                ("$$$", "A"),
                ("A", "B"),
                ("B", "C"),
                ("C", "$$$"),
                ("$$$", "$$$", "A"),
                ("$$$", "A", "B"),
                ("A", "B", "C"),
                ("B", "C", "$$$"),
                ("C", "$$$", "$$$"),
            ]
        )
        assert ref == Counter(get_all_ngrams_by_order(str_seq))
        assert ref == Counter(get_all_ngrams_by_order(lst_seq))

        # Test with a list for `orders`
        ref = Counter(
            [
                ("A",),
                ("B",),
                ("C",),
                ("$$$", "$$$", "A"),
                ("$$$", "A", "B"),
                ("A", "B", "C"),
                ("B", "C", "$$$"),
                ("C", "$$$", "$$$"),
            ]
        )
        assert ref == Counter(get_all_ngrams_by_order(str_seq, orders=[1, 3]))
        assert ref == Counter(get_all_ngrams_by_order(lst_seq, orders=[1, 3]))

    def test_get_skipngrams(self):
        # String and list sequences
        str_seq = "A B C D"
        lst_seq = str_seq.split()

        # Test with no gaps and padding
        ref = Counter([("$$$", "A"), ("A", "B"), ("B", "C"), ("C", "D"), ("D", "$$$")])
        assert ref == Counter(get_skipngrams(str_seq, 2, 0))
        assert ref == Counter(get_skipngrams(lst_seq, 2, 0))

        # Test with no gaps and no padding
        ref = Counter([("A", "B"), ("B", "C"), ("C", "D")])
        assert ref == Counter(get_skipngrams(str_seq, 2, 0, pad_symbol=None))
        assert ref == Counter(get_skipngrams(lst_seq, 2, 0, pad_symbol=None))

        # String and list sequences
        str_seq = "A B C D E"
        lst_seq = str_seq.split()

        # Test with gaps and single gap opening
        ref = Counter(
            [
                ("$$$", "$$$", "A"),
                ("$$$", "A", "B"),
                ("A", "B", "C"),
                ("B", "C", "D"),
                ("C", "D", "E"),
                ("D", "E", "$$$"),
                ("E", "$$$", "$$$"),
                ("$$$", "A", "B"),
                ("$$$", "B", "C"),
                ("A", "C", "D"),
                ("B", "D", "E"),
                ("C", "E", "$$$"),
                ("D", "$$$", "$$$"),
                ("$$$", "$$$", "B"),
                ("$$$", "A", "C"),
                ("A", "B", "D"),
                ("B", "C", "E"),
                ("C", "D", "$$$"),
                ("D", "E", "$$$"),
                ("$$$", "B", "C"),
                ("$$$", "C", "D"),
                ("A", "D", "E"),
                ("B", "E", "$$$"),
                ("C", "$$$", "$$$"),
                ("$$$", "$$$", "C"),
                ("$$$", "A", "D"),
                ("A", "B", "E"),
                ("B", "C", "$$$"),
                ("C", "D", "$$$"),
            ]
        )
        assert ref == Counter(get_skipngrams(str_seq, 3, 2))
        assert ref == Counter(get_skipngrams(lst_seq, 3, 2))

        # Test with gaps and multiple gap openings
        ref = Counter(
            [
                ("$$$", "$$$", "A"),
                ("$$$", "$$$", "B"),
                ("$$$", "$$$", "C"),
                ("$$$", "A", "B"),
                ("$$$", "A", "C"),
                ("$$$", "B", "C"),
                ("$$$", "A", "B"),
                ("$$$", "A", "C"),
                ("$$$", "A", "D"),
                ("$$$", "B", "C"),
                ("$$$", "B", "D"),
                ("$$$", "C", "D"),
                ("A", "B", "C"),
                ("A", "B", "D"),
                ("A", "B", "E"),
                ("A", "C", "D"),
                ("A", "C", "E"),
                ("A", "D", "E"),
                ("B", "C", "D"),
                ("B", "C", "E"),
                ("B", "C", "$$$"),
                ("B", "D", "E"),
                ("B", "D", "$$$"),
                ("B", "E", "$$$"),
                ("C", "D", "E"),
                ("C", "D", "$$$"),
                ("C", "D", "$$$"),
                ("C", "E", "$$$"),
                ("C", "E", "$$$"),
                ("C", "$$$", "$$$"),
                ("D", "E", "$$$"),
                ("D", "E", "$$$"),
                ("D", "$$$", "$$$"),
                ("E", "$$$", "$$$"),
            ]
        )
        assert ref == Counter(get_skipngrams(str_seq, 3, 2, single_gap=False))
        assert ref == Counter(get_skipngrams(lst_seq, 3, 2, single_gap=False))

    def test_get_posngrams(self):
        # String and list sequences
        str_seq = "A B C D"
        lst_seq = str_seq.split()

        # Test with zero left and zero right length
        ref = Counter(
            [
                (("###",), "A", 0),
                (("###",), "B", 1),
                (("###",), "C", 2),
                (("###",), "D", 3),
            ]
        )
        assert ref == Counter(get_posngrams(str_seq, 0, 0))
        assert ref == Counter(get_posngrams(lst_seq, 0, 0))

        # Test with non-zero left and zero right length
        ref = Counter(
            [
                (("$$$", "$$$", "###"), "A", 0),
                (("$$$", "A", "###"), "B", 1),
                (("A", "B", "###"), "C", 2),
                (("B", "C", "###"), "D", 3),
            ]
        )
        assert ref == Counter(get_posngrams(str_seq, 2, 0))
        assert ref == Counter(get_posngrams(lst_seq, 2, 0))

        # Test with zero left and non-zero right length
        ref = Counter(
            [
                (("###", "B", "C"), "A", 0),
                (("###", "C", "D"), "B", 1),
                (("###", "D", "$$$"), "C", 2),
                (("###", "$$$", "$$$"), "D", 3),
            ]
        )
        assert ref == Counter(get_posngrams(str_seq, 0, 2))
        assert ref == Counter(get_posngrams(lst_seq, 0, 2))

        # Test with non-zero left and non-zero right length
        ref = Counter(
            [
                (("$$$", "$$$", "###", "B", "C"), "A", 0),
                (("$$$", "A", "###", "C", "D"), "B", 1),
                (("A", "B", "###", "D", "$$$"), "C", 2),
                (("B", "C", "###", "$$$", "$$$"), "D", 3),
            ]
        )
        assert ref == Counter(get_posngrams(str_seq, 2, 2))
        assert ref == Counter(get_posngrams(lst_seq, 2, 2))

    def test_get_all_posngrams(self):
        # String and list sequences
        str_seq = "A B C"
        lst_seq = str_seq.split()

        # Test with ints as orders
        ref = Counter(
            [
                (("###",), "A", 0),
                (("###",), "B", 1),
                (("###",), "C", 2),
                (("###", "B"), "A", 0),
                (("###", "C"), "B", 1),
                (("###", "$$$"), "C", 2),
                (("$$$", "###"), "A", 0),
                (("A", "###"), "B", 1),
                (("B", "###"), "C", 2),
                (("$$$", "###", "B"), "A", 0),
                (("A", "###", "C"), "B", 1),
                (("B", "###", "$$$"), "C", 2),
                (("$$$", "$$$", "###"), "A", 0),
                (("$$$", "A", "###"), "B", 1),
                (("A", "B", "###"), "C", 2),
                (("$$$", "$$$", "###", "B"), "A", 0),
                (("$$$", "A", "###", "C"), "B", 1),
                (("A", "B", "###", "$$$"), "C", 2),
            ]
        )
        assert ref == Counter(get_all_posngrams(str_seq, 2, 1))
        assert ref == Counter(get_all_posngrams(lst_seq, 2, 1))

        # String and list sequences
        str_seq = "A B C D"
        lst_seq = str_seq.split()

        # Test with lists as orders
        ref = Counter(
            [
                (("$$$", "$$$", "###", "B"), "A", 0),
                (("$$$", "A", "###", "C"), "B", 1),
                (("A", "B", "###", "D"), "C", 2),
                (("B", "C", "###", "$$$"), "D", 3),
                (("$$$", "$$$", "$$$", "###", "B"), "A", 0),
                (("$$$", "$$$", "A", "###", "C"), "B", 1),
                (("$$$", "A", "B", "###", "D"), "C", 2),
                (("A", "B", "C", "###", "$$$"), "D", 3),
            ]
        )
        assert ref == Counter(get_all_posngrams(str_seq, [2, 3], [1]))
        assert ref == Counter(get_all_posngrams(lst_seq, [2, 3], [1]))

    def test_ngram_class(self):
        # A bunch of random words for testing
        words = [
            "adamant",
            "aplastic",
            "asperges",
            "benthamic",
            "bridoon",
            "contraband",
            "dilatableness",
            "help",
            "helper",
            "helpful",
            "hieronymic",
            "hydrogeological",
            "insetting",
            "integrating",
            "lirellate",
            "metempirically",
            "misguided",
            "mononuclear",
            "praiseworthiness",
            "sarcocarp",
            "springlet",
            "ungambling",
            "wilco",
        ]

        # Build an empty ngram model.
        NgramModel()

        # Build a simple ngram model, than train it with different paramenters.
        model = NgramModel(2, 1, sequences=words)

        # Assert that an error will be raised if we try to score a sequence
        # before training the model.
        self.assertRaises(AssertionError, model.score, random.sample(words, 1)[0])

        # Run different trainings.
        model.train()
        model.train(method="lidstone", gamma=0.1)
        model.train(method="certaintydegree", set_min=True)
        model.train(normalize=True)

        # Compute the relative likelihood for a random sample of `words`, both
        # using and not using length probability.
        # This will internally call the `.state_score()` method.
        [model.score(word, use_length=True) for word in random.sample(words, 3)]
        [model.score(word, use_length=False) for word in random.sample(words, 3)]

        # Assert that the score of a word when using length probability will be
        # lower than when not using it.
        rnd_word = random.sample(words, 1)[0]
        assert model.score(rnd_word, use_length=True) < model.score(
            rnd_word, use_length=False
        )

        # Score a random sequence of printable characters (which might,
        # however, not be handled by the installed fonts) and observed characters.
        # The sequence is shuffled in place for even higher randomness, so we
        # are sure to get a sequence of relative low likelihood, which we
        # assert by comparing with the score of some sequence drawn from the
        # training set. This complex random sequence should guarantee full
        # coverage of the fall-backs and defaults when computing a sequence score.
        rnd_seq = random.sample(string.printable, 7)
        rnd_seq += random.sample(words, 1)[0]
        random.shuffle(rnd_seq)
        # assert model.score(rnd_seq) < model.score(random.sample(words, 1)[0])

        # Get the model entropy.
        model.model_entropy()

        # Compute the perplexity for a number of sequences in the training set.
        # This will internally call `.entropy()`.
        assert model.perplexity(random.sample(words, 3))

        # Generate a bunch of random words with different parameters, to guarantee
        # full coverage.
        model.random_seqs(k=15)
        model.random_seqs(k=15, only_longest=True)

        # Generate a bunch of random words with different length parameters.
        model.random_seqs(k=15)
        model.random_seqs(k=15, seq_len=5)
        model.random_seqs(k=15, seq_len=(3, 4, 5, 6))

    def test_all_ngrams(self):
        assert get_all_ngrams("lingpy")[0] == "lingpy"


class TestSmoothing(unittest.TestCase):
    def setUp(self):
        # Set up a bunch of fake distribution to test the methods.
        # We don't use real data as this is only intended to test
        # the programming side, and we don't want to distribute a
        # datafile only for this testing purposes. We setup a simple
        # distribution with character from A to E, and a far more
        # complex one (which includes almost all printable characters
        # as single states, plus a combination of letters and characters,
        # all with a randomly generated frequency)
        self.observ1 = Counter([char for char in "ABBCCCDDDDEEEE"])

        samples = [
            char
            for char in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;?@[\\]^_`{|}~"
        ]
        two_char_samples = [
            [char1 + char2 for char2 in "0123456789"] for char1 in "ABCDEFGHIJK"
        ]
        samples += itertools.chain.from_iterable(two_char_samples)

        random.seed(1305)
        self.observ2 = {
            sample: (random.randint(1, 1000) ** random.randint(1, 3))
            + random.randint(1, 100)
            for sample in samples
        }
        self.observ2["x"] = 100
        self.observ2["y"] = 100
        self.observ2["z"] = 1000

    def test_uniform_dist(self):
        """
        Test for the uniform distribution.
        """

        # Easiest distribution to test: everything must be equal, unobserved
        # must be less than any observed one.
        seen, unseen = smooth_dist(self.observ1, "uniform")
        assert seen["A"] == seen["E"]
        assert seen["A"] > unseen

        seen, unseen = smooth_dist(self.observ2, "uniform")
        assert seen["0"] == seen["~"]
        assert seen["x"] == seen["z"]
        assert seen["0"] > unseen

    def test_random_dist(self):
        """
        Test for the random distribution.
        """

        # Here, we can essentially only test if there are no execution bugs,
        # besides the unobserved probability being less than any other. Nonetheless,
        # we set a seed for comparing the results across platforms.
        seen, unseen = smooth_dist(self.observ1, "random", seed=1305)
        assert seen["A"] < seen["E"]
        assert seen["B"] < seen["D"]
        assert seen["A"] < seen["C"]
        assert seen["A"] > unseen

        seen, unseen = smooth_dist(self.observ2, "random", seed=1305)
        assert seen["B1"] < seen["4"]
        assert seen["F5"] < seen["C8"]
        assert seen["0"] > unseen

    def test_mle_dist(self):
        """
        Test for the Maximum-Likelihood Estimation distribution.
        """

        # This is easy to test as the results of the MLE are the ones we intuitively
        # expect/compute.
        seen, unseen = smooth_dist(self.observ1, "mle")
        assert seen["A"] < seen["B"]
        assert seen["D"] == seen["E"]
        assert seen["A"] > unseen

        seen, unseen = smooth_dist(self.observ2, "mle")
        assert seen["x"] == seen["y"]
        assert seen["x"] < seen["z"]
        assert seen["0"] > unseen

    def test_laplace_dist(self):
        """
        Test for the Laplace distribution.
        """

        seen, unseen = smooth_dist(self.observ1, "laplace")
        assert seen["A"] < seen["B"]
        assert seen["D"] == seen["E"]
        assert seen["A"] > unseen

        seen, unseen = smooth_dist(self.observ2, "laplace")
        assert seen["x"] == seen["y"]
        assert seen["x"] < seen["z"]
        assert seen["0"] > unseen

    def test_ele_dist(self):
        """
        Test for the Expected-Likelihood estimation distribution.
        """

        seen, unseen = smooth_dist(self.observ1, "ele")
        assert seen["A"] < seen["B"]
        assert seen["D"] == seen["E"]
        assert seen["A"] > unseen

        seen, unseen = smooth_dist(self.observ2, "ele")
        assert seen["x"] == seen["y"]
        assert seen["x"] < seen["z"]
        assert seen["0"] > unseen

    def test_wittenbell_dist(self):
        """
        Test for the Witten-Bell distribution.
        """

        seen10, unseen10 = smooth_dist(self.observ1, "wittenbell", bins=10)
        seen99, unseen99 = smooth_dist(self.observ1, "wittenbell", bins=99)
        assert seen10["A"] < seen10["B"]
        assert seen10["D"] == seen10["E"]
        assert seen10["A"] == unseen10
        assert seen10["A"] == seen99["A"]
        assert unseen99 < unseen10

        seen, unseen = smooth_dist(self.observ2, "wittenbell")
        assert seen["x"] == seen["y"]
        assert seen["x"] < seen["z"]
        assert seen["0"] > unseen

    def test_certaintydegree_dist(self):
        """
        Test for the Degree of Certainty distribution.
        """

        seen, unseen = smooth_dist(self.observ1, "certaintydegree")
        seen99, unseen99 = smooth_dist(self.observ1, "certaintydegree", bins=99)
        assert seen["A"] < seen["B"]
        assert seen["D"] == seen["E"]
        assert seen["A"] < unseen
        assert seen["B"] > unseen
        assert seen["A"] < seen99["A"]
        assert unseen > unseen99

        seen, unseen = smooth_dist(self.observ2, "certaintydegree")
        assert seen["x"] == seen["y"]
        assert seen["x"] < seen["z"]
        assert seen["0"] > unseen

    def test_sgt_dist(self):
        """
        Test for the Simple Good-Turing distribution.
        """

        # Only run the test if the numpy and scipy libraries (imported
        # by the function) are installed; an ImportError will not be a
        # test failure as we decided that they should not be dependencies.

        try:
            # The first distribution does not have enough data for SGT,
            # assert that an assertion is raised.
            self.assertRaises(RuntimeWarning, smooth_dist, self.observ1, "sgt")

            # The second distribution also does not have enough data for
            # a confident results, but it does have enough to stress-test the
            # method, so we are not going to allow it to fail (i.e., raise
            # exceptions)
            seen_p05, unseen_p05 = smooth_dist(self.observ2, "sgt", allow_fail=False)
            assert seen_p05["x"] == seen_p05["y"]
            assert seen_p05["x"] < seen_p05["z"]
            assert seen_p05["0"] > unseen_p05
        except ImportError:
            pass


if __name__ == "__main__":
    # Explicitly creating and running a test suite allows to profile it
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLPNgram)
    unittest.TextTestRunner(verbosity=2).run(suite)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestSmoothing)
    unittest.TextTestRunner(verbosity=2).run(suite)
