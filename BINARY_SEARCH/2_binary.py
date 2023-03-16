#이진 탐색: 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 것, 
#이미 정렬이 되어 있어야만 할 수 있음.

#재귀함수.ver
# def binary_search(array,target,start,end):
#     if start>end:
#         return None
#     mid = (start+end) // 2

#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid - 1)
#     else:
#         return binary_search(array, target, mid+1, end)

# n, target, = list(map(int, input().split()))
# array = list(map(int, input().split()))

# result = binary_search(array, target, 0, n-1)
# if result == None:
#     print("해당 원소가 존재하지 않습니다.")
# else:
#     print(result+1)

#반복문.ver

def binary_search(array, target, start,end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

n, target, = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("해당 원소가 존재하지 않습니다.")
else:
    print(result+1)