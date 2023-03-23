from datetime import datetime

arr = []
score = [10,8,6,5,4,3,2,1]
red_score = 0
blue_score = 0

for i in range(8):
    race_time_str, team = map(str, input().split())
    race_time_format = '%M:%S:%f'
    racetime_result = datetime.strptime(race_time_str, race_time_format)
    arr.append([racetime_result,team])

arr.sort(key=lambda arr:arr[0])

for i in range(8):
    if arr[i][1] == 'R':
        red_score += score[i]
    else:
        blue_score += score[i]

if red_score > blue_score:
    print('Red')
else:
    print('Blue')


