# coding: utf8
from __future__ import unicode_literals

from copy import deepcopy

from ....lemmatizer import Lemmatizer
from ....symbols import POS, ADV, NOUN, ADP, PRON, SCONJ, PROPN, DET, SYM, INTJ
from ....symbols import PUNCT, NUM, AUX, X, CONJ, ADJ, VERB, PART, SPACE, CCONJ


class EstonianLemmatizer(Lemmatizer):
    # https://github.com/Filosoft/vabamorf

    symbol_to_str_map = {
        POS: "pos",
        NOUN: "noun",
        VERB: "verb",
        ADJ: "adj",
        ADV: "adv",
        NUM: "num",
        CONJ: "conj",
        PUNCT: "punct",
        ADP: "adp",
        PRON: "pron",
        SCONJ: "sconj",
        CCONJ: "cconj",
        PROPN: "propn",
        DET: "det",
        SYM: "sym",
        INTJ: "intj",
        AUX: "aux",
        X: "x",
        PART: "part",
        SPACE: "space"
    }
    morf_attrs_map = {
        "pos": {
            "verb": ["v"],
            "noun": ["s"],
            "punct": ["z"],
            "propn": ["h"],
            "conj": ["j"],
            "cconj": ["j"],
            "sconj": ["j"],
            "pron": ["p"],
            "intj": ["i"],
            "adv": ["d"],
            "adp": ["k"],
            "adj": ["a", "c", "u", "g"],
            "num": ["n", "o"]
        },
        "numtype": {
            "card": ["n"],
            "ord": ["o"]
        },
        "degree": {
            "cmp": ["c"],
            "pos": ["a", "d"],
            "sup": ["u"]
        },
        "abbr": {
            "yes": ["y"]
        },
        "number": {
            "sing": "sg",
            "plur": "pl"
        },
        "case": {
            "abe": "ab",
            "abl": "abl",
            "ade": "ad",
            "add": "adt",
            "all": "all",
            "ela": "el",
            "ess": "es",
            "gem": "g",
            "ill": "ill",
            "ine": "in",
            "com": "kom",
            "nom": "n",
            "par": "p",
            "ter": "ter",
            "tra": "tr"
        },
        "neg": "neg"
    }

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
        univ_pos = self.univ_pos_to_str(univ_pos)
        pos_tags, form_filters = self.compute_vabamorf_tags_and_form_filters(univ_pos, morphology)
        result = analyze(string)
        analysis_list = result[0]['analysis']
        return self.filter_lemmas(analysis_list, pos_tags, form_filters)

    def univ_pos_to_str(self, univ_pos):
        if isinstance(univ_pos, str):
            return univ_pos.lower()
        return self.symbol_to_str_map[univ_pos]

    def compute_vabamorf_tags_and_form_filters(self, univ_pos, morphology=None):
        if morphology is None:
            return self.morf_attrs_map['pos'].get(univ_pos, []), []
        if POS in morphology.keys():
            pos = self.symbol_to_str_map.get(morphology.pop(POS), "")
            morphology.update({"pos": pos})
        morphology = dict((key.lower(), value.lower()) for key, value in morphology.items())
        morph_attrs = set(morphology.keys())
        if "abbr" in morph_attrs:
            return self.morf_attrs_map['abbr'].get('yes', []), []
        if "numtype" in morph_attrs:
            return self.morf_attrs_map['numtype'].get(morphology.get('numtype', [])), []
        if "degree" in morph_attrs:
            return self.morf_attrs_map['degree'].get(morphology.get('degree', [])), []
        if "pos" not in morph_attrs or morphology.get("pos", "") != univ_pos:
            return self.morf_attrs_map['pos'].get(univ_pos, []), []
        pos_tags = self.morf_attrs_map['pos'].get(univ_pos, [])
        form_filters = []
        morph_attrs.remove('pos')
        for attr in morph_attrs:
            attr_val = morphology.get(attr).lower()
            attr_possible_vals = self.morf_attrs_map.get(attr, {})
            form_filter = attr_possible_vals.get(attr_val, [])
            form_filters += form_filter
        return pos_tags, form_filters

    @staticmethod
    def filter_lemmas(analysis_list, pos_tags, form_filters):
        analysis_list_initial = deepcopy(analysis_list)
        if len(pos_tags) > 0:
            analysis_list = [analysis for analysis in analysis_list if analysis['partofspeech'].lower() in pos_tags]
        if len(form_filters) > 0:
            for form_filter in form_filters:
                analysis_list = [analysis for analysis in analysis_list if form_filter in analysis['form'].lower()]
        if len(analysis_list) == 0:
            analysis_list = analysis_list_initial
        return list(set([analysis['lemma'].lower() for analysis in analysis_list]))
