#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Queue
import threading
import time

exitFlag = 0


class MyThread(threading.Thread):
    def __init__(self, thread_id, name, q):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.q = q

    def run(self):
        print "Starting " + self.name
        process_data(self.name, self.q)
        print "Exiting " + self.name


def process_data(threadName, q):
    while not exitFlag:
        queue_lock.acquire()
        if not work_queue.empty():
            data = q.get()
            queue_lock.release()
            print "%s processing %s" % (threadName, data)
        else:
            queue_lock.release()
        time.sleep(1)


if __name__ == '__main__':
    thread_list = ["Thread-1", "Thread-2", "Thread-3"]
    name_list = ["One", "Two", "Three", "Four", "Five"]
    queue_lock = threading.Lock()
    work_queue = Queue.Queue(10)
    threads = []
    thread_id = 1
    
    # 创建新线程
    for tName in thread_list:
        thread = MyThread(thread_id, tName, work_queue)
        thread.start()
        threads.append(thread)
        thread_id += 1
    
    # 填充队列
    queue_lock.acquire()
    for word in name_list:
        work_queue.put(word)
    queue_lock.release()
    
    # 等待队列清空
    while not work_queue.empty():
        pass
    
    # 通知线程是时候退出
    exitFlag = 1
    
    # 等待所有线程完成
    for t in threads:
        t.join()
    print "Exiting Main Thread"
