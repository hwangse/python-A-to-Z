a=123.456789
print(int(a),float(a))
print()
b=3.14
b=str(b)
print(b,type(b))
b=int(float(b))
print(b,type(b))
b=float(b)
print(b,type(b))
print()
name,num,age=input("Enter 3 things : ").split()
print(name,num,age)
print()
age=int(age)
print("♥"*age)
print()

degree=float(input("본 프로그램은 섭씨를 화씨로 변환해주는 프로그램입니다\n\
변환하고 싶은 섭씨온도를 입력해주세요 : \n"))
print("\n=======================")
print("섭씨온도 ; %.1f" %(degree))
print("화씨온도 : %.2f" %((9/5)*degree+32))



