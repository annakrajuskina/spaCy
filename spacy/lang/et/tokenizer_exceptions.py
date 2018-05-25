# coding: utf8
from __future__ import unicode_literals

from ...symbols import ORTH, LEMMA, NORM

_exc = {}
_abbrev_exc = [

    # http://www.eki.ee/itstandard/2000/FDCC.shtml
    # Weekdays abbreviations
    {ORTH: "E", LEMMA: "esmaspäev", NORM: "esmaspäev"},
    {ORTH: "T", LEMMA: "teisipäev", NORM: "teisipäev"},
    {ORTH: "K", LEMMA: "kolmapäev", NORM: "kolmapäev"},
    {ORTH: "N", LEMMA: "neljapäev", NORM: "neljapäev"},
    {ORTH: "R", LEMMA: "reede", NORM: "reede"},
    {ORTH: "L", LEMMA: "laupäev", NORM: "laupäev"},
    {ORTH: "P", LEMMA: "pühapäev", NORM: "pühapäev"},

    # Months abbreviations
    {ORTH: "jaan", LEMMA: "jaanuar", NORM: "jaanuar"},
    {ORTH: "veebr", LEMMA: "veebruar", NORM: "veebruar"},
    {ORTH: "märts", LEMMA: "märts", NORM: "märts"},
    {ORTH: "mär", LEMMA: "märts", NORM: "märts"},
    {ORTH: "apr", LEMMA: "aprill", NORM: "aprill"},
    {ORTH: "mai", LEMMA: "mai", NORM: "mai"},
    {ORTH: "juuni", LEMMA: "juuni", NORM: "juuni"},
    {ORTH: "juun", LEMMA: "juuni", NORM: "juuni"},
    {ORTH: "juuli", LEMMA: "juuli", NORM: "juuli"},
    {ORTH: "juul", LEMMA: "juuli", NORM: "juuli"},
    {ORTH: "aug", LEMMA: "august", NORM: "august"},
    {ORTH: "augu", LEMMA: "august", NORM: "august"},
    {ORTH: "sept", LEMMA: "september", NORM: "september"},
    {ORTH: "septe", LEMMA: "september", NORM: "september"},
    {ORTH: "okt", LEMMA: "oktoober", NORM: "oktoober"},
    {ORTH: "okto", LEMMA: "oktoober", NORM: "oktoober"},
    {ORTH: "nov", LEMMA: "november", NORM: "november"},
    {ORTH: "nove", LEMMA: "november", NORM: "november"},
    {ORTH: "dets", LEMMA: "detsember", NORM: "detsember"},
    {ORTH: "detse", LEMMA: "detsember", NORM: "detsember"},
]

for abbrev_desc in _abbrev_exc:
    abbrev = abbrev_desc[ORTH]
    for orth in (abbrev, abbrev.capitalize(), abbrev.upper()):
        _exc[orth] = [{ORTH: orth, LEMMA: abbrev_desc[LEMMA], NORM: abbrev_desc[NORM]}]
        _exc[orth + '.'] = [{ORTH: orth + '.', LEMMA: abbrev_desc[LEMMA], NORM: abbrev_desc[NORM]}]

TOKENIZER_EXCEPTIONS = _exc
