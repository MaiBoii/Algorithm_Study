import sys
input = sys.stdin.readline

#특정 원소가 속한 집합 탐색
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent, a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

#노드 개수 및 간선 개수 입력
n,m = map(int, input().split())
parent = [0] * (n+1) #부모 테이블 초기화

#모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

#부모 테이블에서 부모를 자기 자신으로 초기화
for i in range(1,n+1):
    parent[i] = i

#모든 간선 정보 입력 받기
for _ in range(m):
    a,b,cost = map(int,input().split())
    #비용 순으로 정렬하기 위해 튜플의 처
    edges.append((cost, a,b))

#간선은 비용 순으로 정렬
edges.sort()
last = 0 #최소 신장 트리에 포함되는 간선 중 가장 비용이 큰 간선 선택

#간선을 하나씩 확인
for edge in edges:
    cost,a,b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a,b)
        result += cost
        last = cost

print(result-last)