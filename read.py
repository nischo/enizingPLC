#test
import snap7
import snap7.util
import struct
import time
from struct import unpack
from struct import pack
from db_layout import *

#connection to plc
plc = snap7.client.Client()
plc.connect("10.7.14.92",0,2)
connected = plc.get_connected()

if connected:
    print("connected to plc")
else:
    print("not connected")

i = 0

# Read DB80 
while i < 1:
    db = plc.db_read(80,20,2)

    for x in range(len(db)):
        print(db[x])

    time.sleep(0)
    i = i + 1
print ('##########')

#download DB80 from PLC to PC
all_data = plc.upload(80)

db80 = snap7.util.DB(80,all_data,db_layout,96,32)

print(db80[0])

# little endian, signed
#tos = unpack('>'+'h'*(len(db)//2),db)

# big endian, signed
#tos = unpack('>'+'h'*(len(db)//2),db)

print (tos[0])

#L = list(tos)

#L[0] = 1000
#print L[0]

#db10 = bytearray(L)

#db10 = pack('>'+'h'*(len(L)),*L)

#print (db10)

#change value in db10
#db[0] = 1

#plc.db_write(10,0,db10)

#db2 = db_read(10,0,2)
#print(db2[0])

plc.disconnect()


