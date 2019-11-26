#!/usr/bin/env python

import sys
import time
import datetime
import random 
import pi_ina3221

ina3221 = pi_ina3221.Pi_INA3221(addr=0x40)

while True:
    print("------------------------------")
    for channel in range(1,4):
  	busvoltage = ina3221.getBusVoltage_V(channel)
  	shuntvoltage = ina3221.getShuntVoltage_mV(channel)
  	current_mA = ina3221.getCurrent_mA(channel)  

  	loadvoltage = busvoltage + (shuntvoltage / 1000)
  
        print("Channel %d:" % channel)
  	print("Bus Voltage: %3.2f V " % busvoltage)
  	print("Shunt Voltage: %3.2f mV " % shuntvoltage)
  	print("Load Voltage: %3.2f V" % loadvoltage)
  	print("Current: %3.2f mA" % current_mA)
  	print
        
    time.sleep(1.0)
