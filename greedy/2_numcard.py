n,m = map(int,input().split())

result = 0

for i in n:
    data = list(map(int,input().split()))
    min_value = min(data)
    result = max(min_value)
    
print(result)