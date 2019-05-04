import csv

ddrmax2usout = open("C:/Users/Mike Tarpey/OneDrive/Dev/tarpeydev/devcoldtake/ps2/static/DDRMAX2USout.csv",'w')
ddrmax2us = open("C:/Users/Mike Tarpey/OneDrive/Dev/tarpeydev/devcoldtake/ps2/static/ddrmax2us20190425",'rb')
max2w = csv.writer(ddrmax2usout,delimiter=',',lineterminator = '\n')
y = 0

while y <= -1: #24108
    ddrmax2us.seek(y,0)
    i = int.from_bytes(ddrmax2us.read(4), byteorder='little')
    j = int.from_bytes(ddrmax2us.read(2), byteorder='little')
    ddrmax2us.seek(y+2,0)
    k = int.from_bytes(ddrmax2us.read(2), byteorder='little')
    max2w.writerow([str(y),str(i),str(j),str(k)])
    y = y + 4

ddrex2usout = open("C:/Users/Mike Tarpey/OneDrive/Dev/tarpeydev/devcoldtake/ps2/static/EXTREME2USout.csv",'w')
ddrex2us = open("C:/Users/Mike Tarpey/OneDrive/Dev/tarpeydev/devcoldtake/ps2/static/extreme2us20190419",'rb')
ex2w = csv.writer(ddrex2usout,delimiter=',',lineterminator = '\n')
y = 0

while y <= 143424: #143424
    ddrex2us.seek(y,0)
    i14 = int.from_bytes(ddrex2us.read(4), byteorder='little')
    i12 = int.from_bytes(ddrex2us.read(2), byteorder='little')
    ddrex2us.seek(y+2,0)
    i34 = int.from_bytes(ddrex2us.read(2), byteorder='little')
    ddrex2us.seek(y,0)
    i1 = int.from_bytes(ddrex2us.read(1), byteorder='little')
    i13 = int.from_bytes(ddrex2us.read(3), byteorder='little')
    ddrex2us.seek(y+1,0)
    i2 = int.from_bytes(ddrex2us.read(1), byteorder='little')
    i24 = int.from_bytes(ddrex2us.read(3), byteorder='little')
    ddrex2us.seek(y+2,0)
    i3 = int.from_bytes(ddrex2us.read(1), byteorder='little')
    ddrex2us.seek(y+3,0)
    i4 = int.from_bytes(ddrex2us.read(1), byteorder='little')
    ex2w.writerow([str(y),str(i14),str(i12),str(i34),str(i1),str(i2),str(i3),str(i4),str(i13),str(i24)])
    y = y + 4