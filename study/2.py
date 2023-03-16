cryptogram=input()
res = []

for i in range(1,len(cryptogram)+1):
    if cryptogram[i]==cryptogram[i+1]:
        res.remove(cryptogram[i],cryptogram[i+1])
