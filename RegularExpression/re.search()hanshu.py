#re.search()函数
import re
print(re.search('hello','hello python').span())

print(re.search('python','hello python').span())