year=int(input("당신이 태어난 년도를 입력하세요 : "))
print()

age=2019-year+1

if age>26 :
    status="非"
elif age>=20  :
    status="대"
elif age>=17 :
    status="고등"
elif age>=14 :
    status="중"
elif age>=8 :
    status="초등"
else :
    status="非"
print("{}학생입니다".format(status))
print()

y=int(input("임의의 연도를 입력하시오 : "))

flag=0
if y%400==0 or (y%4==0 and y%100!=0) :
    flag=1

if flag : 
    print("{} : 윤년".format(y))
else :
    print("{} : 윤년이 아님".format(y))
