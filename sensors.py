import sys
import time
import math
import threading

sys.path.append('./Software/Python/')
sys.path.append('./Software/Python/grove_rgb_lcd')

import grovepi
import grove_rgb_lcd as lcd

if __name__ == '__main__':
    UR = 4      # Ultrasonic ranger, D4
    DHT = 3     # humidity and temp sensor, D3
    LIGHT = 0   # light sensor, A0
    lcd.setRGB(153,255,51)

    grovepi.pinMode(LIGHT,"INPUT")
    lock = threading.Lock()

    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        time.sleep(0.2)

        try:
            with lock:
                print('lock aquired')
                dist = grovepi.ultrasonicRead(UR)
                time.sleep(0.2)
            print("Distance:" + str(dist))

            with lock:
                print('lock aquired')
                [temp,humidity] = grovepi.dht(DHT,0)
                time.sleep(0.2)
  
            if math.isnan(temp) == False and math.isnan(humidity) == False:
                print("temp = %.02f C humidity =%.02f%%"%(temp, humidity))
         
            with lock:
                print('lock aquired')
                light_value = grovepi.analogRead(LIGHT)
                time.sleep(0.2)
            print("Light:" + str(light_value))

        except IOError:
            print ("Error")

        lcd.setText_norefresh("dist = %3dcm \ntemp=%.02f hum=%.02f" % (dist,temp,humidity))
