'''
정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.
- 2를 곱한다.
- 1을 수의 가장 오른쪽에 추가한다. 
A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.
'''

a,b = map(int, input().split())
cnt = 1
while b!=a:
    cnt+=1
    tmp=b
    if b%10 ==1:
        b//=10
    elif b%2==0:
        b//=2
    
    if tmp==b:
        print(-1)
        break
else:
    print(cnt)