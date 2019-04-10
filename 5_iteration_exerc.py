n=int(input("Enter N(>=1, odd) : "))
if n>=1 and n%2==1 :
    Max=(n+1)//2
    for i in range(1,Max+1) :
        for j in range(i) :
            print("*",end="")
        print()
    for i in range(n-Max,0,-1) :
        for j in range(i) :
            print("*",end="")
        if i!= 1 : 
            print()
else :
    print("N must be >=1 and odd!")
