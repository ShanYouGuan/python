import pymysql

mydb = pymysql.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="root", # 数据库密码
    database="test"#数据库名称
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM employee")
for x in mycursor:
    print(x)
