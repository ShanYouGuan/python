import random
def Getrandomnum(bits):
    char_set = [chr(i)for i in range(65, 91)]
    num_set = [chr(i) for i in range(48, 58)]
    total_set = char_set + num_set
    for j in range(200):
        value_set = "".join(random.sample(total_set, bits))
        print(value_set)
if __name__ =='__main__':
    Getrandomnum(8)

