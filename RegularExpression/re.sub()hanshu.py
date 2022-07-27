#re.sub()函数
import re
phone = "china + 86 010 - 1234567"

print("tel:",re.sub(r'\D',"","+ 86 010 - 1234567"))
#整理程序后

num=re.sub(r'\D',"",phone)
print("tel:",num)