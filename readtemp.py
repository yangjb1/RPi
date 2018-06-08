#!/usr/bin/python

import psutil
import os
import time
from datetime import datetime

def measure_temp():
        temp = os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline()
	temp = float(temp)/1000
	tempC = str("{0:.1f}".format(temp))
	tempF = str("{0:.1f}".format(temp*9/5+32))
        return ("Fahrenheit: " + tempF + " Celsius: " + tempC)

def cpu_usage():
	#return((os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()))
	#return((os.popen("htop | awk '/\R\ {print $2}'").readline().strip()))
	#cpu = (os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline())
	#print cpu
	return str(psutil.cpu_percent(interval=1))


f = open("/home/pi/record.txt",'a+')
f.write('\n')

while True:
	time_=str(datetime.now())
	#print(time_ + ' ' + measure_temp())
	f.write(time_ + ' ' + measure_temp()+ ' CPU%: ' + cpu_usage() + '\n')
	#f.write('CPU: ' + cpu_usage())
	f.flush()
        time.sleep(300)
