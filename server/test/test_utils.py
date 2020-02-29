# -*- coding: utf-8 -*-
# Copyright 2020, Duke Institute for Health Innovation (DIHI), Duke University School of Medicine, Durham NC. All Rights Reserved.

import pytest
import gettext
import polib

from app.utils import getstr


def test_getstr_install():
    el = gettext.translation('base', localedir='locales', languages=['en'])
    el.install()


def test_getstr():
    el = gettext.translation('base', localedir='locales', languages=['en'])
    el.install()
    _ = el.gettext

    assert _('test-msgid-do-not-delete') == 'hello world'
    assert _('value that does not exist') == 'value that does not exist'  # included for clarity

    assert getstr('test-msgid-do-not-delete') == _('test-msgid-do-not-delete')
    assert getstr('value that does not exist') == _('value that does not exist')


def test_strings_complete():
    po = polib.pofile('locales/en/LC_MESSAGES/base.po')
    assert po.percent_translated() == 100


