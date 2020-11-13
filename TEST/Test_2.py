#题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？
i = int(input("请输入当月利润:"))
arx = [100000, 200000, 400000, 600000, 1000000]
rate = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
if i> arx[0] and i<arx[1]:
    money =arx[0]*rate[0]+(i-arx[0])*rate[1]
    print("应发奖金为：{}".format(money))
elif i <= arx[0]:
    money = i*0.1
    print("应发奖金为：{}".format(money))
elif i>arx[1] and i < arx[2]:
    money = (i - arx[1])* rate[2]
    print("应发奖金为：{}".format(money))
elif i> arx[2]and i < arx[3]:
    money = (i - arx[2])*rate[3]
    print("应发奖金为：{}".format(money))
elif i> arx[3]and i < arx[4]:
    money = (i-arx[3])*rate[4]
    print("应发奖金为：{}".format(money))
elif i > arx[5]:
    money = (i- arx[5])*rate[5]
    print("应发奖金为：{}".format(money))

