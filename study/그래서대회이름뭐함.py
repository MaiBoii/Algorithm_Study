exceptions = ['A', 'E', 'I', 'O', 'U'] #모음 제외
n,m = map(int, input().split()) 
S = input()

if m>n or 'A' not in S: #M이 N보다 큰 경우와 A가 S에 없는 경우엔 일단 NO 처리
    print('NO')
else:
    while(S[-1] in exceptions): #마지막에 모음이 없어질때까지 없앰
            S = S[:-1]
    else:
        while(S[-2] != 'A'): #
                S =  S[:-2] + S[-1:]
        if('A' not in S[:-2]): #A가 2개가 아닌 경우 NO
            print('NO')
        while(S[-3] != 'A'):
                S =  S[:-3] + S[-2:]
                S= S[len(S)-m:]
                print('YES')
                print(S)