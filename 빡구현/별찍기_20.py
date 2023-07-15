n = int(input())

def star(leng):
    if leng==3:
        return ['***','* *','***']
    else:
        arr = star(leng//3)
        stars = []
        for i in arr:
            stars.append(i + i + i)
        for i in arr:
            stars.append(i + ' '*(leng//3) + i)
        for i in arr:
            stars.append(i + i + i)
        return stars

print('\n'.join(star(n)))