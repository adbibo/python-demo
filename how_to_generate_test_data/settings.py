#!/usr/bin/env python
# -*- coding=utf-8 -*-

db_info = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'adbibo',
    'db_name': 'dms_test'
}

engine_url = "mysql://%(user)s:%(password)s@%(host)s:%(port)s/%(db_name)s" % db_info

city_list = [u'深圳',
             u'武汉',
             u'太原',
             u'郑州',
             u'南昌',
             u'大连',
             u'重庆',
             u'石家庄',
             u'济南',
             u'西安',
             u'长春',
             u'成都',
             u'长沙',
             u'合肥',
             u'福州',
             u'常州',
             u'杭州',
             u'南通',
             u'贵阳',
             u'佛山',
             u'青岛',
             u'total',
             u'厦门',
             u'上海',
             u'兰州',
             u'南京',
             u'无锡',
             u'徐州',
             u'洛阳',
             u'广州',
             u'天津',
             u'苏州',
             u'宁波',
             u'东莞',
             u'北京',
             u'沈阳', ]
