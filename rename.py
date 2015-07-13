#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import os, re, shutil


def name_mapping(filenames):
    PATTERN = 'M6UTT5U0I_([0-9]+)_([0-9]+)_.+?\.srt'
    for name in filenames:
        match_obj = re.match(PATTERN, name)
        if match_obj:
            new_name = 'lecture-{0}({1}).srt'.format(
                match_obj.group(1),
                'zh-cn' if match_obj.group(2) == '1' else 'en',
            )
            yield name, new_name



def main():
    filenames = os.listdir(os.getcwd())
    for src, dst in name_mapping(filenames):
        shutil.move(src, dst)


if __name__ == '__main__':
    main()
