#计算数字组合方式
sum =  0
for a in range(1,4):
    for b in range(1,4):
        for c in range(1,4):
            if a!=b and b!=c and a!=c:
                print(a,b,c)
                sum += 1
                print("答案为：一共有",sum,'种')