a,b = map(int,input().split())
a_set=set(map(int, input().split()))
b_set=set(map(int, input().split()))

res = a_set-b_set
if not res:
    print(0)
else:
    print(len(res))
    print(*sorted(list(res)))