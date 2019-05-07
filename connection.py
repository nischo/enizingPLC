import snap7
import snap7.util

def conectPLC(plcIP,plcRack,plcSlot):
    #connection to plc
    plc = snap7.client.Client()
    plc.connect(plcIP,plcRack,plcSlot)
    
    return plc