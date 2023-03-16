# 무작위의 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 
# 그 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복해보자!

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i #가장 작은 원소가 할당되는 인덱스
    for j in range(i + 1, len(array)): #i 뒤에 있는 것들 중에서
        if array[min_index] > array[j]: #i 보다 작은게 있다면
            min_index = j #그때부터 i 자리는 그 놈 거다!
    array[i], array[min_index] = array[min_index], array[i] #스와프_C++에 비해 훨씬 간단하다 ㄷ

print(array)

#스와프 : 특정한 리스트가 주어졌을때 두 변수의 위치를 변경하는 작업.

array = [3,5]
print(array)
array[0] , array[1] = array[1], array[0]
print(array)

