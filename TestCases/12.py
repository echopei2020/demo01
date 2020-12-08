import pymysql
conn=pymysql.connect(host='127.0.0.1',user='root',password='cuipei1001?',database='xd_api_test_demo',charset='utf8')
#
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
try:
    sql = "select * from `case` where app='{0}'".format(app)
    cursor.execute(sql)
    data=cursor.fetchall()
    print(data)

except Exception as e:
    print(e)

finally:
    conn.close()