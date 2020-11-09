import sys
import time

sys.path.append('./Software/Python/')
sys.path.append('./Software/Python/grove_rgb_lcd')

import grovepi
import grove_rgb_lcd as lcd

if __name__ == '__main__':
    PORT = 4    # D4
    meter = 0   # A0
    lcd.setRGB(153,255,51)

    grovepi.pinMode(meter, "INPUT")

    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        time.sleep(0.2)

        deg = round( grovepi.analogRead(meter) * 300 / 1023) #range: [0,300]
        print("Rot Sensor:" + str(deg))

        dist = grovepi.ultrasonicRead(PORT)
        print("Distance:" + str(dist))
        
        if dist < deg:
            lcd.setText_norefresh("%3dcm OBJ PRES\n%3dcm" % (deg,dist))
        else:
            lcd.setText_norefresh("%3dcm          \n%3dcm" % (deg,dist))