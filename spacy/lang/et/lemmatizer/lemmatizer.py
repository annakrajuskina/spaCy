# coding: utf8
from __future__ import unicode_literals

from spacy.lang.et.lemmatizer.lookup import LOOKUP
from ...lemmatizer import Lemmatizer


class EstonianLemmatizer(Lemmatizer):
    def __init__(self):
        super(EstonianLemmatizer, self).__init__(lookup=LOOKUP)

    def __call__(self, string, univ_pos, morphology=None):
        if LOOKUP is not None and string in LOOKUP.keys():
            return LOOKUP[string]
        try:
            from pyvabamorf import analyze
        except ImportError:
            raise ImportError(
                'Estonian lemmatizer requires pyvabamorf library. Try to fix it with "pip install pyvabamorf"')
        result = analyze(string)
        analysis_list = result[0]['analysis']
        return list(set([analysis['lemma'] for analysis in analysis_list]))
