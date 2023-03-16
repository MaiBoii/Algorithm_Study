#최대공약수, 최소공배수 유클리드 호제법

a, b = map(int, input().split())

for i in range(min(a,b),1, -1): 
    if (a%i == 0) and (b % i == 0):
        print(i)
        break

for i in range(max(a,b), (a*b) + 1):
    if (i%a == 0) and (i%b == 0):
        print(i)
        break

#호제법이란 말은 두 수가 서로 상대방 수를 나누어서 결국 원하는 수를 얻는 알고리즘을 나타낸다.
#2개의 자연수 a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a > b),a와 b의 최대공약수는 b와 r의 최대공약수와 같다.
#이 성질에 따라, b를 r로 나눈 나머지 r'를 구하고, 다시 r을 r'로 나눈 나머지를 구하는 과정을 반복하여 
# 나머지가 0이 되었을 때 나누는 수가 a와 b의 최대공약수이다.