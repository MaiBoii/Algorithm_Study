n = int(input())
dp = [-1,-1,1,-1,2,1,3,2,4,3] #1부터 9까지의 패턴
for i in range(10, n+1):
    dp.append(dp[i-5]+1)
print(dp[n])