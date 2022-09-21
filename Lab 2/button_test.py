from __future__ import print_function
import qwiic_button
import time
import sys

brightness = 250    # The maximum brightness of the pulsing LED. Can be between 0 and 255
cycle_time = 1000    # The total time for the pulse to take. Set to a bigger number for a slower pulse or a smaller number for a faster pulse
off_time = 200       # The total time to stay off between pulses. Set to 0 to be pulsing continuously.

def run_example():

    print("\nSparkFun Qwiic Button Example 3")
    my_button = qwiic_button.QwiicButton()

    if my_button.begin() == False:
        print("\nThe Qwiic Button isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return
    
    print("\nButton ready!")

    my_button.LED_off()

    while True:
        
        if my_button.is_button_pressed() == True:

            print("\nThe button is pressed!")
            my_button.LED_config(brightness, cycle_time, off_time)
        
        else:
            print("\nThe button is not pressed.")
            my_button.LED_off()
        
        time.sleep(0.1)    # Let's not hammer too hard on the I2C bus

if __name__ == '__main__':
    try:
        run_example()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 3")
        sys.exit(0)