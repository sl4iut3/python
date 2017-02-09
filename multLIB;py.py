def mult(a,b):
    correctif=0
    while a!=1:
        if a%2==1:
            correctif+=b
        print(a,b,correctif,sep=' ')
        a=int(a/2)
        b=b*2
    b=b+correctif
    return b

print(mult(1,51))

