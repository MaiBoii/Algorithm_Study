import sys
ch, cm, cs = map(int, input().split(":"))
bh, bm, bs = map(int, input().split(":"))

wholetime = (bh*3600 + bm*60 + bs) - (ch*3600 + cm*60 + cs)
if wholetime < 0:
    wholetime += 3600*24

rh = int(wholetime/3600)
rm = int((wholetime%3600)/60)
rs = wholetime%60

print("%02d:%02d:%02d" %(rh, rm, rs))