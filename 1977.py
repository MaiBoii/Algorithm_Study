M = int(input())
N = int(input())
number = []

i = 1
while i**2 <= N:
    if M <= i**2 <= N:
        number.append(i ** 2)
    i += 1
if number == []:
    print(-1)
else:
    print(sum(number))
    print(number[0])