#!/usr/bin/env python
# -*- coding=utf-8 -*-


# 将数据库查询的结果每天都转换成dict形式，其实key为字段名，value为字段值
def to_list_dict(result_set, field_list):
    try:
        result_list = list()
        if len(result_set) == 0:
            return result_list

        for result in result_set:
            if len(result) != len(field_list):
                raise ValueError("width of record not equal key fields")
            result_dict = dict()
            for index, field in enumerate(field_list):
                result_dict[field] = result[index]
            result_list.append(result_dict)
    except Exception as e:
        raise e
    return result_list


# 将每条记录都按键值对的方式存储
# 注意：所有的记录中key必须是唯一的
def to_dict_with_key(result_set, field_list, key):
    try:
        result_dict = dict()

        if len(result_set) == 0:
            return result_dict
        for result in result_set:
            if len(result) != len(field_list):
                raise ValueError("width of record not equal key fields")
            key_value = result[field_list.index(key)]

            record_dict = dict()
            for index, field in enumerate(field_list):
                record_dict[field] = result[index]

            if key_value not in result_dict:
                result_dict[key_value] = record_dict
            else:
                raise "key field [%s] not unique" % key
    except Exception as e:
        raise e
    return result_dict


# 将每条记录都按键值对的方式存储
# 注意：所有的记录中key必须是唯一的
def to_dict_with_keys(result_set, field_list, key_fields, split_mark='-'):
    try:
        result_dict = dict()

        if len(result_set) == 0:
            return result_dict
        for result in result_set:
            if len(result) != len(field_list):
                raise ValueError("width of record not equal key fields")
            key_value_list = list()
            for index, field in enumerate(field_list):
                key_value_list.append(result[index])
            key_value = split_mark.join(key_value_list)

            record_dict = dict()
            for index, field in enumerate(field_list):
                record_dict[field] = result[index]

            if key_value not in result_dict:
                result_dict[key_value] = record_dict
            else:
                raise ValueError("key fields [%s] not unique" % split_mark.join(key_fields))
    except Exception as e:
        raise e
    return result_dict


# 获取所有的关键字集合列表
def get_key_list(result_set, field_list, key):
    try:
        key_list = list()
        for result in result_set:
            if len(result) != len(field_list):
                raise ValueError("width of record not equal key fields")
            index = field_list.index(key)
            key_list.append(result[index])
    except Exception as e:
        raise e
    return key_list


# 获取所有的包含关键字的记录
def get_key_record(result_set, field_list, key, key_list):
    try:
        result_list = list()
        for result in result_set:
            if len(result) != len(field_list):
                raise ValueError("width of record not equal key fields")
            key_value = result[field_list.index(key)]
            if key_value in key_list:
                result_list.append(result)
    except Exception as e:
        raise e
    return result_list


# 输出数据库查询结果
def print_result_set(result_set, split_mark="-"):
    try:
        if result_set is None or len(result_set) == 0:
            raise ValueError("result set is NULL.")
        print('\n'.join([split_mark.join(t_record) for t_record in result_set]))
    except Exception as e:
        raise e
