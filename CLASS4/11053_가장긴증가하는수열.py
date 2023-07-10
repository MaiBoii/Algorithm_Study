'''
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 
가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.
'''
A = int(input())
A_arr = list(map(int, input().split()))
dp = [1]*A

for i in range(1,A):
    for j in range(i):
        if A_arr[i]>A_arr[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))


'''
dp = [1,1,1,1,1,1]
dp = [1,2,1,1,1,1]
dp = [1,2,1,1,1,1]
dp = [1,2,1,3,1,1]
'''