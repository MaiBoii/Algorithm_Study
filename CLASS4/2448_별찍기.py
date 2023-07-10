n = int(input())

def star(leng):
    if leng==3:
        return ['  *  ',' * * ','*****']
    else:
        arr = star(leng//2)
        stars = []
        for i in arr:
                stars.append(' '*(leng//2)+i+' '*(leng//2))
        for i in arr:
                stars.append(i + ' ' + i)
        return stars

print('\n'.join(star(n)))