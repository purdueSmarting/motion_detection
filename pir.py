import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
 
GPIO.setup(PIR_PIN, GPIO.IN)

motionless_time = 0
test_time = 30
num = 0
 
try:
    print("PIR Module Test (CTRL+C to exit)")
    time.sleep(2)
    print("Ready")
     
    while True:
        if GPIO.input(PIR_PIN):
            motionless_time = 0
            num = 0
            
            t = time.localtime()
            print("%d:%d:%d Motion Detected!" % (t.tm_hour, t.tm_min, t.tm_sec))
        else:
            motionless_time += 1

            if motionless_time != 0 and motionless_time%test_time == 0:
                num += 1
                print("not detected any movement during %d sec!" % (test_time*num))

                # TODO : POST request

                
        time.sleep(1)
 
except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
