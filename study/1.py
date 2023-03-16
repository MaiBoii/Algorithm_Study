#최고숫자 구하기
def cal(page):
    a = sum(map(int, str(page[0])))
    b_list = map(int, str(page[0]))
    b = 1
    for i in b_list:
        b *= i
    c = sum(map(int, str(page[1])))
    d_list = map(int, str(page[1]))
    d = 1
    for i in d_list:
        d *= i

    return max([a,b,c,d])

#결과값 구하기
def solution(p, c):
    if p>c:
        return 1
    elif c>p:
        return 2
    elif c==p:
        return 0
    else:
        return -1

if __name__ == '__main__':
    pobi = list(map(int, input().split()))
    crong = list(map(int, input().split()))
    p=cal(pobi)
    c=cal(crong)
    print(solution(p,c))