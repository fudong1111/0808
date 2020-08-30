
import os
import serial
from serial.tools.list_ports import comports

port_list= list(comports())

if len(port_list) == 0:
    print('Not found Serial Ports')
else:
    for i in range(len(port_list)):
        print(port_list[i])