s=input("Enter string : ")
for x in s :
    
    if x.isdigit() :
        count=int(x)
    else :
        print(x*count,end="")
print()

dan=-1
while dan!=0 :
    dan=int(input("구구단 몇단을 계산할까요(1~9)?\n"))
    if dan>=1 and dan<=9 : 
        print("구구단 %d단을 계산합니다." %dan)
        for i in range(1,10) :
            print("%d X %d = %d"%(dan,i,dan*i))
    elif dan==0 :
        print("구구단 게임을 종료합니다")
    else :
        dan=int(input("잘못 입력하셨습니다. 1~9 사이 숫자를 입력해주세요!!\n"))


        
n=int(input("n : "))


for i in range(1,n+1) :
    print(" "*(n-i),end="")
    print("*"*(2*i-1))
for i in range(n-1,0,-1) :
    print(" "*(n-i),end="")
    print("*"*(2*i-1))
