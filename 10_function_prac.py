def caseChange(sf) :
    st=""
    for c in sf :
        if c.islower() :
            st=st+c.upper()
        elif c.isupper() :
            st=st+c.lower()
        else :
            st=st+c
    return st

while True :
    st=input("Input : ")
    if st=="STOP" :
        print("Bye")
        break;
    print(caseChange(st))
        


def f(x) :
    return 2*x+7
def g(x) :
    return x**3
def haha(x) :
    return f(x)+g(x)+f(g(x))+g(f(x))

for num in range(-9,10) :
    print("x=%2d : %8.2f" %(num,haha(num)))
print("Done")
