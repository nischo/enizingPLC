from enizingSensor import enizingSensor
import random
from connection import *
from db_layout import *
import time


#define sensors
case        = enizingSensor.enizingSensor("Id","key")
controller  = enizingSensor.enizingSensor("Id","key")
drive       = enizingSensor.enizingSensor("Id","key")
inlet       = enizingSensor.enizingSensor("Id","key")
outlet      = enizingSensor.enizingSensor("Id","key")

#defining plc connection data
plcIP = "10.7.14.92"
plcRack = 0
plcSlot = 2

#connect to PLC
plc = conectPLC(plcIP,plcRack,plcSlot)

#return true if plc is connected
connected = plc.get_connected()

#check if connection is established
if connected:
    print('plc is connected')
else:
    print('plc is not connected')

i = 0

while i < 100:
    #download DB80 from PLC to PC
    all_data = plc.upload(80)
    db80 = snap7.util.DB(80,all_data,db_layout,96,32)
    #print(db80[0])

    #download DB81 from PLC to PC
    all_data = plc.upload(81)
    db81 = snap7.util.DB(80,all_data,db_layout_output,20,10)
    #print[db81[0]]

    #defining testdate 
    caseValues = {}
    controllerValues = {}
    driveValues ={}
    inletValues = {}
    outletValues = {}

    #setting pressure data
    caseValues["pressure"] = random.randint(0,100)
    inletValues["pressure"] = random.randint(350,400)
    outletValues["pressure"] = random.randint(350,400)

    #setting temperature data
    caseValues["temperature"] = db80[0]['INT_FORMAT.TEMP_VERSORGUNG']
    inletValues["temperature"] = db80[0]['REAL_FORMAT.TEMP_VERSORGUNG']
    driveValues["temperature"] = 45

    #setting flow
    outletValues["flow"] = 10

    controllerValues["setpoint"] = db81[0]['DRUCKSOLLWERT_TST2']
    controllerValues["actual_value"] = random.randint(20,70)
    controllerValues["status"] = True
    controllerValues["running_hours"] = 1 + i

    driveValues["speed"] = random.randint(1000,1440)
    driveValues["power"] = random.randint(800,1200)
    driveValues["vibration"] = random.randint(0,100) / 100

    i += 1

    #send date to enizing
    caseResponse =  case.send_csv(caseValues)
    controllerResponse = controller.send_csv(controllerValues)
    driveResponse = drive.send_csv(driveValues)
    inletResponse = inlet.send_csv(inletValues)
    outletResponse = outlet.send_csv(outletValues)

    print(caseResponse)
    print(controllerResponse)
    print(driveResponse)
    print(inletResponse)
    print(outletResponse)
    time.sleep(15)

plc.disconnect()