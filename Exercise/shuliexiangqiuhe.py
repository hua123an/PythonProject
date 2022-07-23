#求取所给数列的和

total=0

list1={1,2,3,4,5}

for ele in range(0,len(list1)):
    total =total + list1[ele]

    print("列表中元素之和:",total)