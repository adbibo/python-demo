#!/usr/bin/env python
# -*- coding=utf-8 -*-

import pika

credentials = pika.PlainCredentials('admin', 'admin')

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.103', 5672, '/', credentials))

channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

print 'starting queue'

connection.close()
