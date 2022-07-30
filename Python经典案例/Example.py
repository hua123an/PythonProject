#寻找单词在字符串中的位置
def test():
    message = "Hello,welcome to my world"
    world = "welcome"
    if world in message:
        return message.find(world)
    else:
        return -1
    print(test())
