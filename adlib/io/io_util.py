#!/usr/bin/env python
# -*- coding=utf-8 -*-

import copy
import hashlib
import json
import os
import re
import time
from datetime import date, datetime

from django.utils.crypto import get_random_string


# 修改文件名
def change_file_name(file_):
    if not file_:
        return file_
    pattern = re.compile(r'^[\w\d/.]+$')
    if pattern.match(file_.name):
        return file_
    name, ext = os.path.splitext(file_.name)
    path_ = os.path.dirname(file_.name)
    new_name = hashlib.md5('{0}{1}'.format(get_random_string(), time.time())).hexdigest()
    new_name = '%s%s' % (new_name, ext.lower())
    file_.name = os.path.join(path_, new_name)
    return file_


def to_dict(model):
    def not_item(item):
        if not str(item).startswith('_'):
            return item

    items = filter(not_item, model.__class__.__dict__.keys())
    return dict([(attr, getattr(model, attr)) for attr in items])





def file_iterator(file_name, chunk_size=512):
    with open(file_name) as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break
