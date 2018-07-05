#!/usr/bin/env python
# -*- coding=utf-8 -*-

from datetime import date, datetime
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Factory

from settings import engine_url, city_list
from models import DmsZkMatterDetail

engine = create_engine(engine_url)


def get_ratio():
    return round(random.random(), 8)


def get_year(faker, _max=2018):
    return faker.random_int(2010, max=_max)


def get_int(faker, _max=999999):
    return faker.random_int(max=_max)


def get_city_name(faker, city_list):
    return faker.random_sample(elements=city_list, length=1)[0]


def insert_many():
    Session = sessionmaker(bind=engine)
    session = Session()
    faker = Factory.create()  # 生成虚假数据
    faker_users = [DmsZkMatterDetail(
        query_date=date.today(),
        period_id=divmod(i, 53)[1],
        period_name='week %d' % divmod(i, 53)[1],
        period_flag=faker.random_sample(elements=['W', 'M'], length=1)[0],
        week_start_date=date.today(),
        week_end_date=date.today(),
        cla_year=get_int(faker),
        city_id=divmod(i, 53)[1],
        city_name=faker.words()[0],
        dept_id=divmod(i, 53)[1],
        dept_name=faker.words()[0],
        resource_qty=get_int(faker),
        new_signed_qty=get_int(faker),
        total_signed_qty=get_int(faker),
        conversion_ratio=get_int(faker),
        signed_amt=get_int(faker),
        new_signed_amt=get_int(faker),
        continue_signed_amt=get_int(faker),
        study_hours_amt=get_int(faker),
        study_hours=get_int(faker),
        payment_qty=get_int(faker),
        online_stu_qty=get_int(faker),
        online_qty=get_int(faker),
        continue_signed_qty=get_int(faker),
        apply_refund_qty=get_int(faker),
        refund_qty=get_int(faker),
        on_class_ratio=get_int(faker),
        full_class_ratio=get_int(faker),
        suspend_class_ratio=get_int(faker),
        seat_qty=get_int(faker),
        seat_used_ratio=get_int(faker),
        emp_qty=get_int(faker),
        emp_capacity_qty=get_int(faker),
        ly_resource_qty=get_int(faker),
        ly_new_signed_qty=get_int(faker),
        ly_total_signed_qty=get_int(faker),
        ly_conversion_ratio=get_int(faker),
        ly_signed_amt=get_int(faker),
        ly_new_signed_amt=get_int(faker),
        ly_continue_signed_amt=get_int(faker),
        ly_study_hours_amt=get_int(faker),
        ly_study_hours=get_int(faker),
        ly_payment_qty=get_int(faker),
        ly_online_stu_qty=get_int(faker),
        ly_online_qty=get_int(faker),
        ly_continue_signed_qty=get_int(faker),
        ly_apply_refund_qty=get_int(faker),
        ly_refund_qty=get_int(faker),
        ly_on_class_ratio=get_int(faker),
        ly_full_class_ratio=get_int(faker),
        ly_suspend_class_ratio=get_int(faker),
        ly_seat_qty=get_int(faker),
        ly_seat_used_ratio=get_int(faker),
        ly_emp_qty=get_int(faker),
        ly_emp_capacity_qty=get_int(faker),
        yty_resource_qty=get_ratio(),
        yty_new_signed_qty=get_ratio(),
        yty_total_signed_qty=get_ratio(),
        yty_conversion_ratio=get_ratio(),
        yty_signed_amt=get_ratio(),
        yty_new_signed_amt=get_ratio(),
        yty_continue_signed_amt=get_ratio(),
        yty_study_hours_amt=get_ratio(),
        yty_study_hours=get_ratio(),
        yty_payment_qty=get_ratio(),
        yty_online_stu_qty=get_ratio(),
        yty_online_qty=get_ratio(),
        yty_continue_signed_qty=get_ratio(),
        yty_apply_refund_qty=get_ratio(),
        yty_refund_qty=get_ratio(),
        yty_on_class_ratio=get_ratio(),
        yty_full_class_ratio=get_ratio(),
        yty_suspend_class_ratio=get_ratio(),
        yty_seat_qty=get_ratio(),
        yty_seat_used_ratio=get_ratio(),
        yty_emp_qty=get_ratio(),
        yty_emp_capacity_qty=get_ratio(),
        update_date=datetime.now()
    ) for i in range(1000)]

    session.add_all(faker_users)
    session.commit()


if __name__ == '__main__':
    insert_many()
