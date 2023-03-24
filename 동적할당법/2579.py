import sys
input=sys.stdin.readline
st=[0]*301
dp=[0]*301

n=int(input())
for i in range(n):
    st[i]=int(input())
dp[1]=st[0]+st[1]
dp[2]=max(st[1]+st[2],st[0]+st[2])
for i in range(3,n):
    dp[i]=max(dp[i-3]+st[i]+st[i-1],st[i]+dp[i-2])
print(dp[n-1])