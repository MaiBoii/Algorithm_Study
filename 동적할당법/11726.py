import sys
input=sys.stdin.readline
dp=[0]*1003
dp[1]=1
dp[2]=2
n=int(input())
for i in range(3,n+2):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[n]%10007)