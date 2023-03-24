import sys
input = sys.stdin.readline

a,b,c = map(int, input().split())

def fpow(a,b,c):
    if b == 1:
        return a%c
    else:
        tmp = fpow(a, b//2, c)
        if b%2 == 0:
            return (tmp*tmp)%c
        else:
            return (tmp*tmp*a)%c
        
print(fpow(a,b,c))