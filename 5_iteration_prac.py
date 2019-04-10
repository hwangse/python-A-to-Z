#prob1
L=[5,6,"hello",7,"python"]
L[-1]="World"
print(L[-4],end=" ")
for x in L :
    if type(x)==str :
        print(x,end=" ")
print()

#prob2
L=[1,2,3,4,5]
print(len(L)-1)
print()
#prob3
a=list()
for i in range(1,101) :
    if i%2 == 0 :
        a.append(i)
print(a)
print()
#prob4
for x in a :
    if x%8==0 and x<60 :
        print(x)
print()       
#prob5
score=[82,98,100,40,75,55,73]
i=1
grade=0
for s in score :
    if s>=90 :
       grade='A'
    elif s>=70 :
        grade='B'
    elif s>=50 :
        grade='C'
    else :
        grade='F'
    print("%d번 학생의 성적은 %c입니다."%(i,grade))
    i+=1
#prob6

#prob7
word=input("Please, enter any word : ")
count=0 
for letter in word :
    if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u' :
        count += 1
        
print(count)
    
    
n=int(input("Enter # of lines : "))

for i in range(n,-1,-1) :
    for j in range(i) :
        print("*",end='')
    if i!=1 : 
        print()
