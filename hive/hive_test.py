# -*- coding=utf-8 -*-
import sys

import pyhs2
# import xlrd
import xlwt


class HiveClient:
    def __init__(self, db_host, user, password, database, port=10000, auth_mechanism="PLAIN"):
        """
        create connection to hive server2
        """
        self.conn = pyhs2.connect(host=db_host,
                                  port=port,
                                  auth_mechanism=auth_mechanism,
                                  user=user,
                                  password=password,
                                  database=database,
                                  )

    def query(self, sql):
        """
        query
        """
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetch()

    def close(self):
        """
        close connection
        """
        self.conn.close()


def write_xlwt(filename, result):
    book = xlwt.Workbook()  # 打开一个工作薄
    sheet1 = book.add_sheet('sheel1')  # 添加一个sheet页
    for i in range(len(result) + 1):
        if i == 0:
            sheet1.row(i).write(0, '日期')
            sheet1.row(i).write(1, '小时')
            sheet1.row(i).write(2, '楼层')
            sheet1.row(i).write(3, '店铺号')
            sheet1.row(i).write(4, '店铺名称')
            sheet1.row(i).write(5, '人数')
        else:
            for a in range(len(result[i - 1])):
                sheet1.row(i).write(a, result[i - 1][a])
    book.save(filename)


def main():
    """
    main process
    """
    try:
        hive_client = HiveClient(db_host='192.168.14.44', port=10000, user='hive', password='hive', database='test',
                                 auth_mechanism='PLAIN')

        sql = 'SELECT * FROM test LIMIT 10'  # 实例sql语句
        result = hive_client.query(sql)
        hive_client.close()
    except pyhs2.error as tx:
        print('%s' % tx.message)
        sys.exit(1)
    write_xlwt('test.xls', result)


if __name__ == '__main__':
    main()
