import sys
input=sys.stdin.readline

n=int(input())
count=0
six=666
while count<10000:
    if '666' in str(six):
        count+=1
    if count == n:
        print(six)
        break
    six+=1