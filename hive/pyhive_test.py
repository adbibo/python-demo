#!/usr/bin/env python
# -*- coding=utf-8 -*-

from pyhive import hive
from TCLIService.ttypes import TOperationState


cursor = hive.connect('localhost').cursor()

cursor.execute('show databases;')

status = cursor.poll().operationState
while status in (TOperationState.INITIALIZED_STATE, TOperationState.RUNNING_STATE):
    logs = cursor.fetch_logs()
    for message in logs:
        print(message)
