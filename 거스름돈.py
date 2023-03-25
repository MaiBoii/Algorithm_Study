n = int(input())
coins =[5,2]
count = 0

for i in coins:
    count += n//i
    n = n%i

print(count)