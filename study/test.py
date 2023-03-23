a = 'aaaaaaaa'

# while(len(a) != 3):
#     a = a.lstrip()
#     print(a)

a = a[len(a)-3:]

print(len(a))
print(a)