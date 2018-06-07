#!/usr/bin/env python
# -*- coding=utf-8 -*-

import json

from codec.coder import JsonEncoderUtil
from db.db_util import to_list_dict


# 转换dict为request返回json串
def to_json(result_set, field_num=1, field_list=None):
    result_dict = dict()
    try:
        if result_set is None or len(result_set) == 0:
            result_dict['data'] = []
            result_dict['message'] = 'empty'
            result_dict['code'] = 1
        elif field_num == 1:
            result_dict['data'] = [record[0] for record in result_set]
            result_dict['message'] = 'success'
            result_dict['code'] = 0
        elif field_list is not None:
            result_dict['data'] = to_list_dict(result_set, field_list)
            result_dict['message'] = 'success'
            result_dict['code'] = 0
        else:
            return to_json_empty()
    except Exception, e:
        return to_json_error(e)
    return json.dumps(result_dict, cls=JsonEncoderUtil)


# request返回失败
def to_json_error(e):
    result_dict = dict()
    result_dict['data'] = [e]
    result_dict['message'] = 'failed'
    result_dict['code'] = -1
    return json.dumps(result_dict)


# request返回为空
def to_json_empty():
    result_dict = dict()
    result_dict['data'] = []
    result_dict['message'] = 'empty'
    result_dict['code'] = 1
    return json.dumps(result_dict)


# request返回为单曲线
def to_json_single_curve(list_dict_info, x_field, y_field):
    data_dict = dict()
    for item in list_dict_info:
        if x_field == 'time_s':
            key = item[x_field].split(' ')[1]
        else:
            key = item[x_field]
        if key not in data_dict:
            data_dict[key] = item['sum_item']

    sorted_time_list = sorted(set(data_dict.keys()))
    value_list = list()

    for time_s in sorted_time_list:
        value_list.append(data_dict[time_s])

    series_list = list()
    series_list.append({'data': value_list, 'name': y_field})

    result_dict = dict()
    result_dict['data'] = dict()
    result_dict['data']['date'] = sorted_time_list
    result_dict['data']['series'] = series_list
    result_dict['message'] = 'success'
    result_dict['code'] = 0
    return json.dumps(result_dict)


# request返回为多条曲线
def to_json_graph_format(list_dict_info, x_field, y_field, name_field):
    data_dict = dict()
    for item in list_dict_info:
        name = item[name_field]
        if name not in data_dict:
            data_dict[name] = dict()

        if x_field == 'time_s':
            key = item[x_field].split(' ')[1]
        else:
            key = item[x_field]
        if key not in data_dict[name]:
            data_dict[name][key] = item[y_field]

    time_list = list()
    for name, name_info in data_dict.items():
        time_list.extend(name_info.keys())

    name_dict = dict()
    sorted_time_list = sorted(set(time_list))
    name_list = sorted(data_dict.keys())

    for time_s in sorted_time_list:
        for name in name_list:
            if name not in name_dict:
                name_dict[name] = list()
            item_value = data_dict[name][time_s] if time_s in data_dict[name] else 0
            name_dict[name].append(item_value)

    series_list = list()
    for key, item in name_dict.items():
        series_list.append({'data': item, 'name': key})

    result_dict = dict()
    result_dict['data'] = dict()
    result_dict['data']['date'] = sorted_time_list

    result_dict['data']['series'] = series_list
    result_dict['message'] = 'success'
    result_dict['code'] = 0
    return json.dumps(result_dict)
