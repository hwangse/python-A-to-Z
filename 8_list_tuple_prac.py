s=input("Enter string : ").split()
print("number of words in s : %d" %len(s))

Sum=0
for a in s : 
    Sum += len(a)
print("average length : %.2f" %(Sum/len(s)))

L=[3,7,6,11,5]
first=L[0]

for i in range(1,len(L)) :
    L[i-1]=L[i]
L[-1]=first
print(L)
print()
L = [[1,2,3], [1,4], [7], [1,3,5,7]]
i=0
for a in L :
    Sum=0
    for b in a :
        Sum += b*b
    L[i]=Sum
    i+=1
print(L,"\n")
