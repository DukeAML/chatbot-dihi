# -*- coding: utf-8 -*-
# Copyright 2019, Duke Institute for Health Innovation (DIHI), Duke University School of Medicine, Durham NC. All Rights Reserved.

from app import app
import functools
import gettext
import time
from typing import Any, List

_el = gettext.translation('base', localedir='locales', languages=['en'])
_el.install()

getstr = _el.gettext
""" Wraps `gettext.gettext`.
"""

def timefunc(f):  # pragma: no cover
    """ Provides an annotation for timing the duration of a function.
    """
    @functools.wraps(f)
    def f_timer(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        app.logger.info(f'⏱  Timing: {f.__module__}:{f.__name__} took {(end - start):.4f}s')
        return result
    return f_timer
