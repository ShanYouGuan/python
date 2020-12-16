# def get_filelines(filename):
#     with open(filename,'rb') as f:
#         return f.readlines()
#
#
# if __name__ == '__main__':
#     for i in get_filelines():
#         #process(i)
# 如果这个电脑内存只有4G，而你的数据有10G
def get_filelines(filename):
    with open(filename,'rb') as f:
        yield f.readlines()