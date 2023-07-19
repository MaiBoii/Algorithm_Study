import sys
input = sys.stdin.readline

n,m = map(int, input().split())
data = dict()
for i in range(1,n+1):
    name = str(input().rstrip())
    data[name] = i
    data[i] = name

for i in range(m):
    question = input().rstrip()
    if question.isdigit():
        print(data[int(question)])
    else:
        print(data[question])
