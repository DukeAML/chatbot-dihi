# -*- coding: utf-8 -*-
# Copyright 2019, Duke Institute for Health Innovation (DIHI), Duke University School of Medicine, Durham NC. All Rights Reserved.

import polib
import logging

""" Generates the .mo file from the project's .po file.
"""

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    po = polib.pofile('locales/en/LC_MESSAGES/base.po')
    if po.percent_translated() == 100:
        logging.info(f'strings are {po.percent_translated()}% complete.')
    else:
        logging.error(f'strings are {po.percent_translated()}% complete.')
    po.save_as_mofile('locales/en/LC_MESSAGES/base.mo')
    logging.info('Updated binary language files.')
