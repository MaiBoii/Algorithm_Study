import math
def primenumber(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(x) + 1)):	# 2부터 x의 제곱근까지의 숫자
            if x % i == 0:		# 나눠떨어지는 숫자가 있으면 소수가 아님
                return False
        return True		

def two_sum(x):
    arr = []
    for i in range(1, x):
        arr.append([i, x-i])
    return arr

N = int(input())
for i in range(N):
    a = int(input())
    sum_nums = two_sum(a)
    result = []
    for i in range(len(sum_nums)):
        if primenumber(sum_nums[i][0]) == True and primenumber(sum_nums[i][1]) == True:
            result.append(1)
        else:
            result.append(0)

    if 1 in result:
        print('Yes')
    else:
        print('No')

