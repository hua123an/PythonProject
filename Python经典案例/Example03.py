#使用while循环语句实现乘法口诀表
i = 1
while i <=9:
    j = i
    while j <= i:
        print("%d*%d=%-2d"%(i,j,i*j),end=" ")
        print()
        i+=1


