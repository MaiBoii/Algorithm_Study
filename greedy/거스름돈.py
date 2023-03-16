n=int(input())
count = 0

#동전 종류
coins=[500,100,50,10]

#동전을 
for i in coins:
    count += n//i
    n %= i

print(count)