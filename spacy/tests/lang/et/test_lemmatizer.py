# coding: utf-8
from __future__ import unicode_literals

import pytest

# from ....tokens.doc import Doc
from spacy.tokens.doc import Doc


@pytest.fixture
def et_lemmatizer(ET):
    return ET.Defaults.create_lemmatizer()


@pytest.mark.models('et')
def test_doc_lemmatization(ET):
    doc = Doc(ET.vocab, words=['karu'])
    doc[0].tag_ = 'NOUN'
    assert doc[0].lemma_ == 'karu'


@pytest.mark.models('et')
@pytest.mark.parametrize('text, lemmas', [("inimestega", ["inimene"]),
                                          ("noaga", ["nuga"]),
                                          ("kõhust", ["kõht"]),
                                          ("kasse", ["kass"])])
def test_et_lemmatizer_noun_lemmas(et_lemmatizer, text, lemmas):
    assert et_lemmatizer.noun(text) == lemmas


@pytest.mark.models('et')
@pytest.mark.parametrize('text, lemmas', [("ilusama", ["ilusam"]),
                                          ("punastega", ["punane"]),
                                          ("pikima", ["pikim"])])
def test_et_lemmatizer_adj_lemmas(et_lemmatizer, text, lemmas):
    assert et_lemmatizer.adj(text) == lemmas


@pytest.mark.models('et')
@pytest.mark.parametrize('text, lemmas', [("nägi", ["nägema"]),
                                          ("loeks", ["lugema"])])
def test_et_lemmatizer_verb_lemmas(et_lemmatizer, text, lemmas):
    assert et_lemmatizer.verb(text) == lemmas


@pytest.mark.models('et')
@pytest.mark.parametrize('text, lemmas', [("loetavad", ["loetav"])])
def test_et_lemmatizer_adj_lemmas(et_lemmatizer, text, lemmas):
    assert et_lemmatizer.adj(text) == lemmas


@pytest.mark.models('et')
@pytest.mark.parametrize('text, tag, lemmas', [["Tartusse", "propn", ["tartu"]],
                                               ["majja", "noun", ["maja"]]])
def test_et_lemmatizer_lemmas(et_lemmatizer, text, tag, lemmas):
    assert et_lemmatizer(text, tag) == lemmas


@pytest.mark.models('et')
@pytest.mark.parametrize('text, tag, morphology, lemmas', [["teist", "num", {"NumType": "Ord"}, ["teine"]],
                                                           ["suurimaga", "adj", {"Degree": "Sup"}, ["suurim"]],
                                                           ["USA", "noun", {"Abbr": "Yes"}, ["usa"]]])
def test_et_lemmatizer_lemmas_with_morphology(et_lemmatizer, text, tag, morphology, lemmas):
    assert et_lemmatizer(text, tag, morphology) == lemmas
