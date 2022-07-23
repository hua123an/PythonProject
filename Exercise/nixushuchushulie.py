#import "nixushulie.py"
#逆序输出列表
def Reverse(lst):
    return[ele for ele in reversed(lst)]

lst={1,2,3,4,5,6,7,8,9,20}

print(Reverse(lst))