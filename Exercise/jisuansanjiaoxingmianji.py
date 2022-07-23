a = float(3.0)   #输入三角形的第一条边

b= float(4.0)    #输入三角形的第二条便

c = float(5.0)     #输入三角形的第三条边

s = (a+b+c)/2    #三角形面积计算公式

area=(s*(s-a)*(s-b)*(s-c))**0.5


print(area)


