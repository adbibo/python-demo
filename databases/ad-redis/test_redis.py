#!/usr/bin/env python
# -*- coding=utf-8 -*-

import redis


def hello_world():
    r = redis.Redis('127.0.0.1', port=6379)
    r.set('name', 'hello world!')

    print(r.get('name'))


def redis_connect_pool():
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379)

    r = redis.Redis(connection_pool=pool)

    pipe = r.pipeline(transaction=True)

    r.set('name', 'alex')
    r.set('role', 'sb')

    pipe.execute()


if __name__ == '__main__':
    redis_connect_pool()