

def count_word():
    file = open('English_txt', 'r')
    readfile = file.readlines()
    num_dict ={}
    for i in readfile:
        str_line = i
    for code in str_line:
        if code not in num_dict:
            num_dict['{}'.format(code)] = 1
        else:
            num = 1
            num_dict['{}'.format(code)] += num
    return num_dict


if __name__ == '__main__':
    print("统计结果：", count_word())