import sys
input = sys.stdin.readline
dp=[1]*42
dp[0]=0
dp[1]=1
for i in range(2,41):
    dp[i]=dp[i-2]+dp[i-1]

t=int(input())
for i in range(t):
    n=int(input())
    print(dp[n-1],dp[n])