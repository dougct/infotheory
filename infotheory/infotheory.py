# -*- coding: utf8 -*-

import math
import pandas as pd
import numpy as np
import scipy.stats
from collections import defaultdict


def shannon_entropy(labels, base=2):
    """ Computes entropy of label distribution. """
    n_labels = len(labels)
    if n_labels <= 1:
        return 0

    value, counts = np.unique(labels, return_counts=True)
    probs = counts / n_labels
    n_classes = np.count_nonzero(probs)

    if n_classes <= 1:
        return 0

    ent = 0.

    # Compute entropy
    base = e if base is None else base
    for i in probs:
        ent -= i * math.log(i, base)

    return ent



# Input a pandas series 
def scipy_entropy(data, base=2):
    # Calculate the probabilities.
    p_data = data.value_counts() / len(data)
    # Input probabilities to get the entropy.
    return scipy.stats.entropy(p_data, base=base)



def binary_entropy(nr_labels, nr_target_labels, base=2):
    p = nr_target_labels / nr_labels
    if p == 1.0 or p == 0.0:
        return 0.0
    return -p * math.log(p, base) - (1 - p) * math.log(1 - p, base)



def lzw_encode(symbols):
    """Compress a string to a list of output symbols."""
 
    # Build the dictionary.
    dictionary = {c:i for i, c in enumerate(set(symbols))}
    dict_size = len(dictionary)
    
    w = ""
    result = []
    seq_sizes = []
    for c in symbols:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            seq_sizes.append(len(w))
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    # Output the code for w.
    if w:
        seq_sizes.append(len(w))
        result.append(dictionary[w])
    
    return result, seq_sizes



def lzw_entropy(labels):
    _, seq_sizes = lzw_encode(labels)
    return (1 / (sum(seq_sizes) / len(seq_sizes))) * math.log(len(seq_sizes))



def compute_pi_fano(S, N):
    if S == 0.0 or N <= 1:
        return 1.0
    for p in np.arange(0.001, 1.000, 0.001):
        h = -p * math.log2(p) - (1 - p) * math.log2(1 - p)
        pi_fano = h + (1 - p) * math.log2(N - 1) - S
        if pi_fano <= 0.001:
            return p
    return 0.0


