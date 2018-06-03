# coding: utf-8
"""Test that tokenizer exceptions are parsed correctly."""

from __future__ import unicode_literals

import pytest


@pytest.mark.parametrize('text, norms', [("E", ["esmaspäev"]),
                                         ("R.", ["reede"]),
                                         ("dets.", ["detsember"]),
                                         ("nn", ["niinimetatud"]),
                                         ("nn.", ["niinimetatud"])])
def test_et_tokenizer_abbrev_exceptions(et_tokenizer, text, norms):
    tokens = et_tokenizer(text)
    assert len(tokens) == len(norms)
    assert [token.norm_ for token in tokens] == norms
