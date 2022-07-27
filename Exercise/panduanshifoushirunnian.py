#判断是否是闰年
num = 20000
if num%100==0:
    if num%400==0:
        print("%s是闰年"%num)
    else:
        print("%s不是闰年"%num)
else:
    if num%4==0:
        print("%s是闰年"%num)
    else:
        print("%s不是闰年"%num)
