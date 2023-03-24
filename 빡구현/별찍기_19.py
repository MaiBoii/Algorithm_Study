N = int(input())
result = [[' ' for _ in range(4*N-3)] for _ in range(4*N-3)] #이러면 2차원 배열을 더 간단히 할 수 있다

def draw_star(n,x,y):
    if n == 1:
        result[x][y] = '*'
        return 
    
    length = 4 * n - 3

    for i in range(length):
        result[x][y+i] = '*'
        result[x+i][y] = '*'
        result[x+length-1][y+i] = '*'
        result[x+i][y+length-1] = '*'
    
    draw_star(n-1, x+2, y+2) #재귀함수

draw_star(N,0,0)
for i in result:
    print(''.join(i))