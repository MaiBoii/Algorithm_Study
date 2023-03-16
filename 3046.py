h,m,s = map(int, input().split())
time = int(input())

whole = h*3600+m*60+s

while(time > 24*3600):
    time -= 24*3600

result = whole + time

if result >= 24*3600:
    result -= 24*3600
if result < 0:
    result += 24*3600

print(result//3600,(result%3600)//60,(result%60))