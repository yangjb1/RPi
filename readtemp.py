import os
import time
from datetime import datetime

def measure_temp():
        temp = os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline()
	temp = float(temp)/1000
	tempC = str(temp)
	tempF = str(temp*9/5+32)
        return ("Fahrenheit: " + tempF + " Celsius: " + tempC)

f = open("record.txt",'a+')
f.write('\n')
while True:
	time_=str(datetime.now())
	print(time_ + ' ' + measure_temp())
	f.write(time_ + ' ' + measure_temp()+'\n')
	f.flush()
        time.sleep(300)
