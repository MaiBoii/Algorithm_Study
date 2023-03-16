from re import L

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스를 반환한다.
        if array[mid] == target:
            return mid
        # 중간값보다 타겟값이 작을 경우 왼쪽을 확인한다.
        elif array[mid] > target:
            end = mid - 1
        # 중간값보다 타겟값이 더 클 경우 오른쪽을 확인한다.
        else:
            start = mid + 1
        return None

    n = int(input())
    array = list(int, input().split())
    array.sort()

    m = int(input())
    x = list(int, input().split())

    for i in x:
        result = binary_search(array, i , 0 , n-1)
        if result != None:
            print('yes', end = ' ')
        else:
            print('no', end= ' ')        

############ #계수 정렬로 풀기 ###############
n = int(input())
array = [0] * 1000001

for i in input().split():
    array[input[i]] = 1

# M(손님이 확인 요청한 부품 개수)를 입력받기)
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')

############# 집합 자료형으로 풀기 ##############
n = int(input())
array = set(map(int, input().split()))

m = int(input())

x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')