import sys
input = sys.stdin.readline

def fib(n) :
    if n == 1 or n == 2:
         return 1
    else:
        return (fib(n - 1) + fib(n - 2))

def dp_fibo(n):
    dp_arr = [1,1,2]
    count = 0
    for i in range(3,n+1):
        fibo = dp_arr[i-1] + dp_arr[i-2]
        dp_arr.append(fibo)
        count += 1
    return count

n = int(input())
print(fib(n),dp_fibo(n))