n=int(input("enter the number : "))
List=[]
for i in range(n) :
    a=int(input("Enter the integer number : "))
    List.append(a)
print(List)
List.sort()
print("%d %d"%(List[0],List[-1]))

word=input("Enter one word : ")
count=[0]*6
for letter in word : 
    if letter == 'a' :
        count[0] += 1
    elif letter == 'e' :
        count[1] += 1
    elif letter == 'i' :
        count[2] += 1
    elif letter =='o' :
        count[3] += 1
    elif letter == 'u' :
        count[4] += 1
    else :
        count[5] += 1
print(count)
