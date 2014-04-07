import RPi.GPIO as GPIO
from time import sleep

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Boolean taking care of doing action only once on button press
current_button_state = False

try:
    while 1:
        if (GPIO.input(22) == 0):
            current_button_state = False

        else:
            if (current_button_state == False):
                # This will get triggered once when the button is pressed
                print "Poing"

            current_button_state = True

        # Don't continuously check for button changes, wait 100 ms
        sleep(0.1)

finally:
    # Avoid Port already in use errors when restarting the script
    GPIO.cleanup()
