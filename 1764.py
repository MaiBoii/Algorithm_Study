import sys
input=sys.stdin.readline
n_set=set()
m_set=set()
n,m=map(int,input().split())
for i in range(n):
    lstn=input()
    n_set.add(lstn)
for i in range(m):
    seen=input()
    m_set.add(seen)
nm_set=sorted(n_set&m_set)
print(len(nm_set))
for i in range(len(nm_set)):
    print(nm_set[i].rstrip('\n'))