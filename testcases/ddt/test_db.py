# -*- coding:utf-8 -*-
import MySQLdb
import pytest

conn = MySQLdb.connect(
    host='159.75.96.188',
    port=3306,
    user='root',
    passwd='bo69nyCG7t04',
    db='testing_db',
    charset='gbk',
    # cursorclass=MySQLdb.cursors.DictCursor
)


# 数据库测试
def get_data():
    query_sql = 'select * from user_tbl;'
    lst = []
    try:
        cursor = conn.cursor()
        cursor.execute(query_sql)
        r = cursor.fetchall()
        for x in r:
            u = (x[0], x[1], x[2])
            lst.append(u)
        return lst
    finally:
        cursor.close()
        conn.close()


@pytest.mark.parametrize('id, name, pwd', get_data())
def test01(id, name, pwd):
    print(id, name, pwd)


if __name__ == '__main__':
    pytest.main('-sv', 'test_db.py')
