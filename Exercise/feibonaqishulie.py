def recur_fio(n):
    if n<1:
        return n
    else:
        return (recur_fio(n-1)+recur_fio(n-2))
    nterms = 20

    if nterms <=0:
        print("输入正数:")
    else:
        print("斐波那契数列为:")
        for i in range(nterms):
            print(recur_fio(i))