n = int(input())
paper = []
white, blue = 0,0
for i in range(n):
    arr = list(map(int, input().split()))
    paper.append(arr)

def cut(x,y,n):
    global white,blue
    color = paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != paper[i][j]:
                cut(x,y,n//2)
                cut(x,y+n//2,n//2)
                cut(x+n//2,y,n//2)
                cut(x+n//2,y+n//2,n//2)
                return 
    if color == 1:
            blue += 1
    else:
            white += 1
cut(0,0,n)
print(white)
print(blue)