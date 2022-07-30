#字符串拼接
test = ["hello","world","yoyo"]

#定义一个字符串
j=""
#利用for循环打印列表数据
for i in test:
    j = j+"-"+i

    print(j.lstrip("-"))