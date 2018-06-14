#!/usr/bin/env python
# -*- coding=utf-8 -*-

from datetime import datetime

import xlwt


def set_style(name, height, bold=False):
    style = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体
    font.name = name  # 'Times New Roman'
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style


def write_row(sheet_, rowBegin, rowEnd, col, data):
    sheet_.write_merge(rowBegin, rowEnd, col, col, data, set_style('Times New Roman', 220, True))
    # width = sheet_.col(col).width
    # fact_width = len(data) if isinstance(data, str) else 32
    # if width < fact_width * 367:
    #     sheet_.col(col).width = fact_width * 260


def writer_row(sheet_, row_begin, row_end, row, field_list):
    for index in range(len(field_list)):
        record = str(row[field_list[index]]) if isinstance(row[field_list[index]], datetime) else row[field_list[index]]
        write_row(sheet_, row_begin, row_end, index, record)


def write_excel(result_list, field_list, sheet_name, first_row):
    excel_stream = xlwt.Workbook(encoding='utf-8', style_compression=2)
    sheet1 = excel_stream.add_sheet(sheet_name, cell_overwrite_ok=True)
    row = 0

    for i in range(0, len(first_row)):
        sheet1.write(row, i, first_row[i], set_style('Times New Roman', 220, True))
    row += 1
    for item in result_list:
        row_begin = row
        row_end = row
        writer_row(sheet1, row_begin, row_end, item, field_list)
        row += 1
    return excel_stream


def create_excel(result_list, field_list, sheet_name, first_row, tmp_dir):
    try:
        excel_stream = write_excel(result_list, field_list, sheet_name=sheet_name, first_row=first_row)
        excel_path = '%s/%s.xls' % (tmp_dir, sheet_name)
        excel_stream.save(excel_path)
    except Exception as e:
        raise e
    return '%s' % excel_path
