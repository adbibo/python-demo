#!/usr/bin/env python
# -*- coding=utf-8 -*-

import math
from datetime import date, datetime, timedelta
import time


class TMUtil(object):

    def __init__(self, dt, format_str="%Y-%m-%d %H:%M:%S"):
        if isinstance(dt, datetime) or isinstance(dt, date):
            self._format_date = dt
        else:
            self._format_date = datetime.strptime(dt, format_str)

        self._weekday = self._format_date.isocalendar()[2]

    # 通过一周的第一天获取当前周范围字符串
    def get_week_range(self, mode=0):
        first_date = self._format_date
        last_date = first_date + timedelta(days=6)
        if mode == 0:
            return '%s~%s' % (first_date.strftime('%Y年%m月%d日'), last_date.strftime('%m月%d日'))
        elif mode == 1:
            return '%s~%s' % (first_date.strftime('%m-%d'), last_date.strftime('%m-%d'))

    # 获取指定日期所在周的上一周第一天
    def get_last_week_first_day(self, mode=0, result_format="%Y%m%d"):
        day_delta = self._weekday + 6
        last_week_first_date = self._format_date - timedelta(days=day_delta)
        if mode == 0:
            return last_week_first_date.strftime(result_format)
        else:
            return last_week_first_date

    # 获取指定日期所在周的下一周第一天
    def get_next_week_first_day(self, mode=0, result_format="%Y%m%d"):
        day_delta = 8 - self._weekday
        next_week_first_date = self._format_date + timedelta(days=day_delta)
        if mode == 0:
            return next_week_first_date.strftime(result_format)
        else:
            return next_week_first_date

    # 计算当天00:00:00到dt时的秒数
    def date_to_seconds(self):
        start_ts = int(time.mktime(self._format_date.date().timetuple()))
        now_ts = int(time.mktime(self._format_date.timetuple()))
        return now_ts - start_ts

    # 将秒数转换为 HH:
    @staticmethod
    def seconds2hms(seconds):
        integer_second = math.ceil(float(seconds))
        hour = int(integer_second) / 3600
        minute = (int(integer_second) - hour * 3600) / 60
        second = int(integer_second) % 60
        return "%02d:%02d:%02d" % (hour, minute, second)

    # 获取某年第N天的日期
    @staticmethod
    def get_date_by_day(year, day):
        return datetime(year, 1, 1) + timedelta(days=day - 1)


if __name__ == "__main__":
    tm = TMUtil(datetime.now())
    print(tm.date_to_seconds())
    print(tm.get_next_week_first_day())
    print(tm.get_last_week_first_day())
    print(tm.get_week_range())
