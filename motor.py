# Import the RPi.GPIO library for Raspberry Pi GPIO control
import RPi.GPIO as GPIO
# Import the sleep function from the time module
from time import sleep

# Define the GPIO pins for the motor inputs and enable pin
input1 = 24
input2 = 23
en = 25
temp1 = 1  # A variable to store the motor direction

# Set the GPIO mode to use the BCM numbering scheme
GPIO.setmode(GPIO.BCM)
# Set up the GPIO pins as outputs
GPIO.setup(input1, GPIO.OUT)
GPIO.setup(input2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
# Set the initial states of the motor inputs to LOW
GPIO.output(input1, GPIO.LOW)
GPIO.output(input2, GPIO.LOW)

# Create a PWM (Pulse Width Modulation) object on the enable pin
p = GPIO.PWM(en, 1000)
# Start the PWM with a duty cycle of 25%
p.start(25)

# Print initial messages to the console
print("\n")
print("The default speed & direction of the motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")

# Enter an infinite loop to control the motor based on user input
while True:
    x = input()  # Read user input
    
    # Check user input and control the motor accordingly
    if x == 'r':
        print("run")
        if temp1 == 1:
            GPIO.output(input1, GPIO.HIGH)
            GPIO.output(input2, GPIO.LOW)
            print("forward")
            x = 'z'
        else:
            GPIO.output(input1, GPIO.LOW)
            GPIO.output(input2, GPIO.HIGH)
            print("backward")
            x = 'z'
    
    elif x == 's':
        print("stop")
        GPIO.output(input1, GPIO.LOW)
        GPIO.output(input2, GPIO.LOW)
        x = 'z'
    
    elif x == 'f':
        print("forward")
        GPIO.output(input1, GPIO.HIGH)
        GPIO.output(input2, GPIO.LOW)
        temp1 = 1
        x = 'z'
    
    elif x == 'b':
        print("backward")
        GPIO.output(input1, GPIO.LOW)
        GPIO.output(input2, GPIO.HIGH)
        temp1 = 0
        x = 'z'
    
    elif x == 'l':
        print("low")
        p.ChangeDutyCycle(25)
        x = 'z'
    
    elif x == 'm':
        print("medium")
        p.ChangeDutyCycle(50)
        x = 'z'
    
    elif x == 'h':
        print("high")
        p.ChangeDutyCycle(75)
        x = 'z'
    
    elif x == 'e':
        # Cleanup GPIO and exit the program when 'e' is entered
        GPIO.cleanup()
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
