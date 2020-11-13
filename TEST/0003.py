import random, pymysql
def getrandomnum(bits):
    codelist = []
    char_set = [chr(i)for i in range(65, 91)]
    num_set = [chr(i) for i in range(48, 58)]
    total_set = char_set + num_set
    for i in range(200):
        value_set = "".join(random.sample(total_set, bits))
        codelist.append(value_set)
    return (codelist)
def insertcode(codelist):
    try:
        mydb = pymysql.connect(
            host="localhost",  # 数据库主机地址
            user="root",  # 数据库用户名
            passwd="root",  # 数据库密码
            database="test"  # 数据库名称
        )
        cur = mydb.cursor()
    except BaseException as e:
        print(e)
    else:
        try:
            cur.execute('''CREATE TABLE IF NOT EXISTS code(
                              id INT NOT NULL AUTO_INCREMENT,
                              code VARCHAR(32) NOT NULL,
                              PRIMARY KEY(id)
                          )''')
            for code in codelist:
                cur.execute('INSERT INTO code(code) VALUES(%s)',code)
                cur.connection.commit()
        except BaseException as e:
                print(e)
    finally:
        cur.close()
        mydb.close()
if __name__ =='__main__':
    string1 = getrandomnum(8)
    insertcode(string1)
    print("OK")

