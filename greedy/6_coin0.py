n, k = map(int, input().split())

values = list()

for i in range(n):
    values.append(int(input())) #몰랐던거

count = 0

for i in reversed(range(n)): #range는 범위를 반환하는 것이지, 리스트 자체를 반환하는 것은 아니다.
    count += k//values[i] #앞 원소가 뒤 원소의 약수기 때문에 몫을 계속 더해주면 최소값이 나옴
    k = k % values[i] #몰랐던거 : 앞 원소로 넘어가기 전에 k를 그 시점의 나머지로 초기화해줌.

print(count)