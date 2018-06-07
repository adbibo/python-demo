#!/usr/bin/env python
# -*- coding=utf-8 -*-

from decimal import Decimal


def div(divsor, dividend, digits=4):
    if dividend == 0:
        return 0
    else:
        return round(Decimal(divsor) / Decimal(dividend), digits)
