import sys
input = sys.stdin.readline
INF = int(1e9)

#노드 개수와 간선 갯수 입력
n,m = map(int, input().split())
#시작 노드 번호 입력
start = int(input())
#각 노드에 연결되어 있는 노드에 대한 정보를 담는 공백 리스트 만들기
graph = [[] for _ in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트
visited = [False] * (n+1)
#일단 처음 간선 길이는 무한으로 초기화
distance = [INF] * (n+1)

#모든 간선 정보 입력받기
for _ in range(n+1):
    a,b,c, = map(int, input().split()) # <= a번 노드에서 b번 노드로 가는 비용이 c이다.
    graph[a].append((b,c))
    
    
