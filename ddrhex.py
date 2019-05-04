import pandas
import numpy
import struct
import codecs

pandas.set_option('display.max_rows', 10000)

ddrmaxjp = pandas.read_csv("/home/annuitydew/ps2/static/DDRMAXJP.csv",usecols=[0,1,2],encoding="utf-8")
ddrmaxjp['short1'] = '0000'
ddrmaxjp['short2'] = '0000'
ddrmaxjp['int32Long'] = 0
ddrmaxjp['int32short1'] = 0
ddrmaxjp['int32short2'] = 0

y = 0
while y < len(ddrmaxjp.index):
    ddrmaxjp.loc[y,'short1'] = str(ddrmaxjp.loc[y,'Long'])[0:4]
    ddrmaxjp.loc[y,'short2'] = str(ddrmaxjp.loc[y,'Long'])[4:8]
    ddrmaxjp.loc[y,'int32Long'] = struct.unpack("<I",codecs.decode(ddrmaxjp.loc[y,'Long'],"hex"))[0]
    ddrmaxjp.loc[y,'int32short1'] = struct.unpack("<I",codecs.decode(ddrmaxjp.loc[y,'short1'] + "0000","hex"))[0]
    ddrmaxjp.loc[y,'int32short2'] = struct.unpack("<I",codecs.decode(ddrmaxjp.loc[y,'short2'] + "0000","hex"))[0]
    y = y + 1

ddrmaxus = pandas.read_csv("/home/annuitydew/ps2/static/DDRMAXUS.csv",usecols=[0,1,2],encoding="utf-8")
ddrmaxus['short1'] = '0000'
ddrmaxus['short2'] = '0000'
ddrmaxus['int32Long'] = 0
ddrmaxus['int32LongHalf'] = 0
ddrmaxus['int32short1'] = 0
ddrmaxus['int32short2'] = 0

x = 0
while x < len(ddrmaxus.index):
    ddrmaxus.loc[x,'short1'] = str(ddrmaxus.loc[x,'Long'])[0:4]
    ddrmaxus.loc[x,'short2'] = str(ddrmaxus.loc[x,'Long'])[4:8]
    ddrmaxus.loc[x,'int32Long'] = struct.unpack("<I",codecs.decode(ddrmaxus.loc[x,'Long'],"hex"))[0]
    if x > 0:
        ddrmaxus.loc[x,'int32LongHalf'] = struct.unpack("<I",codecs.decode(ddrmaxus.loc[x - 1,'short2'] + ddrmaxus.loc[x,'short1'],"hex"))[0]
    ddrmaxus.loc[x,'int32short1'] = struct.unpack("<I",codecs.decode(ddrmaxus.loc[x,'short1'] + "0000","hex"))[0]
    ddrmaxus.loc[x,'int32short2'] = struct.unpack("<I",codecs.decode(ddrmaxus.loc[x,'short2'] + "0000","hex"))[0]
    x = x + 1

ddrmax2us = pandas.read_csv("/home/annuitydew/ps2/static/DDRMAX2US.csv",usecols=[0,1,2],encoding="utf-8")
ddrmax2us['short1'] = '0000'
ddrmax2us['short2'] = '0000'
ddrmax2us['int32Long'] = 0
ddrmax2us['int32LongHalf'] = 0
ddrmax2us['int32short1'] = 0
ddrmax2us['int32short2'] = 0

x = 0
while x < len(ddrmax2us.index):
    ddrmax2us.loc[x,'short1'] = str(ddrmax2us.loc[x,'Long'])[0:4]
    ddrmax2us.loc[x,'short2'] = str(ddrmax2us.loc[x,'Long'])[4:8]
    ddrmax2us.loc[x,'int32Long'] = struct.unpack("<I",codecs.decode(ddrmax2us.loc[x,'Long'],"hex"))[0]
    if x > 0:
        ddrmax2us.loc[x,'int32LongHalf'] = struct.unpack("<I",codecs.decode(ddrmax2us.loc[x - 1,'short2'] + ddrmax2us.loc[x,'short1'],"hex"))[0]
    ddrmax2us.loc[x,'int32short1'] = struct.unpack("<I",codecs.decode(ddrmax2us.loc[x,'short1'] + "0000","hex"))[0]
    ddrmax2us.loc[x,'int32short2'] = struct.unpack("<I",codecs.decode(ddrmax2us.loc[x,'short2'] + "0000","hex"))[0]
    x = x + 1

ddrmaxus.to_csv(path_or_buf="/home/annuitydew/ps2/static/DDRMAXUSout.csv")
ddrmaxjp.to_csv(path_or_buf="/home/annuitydew/ps2/static/DDRMAXJPout.csv")
ddrmax2us.to_csv(path_or_buf="/home/annuitydew/ps2/static/DDRMAX2USout.csv")