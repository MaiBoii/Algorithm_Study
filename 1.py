from math import prod
while(True):
    pobi=int(input())
    pobi_page=[pobi,pobi+1]
    crong=int(input())
    crong_page=[crong,crong+1]
    if pobi_page[1]-pobi_page[0]!=1 or crong_page[1]-crong_page[0]!=1:
        print(-1)
        break
    a=sum(int(i) for i in str(pobi_page[0])) 
    b=prod(int(i) for i in str(pobi_page[0]))
    c=sum(int(i) for i in str(pobi_page[1])) 
    d=prod(int(i) for i in str(pobi_page[1]))
    p=[a,b,c,d]
    pobi_score=max(p)
    a1=sum(int(i) for i in str(crong_page[0])) 
    b1=prod(int(i) for i in str(crong_page[0]))
    c1=sum(int(i) for i in str(crong_page[1])) 
    d1=prod(int(i) for i in str(crong_page[1]))
    c=[a1,b1,c1,d1]
    crong_score=max(c)

    if pobi_score>crong_score:
        print(1)
    elif pobi_score<crong_score:
        print(2)
    elif pobi_score==crong_score:
        print(0)


