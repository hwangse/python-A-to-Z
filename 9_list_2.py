def char_freq(s) :
    d={}
    for letter in s :
        
        if letter.isspace() :
            continue
        else :
            letter=letter.lower()
            d[letter]=d.get(letter,0)+1
    return d
    
s="Follow me!"
D=char_freq(s)
for a,b in D.items() :
    print("{} : {}".format(a,b))


kor_score = [49,79,20,100,80]
math_score = [43,59,85,30,90]
eng_score = [49,79,48,60,100]
midterm_score = [kor_score, math_score, eng_score]

for List in midterm_score :
    for score in List :
        if score >= 90 :
            letter='A'
        elif score >= 80 :
            letter='B'
        elif score >= 70 :
            letter='C'
        elif score >=60 :
            letter='D'
        else :
            letter='F'
        print(letter,end=" ")
    print()



avg=[0]*len(kor_score)


for List in midterm_score :
    for i,x in enumerate(List) :
        avg[i] += x

for i in range(1,6) :
    print("20170%d 평균: %.2f" %(i,avg[i-1]/3))
