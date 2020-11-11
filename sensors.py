# EE 250 Final Project
# By: Zechen Wang
# Date: 11/11/2020

import sys
import time
import math
import threading

sys.path.append('./Software/Python/') # Please modify this line to your grovepi library's path

import grovepi
import sendInflux   # sendInflux.py includes the functions needed to transmit data to InfluxDB

if __name__ == '__main__':
    UR = 4      # Ultrasonic ranger, D4
    DHT = 3     # humidity and temp sensor, D3
    LIGHT = 0   # light sensor, A0

    grovepi.pinMode(LIGHT,"INPUT")
    lock = threading.Lock() # use lock to prevent I2C race

    while True:

        try:

            #read ultrasonic ranger
            dist = 0;
            for i in range(1,6):    
                with lock: 
                    get_dist = grovepi.ultrasonicRead(UR)
                    time.sleep(0.2)
                dist += get_dist; 

            dist /= 5;  #average on 5 polls


            print("Distance:" + str(dist))

            #read humidity&temp sensor
            with lock:  
                [temp,humidity] = grovepi.dht(DHT,0)
                time.sleep(0.2)
  
            if math.isnan(temp) == False and math.isnan(humidity) == False:
                print("temp : %.02f C \nhumidity :%.02f%%"%(temp, humidity))
         
            #read light sensor
            with lock:
                light_value = grovepi.analogRead(LIGHT)
                time.sleep(0.2)
            print("Light:" + str(light_value))

        except IOError:
            print ("Error")

        #send data to influxdb
        sendInflux.send('Temperature',temp)
        sendInflux.send('Humidity',humidity)
        sendInflux.send('Light',light_value)
        sendInflux.send('Distance',dist)

        #measures every 10 seconds
        time.sleep(10)