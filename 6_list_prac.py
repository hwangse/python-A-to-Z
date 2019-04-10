#prac1
a,b=input("자연수 두개를 입력하시오 : ").split()
a=int(a);b=int(b)

if a>b :
    x=a
    y=b
else :
    x=b
    y=a
    
r=-1
gcd=-1
while r != 0 :
    r=x%y
    #print("x= %d, y= %d, r= %d"%(x,y,r))
    if r==0 :
        gcd=y
        break
    x=y
    y=r

print("GCD({}, {}) = {}".format(a,b,gcd))

#prac2

decimal=int(input("input decimal number : "))

i=0
dec_list=""
while True :
    print("------%dth loop value check------"%(i))
    r=decimal%2
    y=decimal//2
    print("initial decimal : %d" %decimal)
    print("remainder : %d" %r)
    print("output decimal : %d" %y)
    print("initial result:",dec_list)
    dec_list=str(r)+dec_list
    print("output result:",dec_list)
    print("----------------------------------\n")
    decimal=y
    i+=1
    if y==0 : break

print("\nbinary number is {}".format(dec_list))
    
