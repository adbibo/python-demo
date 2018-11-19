#!/usr/bin/env python
# encoding: utf-8

# @author: adbibo
# @contact: laoliu.yin@gmail.com
# @file: properties.py
# @time: 2018/7/5 下午2:10
# @desc:

from decimal import Decimal


########################################################################
class Fees(object):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self._fee = None

    # ----------------------------------------------------------------------
    def get_fee(self):
        """
        Return the current fee
        """
        return self._fee

    # ----------------------------------------------------------------------
    def set_fee(self, value):
        """
        Set the fee
        """
        if isinstance(value, str):
            self._fee = Decimal(value)
        elif isinstance(value, Decimal):
            self._fee = value
        elif isinstance(value, int):
            self._fee = value

    fexx = property(get_fee, set_fee)

    @property
    def fee(self):
        return self._fee

    @fee.setter
    def fee(self, value):
        """
        The setter of the fee property
        """
        if isinstance(value, str):
            self._fee = Decimal(value)
        elif isinstance(value, Decimal):
            self._fee = value
        elif isinstance(value, int):
            self._fee = value

            
if __name__ == '__main__':
    f = Fees()
    f.set_fee(Decimal(1.0))
    print(f.fexx)
