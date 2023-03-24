from curses import pair_content


n = int(input())

# 1. 5의 배수 2. 5와3의 조합으로 가능 3.조합으로도 안될 때 
# 

if n % 5 == 0:
    print(n // 5)
else:
    p = 0
    while n>0:
        n -= 3
        p += 1
        if n%5 == 0:
            p += n//5
            print(p)
            break
        elif n == 1 or n ==2:
            print(-1)
        elif n == 0:
            print(p)
            break