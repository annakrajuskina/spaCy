# coding: utf8
from __future__ import unicode_literals

from ...attrs import LIKE_NUM

_num_words = ['null', 'üks', 'kaks', 'kolm', 'neli', 'viis', 'kuus', 'seitse', 'kaheksa', 'üheksa', 'kümme',
              'üksteist', 'kaksteist', 'kolmteist', 'neliteist', 'viisteist', 'kuusteist', 'seitseteist',
              'kaheksateist', 'üheksateist', 'kakskümmend', 'kolmkümmend', 'nelikümmend', 'viiskümmend',
              'kuuskümmend', 'seitsekümmend', 'kaheksakümmend', 'üheksakümmend',
              'sada', 'tuhat', 'miljon', 'miljard', 'triljon', 'kvadriljon']


def like_num(text):
    text = text.replace(',', '').replace('.', '')
    if text.isdigit():
        return True
    if text.count('/') == 1:
        num, denom = text.split('/')
        if num.isdigit() and denom.isdigit():
            return True
    if text.lower() in _num_words:
        return True
    return False


LEX_ATTRS = {
    LIKE_NUM: like_num
}
