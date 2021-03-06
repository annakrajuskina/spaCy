# coding: utf8
from __future__ import unicode_literals

from .lemmatizer import EstonianLemmatizer
from .lemmatizer.lookup import LOOKUP
from .lex_attrs import LEX_ATTRS
from .stop_words import STOP_WORDS
from .tokenizer_exceptions import TOKENIZER_EXCEPTIONS
from ..norm_exceptions import BASE_NORMS
from ..tokenizer_exceptions import BASE_EXCEPTIONS
from ...attrs import LANG, NORM
from ...language import Language
from ...util import update_exc, add_lookups


class EstonianDefaults(Language.Defaults):
    lex_attr_getters = dict(Language.Defaults.lex_attr_getters)
    lex_attr_getters[LANG] = lambda text: 'et'
    lex_attr_getters[NORM] = add_lookups(Language.Defaults.lex_attr_getters[NORM], BASE_NORMS)

    lex_attr_getters.update(LEX_ATTRS)

    tokenizer_exceptions = update_exc(BASE_EXCEPTIONS, TOKENIZER_EXCEPTIONS)

    stop_words = STOP_WORDS

    @classmethod
    def create_lemmatizer(cls, nlp=None):
        return EstonianLemmatizer(LOOKUP)


class Estonian(Language):
    lang = 'et'
    Defaults = EstonianDefaults


__all__ = ['Estonian']
