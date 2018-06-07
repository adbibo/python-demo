#!/usr/bin/env python
# -*- coding=utf-8 -*-
import xlrd

import sys

reload(sys)
sys.setdefaultencoding('utf8')


class ExcelReader(object):
    __slots__ = ['_fields', '_content']

    def __init__(self, excel_name, index_of_sheet):
        excel = xlrd.open_workbook(excel_name)
        table = excel.sheet_by_index(index_of_sheet)
        self._fields = table.row_values(0)
        self._content = [[self.get_item_value(table.cell(r, c)) for c in range(table.ncols)] for r in
                         range(1, table.nrows)]

    @staticmethod
    def get_item_value(item):
        # type =  0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
        item_type = item.ctype

        if item_type in [1, 3]:
            return str(item.value)

        elif item_type == 2:
            return int(item.value)
        elif item_type == 4:
            return bool(item.value)
        else:
            return 0

    def get_fields(self):
        return self._fields

    def get_row_list(self):
        return self._content
