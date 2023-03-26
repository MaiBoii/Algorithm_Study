import math

def distance(current, goal):
        key = {1:[0,0], 2:[1,0], 3:[2,0], 
               4:[0,1], 5:[1,1], 6:[2,1],
               7:[0,2], 8:[1,2], 9:[2,2],
               '*':[0,3], 0:[1,3], '#':[2,3]}
        x1,y1 = key[current]
        x2,y2 = key[goal]
        
        result = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
        return result

def solution(numbers, hand):
    answer = ''
    
    left = [1,4,7]
    right = [3,6,9]
    mid = [2,5,8,0]
    
    left_fing = '*'
    right_fing = '#'
    
    for number in numbers:
        if number in left:
            answer += 'L'
            left_fing = number
        elif number in right:
            answer += 'R'
            right_fing = number
        #2,5,8,0일 경우 거리가 작은 곳에서 해야한다.
        elif number in mid:
            if distance(left_fing, number)>distance(right_fing, number):
                answer += 'L'
                left_fing = number
            elif distance(left_fing, number)<distance(right_fing, number):
                answer += 'R'
                right_fing = number
            else:
                if hand == 'left':
                    answer += 'L'
                    left_fing = number
                else:
                    answer += 'R'
                    right_fing = number
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(distance(3,5))