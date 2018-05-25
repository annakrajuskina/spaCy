# coding: utf8
from __future__ import unicode_literals

from ...lemmatizer import Lemmatizer


class EstonianLemmatizer(Lemmatizer):
    def __init__(self, LOOKUP):
        super(EstonianLemmatizer, self).__init__()
        self.lookup_table = LOOKUP

    def __call__(self, string, univ_pos, morphology=None):
        if self.lookup_table is not None and string in self.lookup_table.keys():
            return self.lookup_table[string]
        try:
            from pyvabamorf import analyze
        except ImportError:
            raise ImportError(
                'Estonian lemmatizer requires pyvabamorf library. Try to fix it with "pip install pyvabamorf"')
        result = analyze(string)
        analysis_list = result[0]['analysis']
        return list(set([analysis['lemma'].lower() for analysis in analysis_list]))
