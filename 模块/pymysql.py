# coding= utf-8
import pymysql

# 连接数据库                  mysql的ip  用户名 密码 要连接的数据库名
db = pymysql.connect("192.168.159.128","long","long","test")

#创建一个cursor对象
cursor = db.cursor()
sql = "select version()"
cursor.execute(sql)
# 获取单条返回的信息
data = cursor.fetchone()
# 获取多条的数据
data = cursor.fetchall()

#使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。

cursor.rowcount
print(data)

# 关闭

cursor.close()
db.close()
