#Author: 10v
#Purpose:  With this code, we are going to show lines of text on the lcd display using python libraries.

#import the necessary libraries.
import time
import lcddriver

disp = lcddriver.lcd()

#Begin the while true block, this will run the program indefinitely till a key is pressed
try:
    while True:
        print("Printing message to LCD Display") # Display message on your terminal
        disp.lcd_display_string("What's up?",1) # Display message on your LCD on Line #1
        disp.lcd_display_string("10v's Tutorials",2) # Display message on your LCD on Line #2
        time.sleep(3) # Delay of 3 seconds
        disp.lcd_display_string("Happy Pi Programming",1) # Display message on your LCD on Line #1
        time.sleep(3) # Delay of 3 seconds
        disp.lcd_clear() # Clear the LCD screen
        time.sleep(3) # Delay of 3 seconds

except KeyboardInterrupt: # When any key is pressed, it interrupts the program
    print("Bye Bye!")  #Display departing message on terminal
    disp.lcd_clear () #Make sure you clear the display screen when program is exiting.
