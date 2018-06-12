from unittest import TestCase

import infotheory

class TestShannonEntropy(TestCase):
    def test_shannon_entropy(self):
        self.assertTrue(infotheory.shannon_entropy([1, 1, 1, 1]) == 0.0)
        self.assertTrue(infotheory.shannon_entropy([1, 2, 3, 4]) == 2.0)
        self.assertTrue(infotheory.shannon_entropy([1, 1, 3, 4]) == 1.5)

