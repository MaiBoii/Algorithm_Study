def solution(s):
    array = []
    for i in s:
        if i==')' and len(array) == 0:
            return False
        elif i==')' and array[-1] == '(':
            array.pop()
        else:
            array.append(i)
    if len(array)==0:
        return True
    else:
        return False