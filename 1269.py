a,b = map(int, input().split())
a_set=set(list(map(int, input().split())))
b_set=set(list(map(int, input().split())))

c_set = set()
c_set.update(a_set-b_set)
c_set.update(b_set-a_set)
print(len(c_set))
