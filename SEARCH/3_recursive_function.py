#재귀함수 
def recursive_function(i):
    if i == 100:
        return
    print(i, "번째 재귀함수에서", i+1, '번째 재귀 함수를 호출합니다.')
    recursive_function(i+1)
    print(i,"번째 재귀함수를 종료한니다...")

recursive_function(1)

#반복적으로 구현한 팩토리얼
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

#재귀적으로 구현한 팩토리얼
def recursive_factorial(n):
    if n <= 1:
        return 1
    return n * recursive_factorial(n-1)

print("반복적으로 구현: ", factorial_iterative(5))
print("재귀적으로 구현: ", recursive_factorial(5))

