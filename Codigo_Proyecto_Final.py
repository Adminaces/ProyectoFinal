#Codigo Proyecto Final 
#AdminAces

#!/usr/bin/env python
#
# GrovePi Project for a Weather Station project.
#   *   Reads the data from light, temperature and humidity sensor 
#       and takes pictures from the Pi camera periodically and logs them
#       coming soon:  reading atmospheric pressure(BMP180)
#   *   Sensor Connections on the GrovePi:
#           -> Grove light sensor                       - Port A2
#           -> Grove Temperature and Humidity sensor    - Port D4
#           -> Raspberry Pi Camera
#           -> Grove Pressure sensor (BMP 180)          - Any I2C port, I2C-1, I2C-2, or I2C-3.

#
# NOTES:
#   *   Make sure that the Pi camera is enabled and working. You can see detailed directions here: https://www.raspberrypi.org/help/camera-module-setup/
#   *   The GrovePi connects the Raspberry Pi and Grove sensors.  You can learn more about GrovePi here:  http://www.dexterindustries.com/GrovePi
#   *   Have a question about this example?  Ask on the forums here:  http://forum.dexterindustries.com/c/grovepi
#
'''
## License

The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2017  Dexter Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

#################################################################
import time
import grovepi
import subprocess
import math
from grove_rgb_lcd import *
from datetime import datetime
# import picamera
from grove_i2c_barometic_sensor_BMP180 import BMP085
#################################################################
## File Location

log_file="/home/pi/Desktop/weather_station_log.csv"     # This is the name of the file we will save data to.
                                                        # This is hard coded to the Desktop.

#################################################################
  
def truncate(number:float, max_decimals:int) -> float:
    int_part, dec_part = str(number).split(".")
    return float(".".join((int_part,dec_part[:max_decimals])))
  
                                                        
                                                        
## Sensors
light_sensor            = 0    #Light Sensor Port Number
temp_humidity_sensor    = 4     #Temperature sensor Port Number

#potencimeter
potenciometer = 2

blue=0
therm_version = blue            
# setting the backlight color once reduces the amount of data transfer over the I2C line
setRGB(255,255,255)


#################################################################
# Timings
# You can adjust the frequency of the operations here:  how frequently the sensors are read,
# how frequently the data is written to csv, and how frequently pictures are taken.

resp = 0  



# Timings
#################################################################


#Read the data from the sensors.
def read_sensor():
    try:
        

        light=grovepi.analogRead(light_sensor)
        [temp,humidity] = grovepi.dht(temp_humidity_sensor,therm_version)   # Here we're using the thermometer version.
        #Return -1 in case of bad temp/humidity sensor reading
        if math.isnan(temp) or math.isnan(humidity):        #temp/humidity sensor sometimes gives nan
            return [-1,-1,-1,-1]
            #return [-1,-1,-1]
        return [light,temp,humidity]
        #return [light,temp,humidity]
    
    #Return -1 in case of sensor error
    except (IOError,TypeError) as e:
            # return [-1,-1,-1]
            return [-1,-1,-1,-1]



#Save the initial time, we will use this to find out when it is time to take a picture or save a reading
last_read_sensor= int(time.time())

# Main Loop
while True:
    resp = (grovepi.analogRead(potenciometer)//255.75)+ 1
    tiempo_actual = datetime.now()
    current_time = int(time.time())
    [light,temp,humidity]=read_sensor()
    light //= 80
    # If any reading is a bad reading, skip the loop and try again
    if light==-1:
        print("Bad reading")
        time.sleep(1)
        continue
    curr_time = time.strftime("%Y-%m-%d:%H-%M-%S")
    print(("Time:%s\nLight: %d\nTemp: %.2fC\nHumidity: %d \n" %(tiempo_actual,light,temp,humidity)))

    # If it is time to take the sensor reading
    if current_time-last_read_sensor>resp:
        # Save the sensor reading to the CSV file
        print("Save the sensor reading to the CSV file.")
        f=open(log_file,'a')
        f.write("%s,%.2f,%.2f,%d;\n" %(str(tiempo_actual),light,temp,humidity))
        f.close()
        
        #Update the last read time
        last_read_sensor=current_time
    setText_norefresh("T:" + str(truncate(temp,0)) + "c  L:" + str(light)+"lm  H:" + str(truncate(humidity,0)) +"% Ts:"+str(truncate(resp,0)))

    time.sleep(1)