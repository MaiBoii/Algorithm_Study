n,m = map(int,input().split())
dict = {}
for i in range(n):
    team = input()
    num = int(input())
    arr= []
    for _ in range(num):
        name = input()
        arr.append(name)
    dict[team] = '-'.join(sorted(arr))

for _ in range(m):
    quiz_name = input()
    quiz = int(input())
    if quiz == 0:
        for i in dict[quiz_name].split('-'):
            print(i)
    elif quiz == 1:
        for team,members in dict.items():
            if quiz_name in members.split('-'):
                print(team)