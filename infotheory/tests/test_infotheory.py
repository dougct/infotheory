from unittest import TestCase

import infotheory

class TestShannonEntropy(TestCase):
    def test_shannon_entropy(self):
        result = infotheory.entropy([1, 1, 1, 1])
        self.assertTrue(result == 0.0)

