# coding: utf8
from __future__ import unicode_literals

import bz2
import os
from collections import defaultdict

# https://raw.githubusercontent.com/michmech/lemmatization-lists/master/lemmatization-et.txt
fnm = os.path.join(os.path.curdir(), 'dict.bz2')
lemmas = defaultdict(list)
with bz2.BZ2File(fnm) as inf:
    for ln in inf:
        infl, lem = ln.decode('utf8').rstrip().split("\t", 1)
        lemmas[infl].append(lem[0])

LOOKUP = lemmas
