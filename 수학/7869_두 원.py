import sys
import math
input = sys.stdin.readline

x1, y1, r1, x2, y2, r2 = map(float,input().split())

d = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
ans = 0
#1)원이 안 겹치는 경우
if d>=r1+r2:
    ans = 0
#2)원이 포함되는 경우 
elif d+min(r1,r2) <= max(r1,r2):
    ans = min(r1,r2)**2*math.pi
#3) 원의 일부만 겹치는 경우
else:
    각도1= (math.acos((r1**2+d**2-r2**2)/(2*r1*d)))*2
    각도2= (math.acos((r2**2+d**2-r1**2)/(2*r2*d)))*2
    s1 = r1**2*(0.5)*(각도1-math.sin(각도1))
    s2 = r2**2*(0.5)*(각도2-math.sin(각도2))
    ans = s1+s2
print(f"{ans:.3f}")