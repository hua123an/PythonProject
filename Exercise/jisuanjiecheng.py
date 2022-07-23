#计算阶乘
num = float(10.0)

factorial = 1

if num <0:
    print("输入的数值有误")
elif num == 0:
    print("0的阶乘是1")
else:
    for i in range(1,num+1):
        factorial=factorial * i
        print("%d的阶乘为%d"%(num,factorial))