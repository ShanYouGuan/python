import redis, random


def get_random_num(bits):
    codelist = []
    char_set = [chr(i) for i in range(65, 91)]
    num_set = [chr(i) for i in range(48, 58)]
    total_set = char_set + num_set
    for i in range(200):
        value_set = "".join(random.sample(total_set, bits))
        codelist.append(value_set)
    return codelist


def insert_to_redis(my_list):
    redis_conn = redis.Redis(host="127.0.0.1", port=6379, db=0)
    for i in range(200):
        redis_conn.lpush("mycodelist", my_list[i])


if __name__ =='__main__':
    insert_to_redis(get_random_num(8))
    print("插入Redis数据库成功！！")