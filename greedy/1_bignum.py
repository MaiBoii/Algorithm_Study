n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort() #오름차순으로 정렬
first = data[n - 1] #가장 큰 수 설정
second = data[n - 2] #두 번째로 큰 수 설정

result = 0

while True:
    for i in range(k): 
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

n , m , k = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = (m/(k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m-count) * second

print(result)