# Libaries
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

#Disable warnings
GPIO.setwarnings(False)

## Hardware
greenLED = LED(14)
buzzer = 23
GPIO.setup(buzzer,GPIO.OUT)


## GUI
win = Tk()
win.title("Morse Code Converter")
headingFont = tkinter.font.Font(family = 'Helvetica', size = 25, weight = "bold")
canvas = Canvas(win, width = 400, height = 300)
canvas.pack()

## Functions

# Turn green LED on
def LEDon():
    greenLED.on()

# Turn green LED off
def LEDoff():
    greenLED.off()

# Turn buzzer on
def buzzerOn():
    GPIO.output(buzzer, GPIO.HIGH)
    
# Turn buzzer off    
def buzzerOff():
    GPIO.output(buzzer, GPIO.LOW)
    
# Method to turn buzzer and LED on for 500ms to show a dot    
def dot():
    LEDon()
    buzzerOn()
    sleep(0.5)
    LEDoff()
    buzzerOff()
    sleep(0.5)
    
# Method to turn buzzer and LED on for 1500ms to show a dash        
def dash():
    LEDon()
    buzzerOn()
    sleep(1.5)
    LEDoff()
    buzzerOff()
    sleep(0.5)
    
# Method to take a word and output morse code that corresponds
def letterSelection(word):
    i = 0 # set first letter as 0
    for letter in word: # loop through each letter in the word
        if i > 11: # once 12 characters have been completed exit the loop
            break
        # call dot and dash functions based on different letter and the
        # corresponding code
        elif letter.lower() == 'a':
            dot()
            dash()
        elif letter.lower() == 'b':
            dash()
            dot()
            dot()
            dot()
        elif letter.lower() == 'c':
            dash()
            dot()
            dash()
            dot()
        elif letter.lower() == 'd':
            dash()
            dot()
            dot()
        elif letter.lower() == 'e':
            dot()
        elif letter.lower() == 'f':
            dot()
            dot()
            dash()
            dot()
        elif letter.lower() == 'g':
            dash()
            dash()
            dot()
        elif letter.lower() == 'h':
            dot()
            dot()
            dot()
            dot()
        elif letter.lower() == 'i':
            dot()
            dot()
        elif letter.lower() == 'j':
            dot()
            dash()
            dash()
            dash()
        elif letter.lower() == 'k':
            dash()
            dot()
            dash()
        elif letter.lower() == 'l':
            dot()
            dash()
            dot()
            dot()
        elif letter.lower() == 'm':
            dash()
            dash()
        elif letter.lower() == 'n':
            dash()
            dot()
        elif letter.lower() == 'o':
            dash()
            dash()
            dash()
        elif letter.lower() == 'p':
            dot()
            dash()
            dash()
            dot()
        elif letter.lower() == 'q':
            dash()
            dash()
            dot()
            dash()
        elif letter.lower() == 'r':
            dot()
            dash()
            dot()
        elif letter.lower() == 's':
            dot()
            dot()
            dot()
        elif letter.lower() == 't':
            dash()
        elif letter.lower() == 'u':
            dot()
            dot()
            dash()
        elif letter.lower() == 'v':
            dot()
            dot()
            dot()
            dash()
        elif letter.lower() == 'w':
            dot()
            dash()
            dash()
        elif letter.lower() == 'x':
            dash()
            dot()
            dot()
            dash()
        elif letter.lower() == 'y':
            dash()
            dot()
            dash()
            dash()
        elif letter.lower() == 'z':
            dash()
            dash()
            dot()
            dot()
        elif letter == " ":
            sleep(2.5)
        
        i = i + 1 # increase the letter count
        sleep(1) # bettwen each letter 1.5 seconds is required, end of dot or dash has 0.5 delay
    
# Method that takes word from text box and passes to letter selection function
def convertToMorseCode():
    userText = textEntry.get() # gets text from the text box
    label = Label(win, text = userText) # assigning the text to label
    canvas.create_window(200, 230, window = label) # showing the text converted
    letterSelection(userText)
      

def close():
    GPIO.cleanup()
    win.destroy()

## Widgets
canvas.create_text(200, 60, font = headingFont, text = "Morse Code Converter")

canvas.create_text(200, 120, text = "Enter word to be converted (max. 12 characters, no numbers)")

textEntry = Entry(win, width = 30)
canvas.create_window(200, 140, window = textEntry)
    
convertToMorseCodeButton = Button(win, text = "Convert To Morse Code", command = convertToMorseCode, bg = '#d1ff9f', height = 2, width = 20)
canvas.create_window(200, 180, window = convertToMorseCodeButton)


win.protocol("WM_DELETE_WINDOW", close)

win.mainloop()
