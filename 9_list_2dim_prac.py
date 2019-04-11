

kor_score = [49,79,20,100,80]
math_score = [43,59,85,30,90]
eng_score = [49,79,48,60,100]
midterm_score = [kor_score, math_score, eng_score]

avg=[0]*len(kor_score)

for List in midterm_score :
    for i,x in enumerate(List) :
        avg[i] += x

for i in range(1,6) :
    print("20170%d 평균: %.2f" %(i,avg[i-1]/3))
