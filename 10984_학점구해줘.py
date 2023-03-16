T=int(input())
for i in range(T):
    N=int(input())
    C=0
    G=0
    for i in range(N):
        a,b=map(float,input().split())
        C+=a
        G+=a*b
    GPA=G/C
    print(int(C),'%.1f'%GPA)