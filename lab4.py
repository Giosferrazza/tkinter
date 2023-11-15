"""
Lab4

Python WindChill Calculator

Created by Giovanni Sferrazza for cs202, T.M.C.C. 
Date: 11/25/2023
"""

from tkinter import *

window = Tk() # Create a root window
window.title("WindChill Calculator") # Title of the window
window.geometry("300x100") # Size of the window


class WindChill():
    def __init__(self, parent): # Constructor
        self.parent = parent # Parent is the root window

        self.temp = StringVar() # Create tkinter variables
        self.velocity = DoubleVar() 
        self.wind_chill = StringVar()

        self.velocity.set(0.0) # Set the default values
        self.temp.set(0)
        self.wind_chill.set(0.0)

        self.setTemperature()  # Create the GUI
        self.setWind()
        self.setWindChill()

    def setTemperature(self):
        label = Label(window, text = "Temperature:") #Create Temp
        entry = Entry(window, textvariable=self.temp) #Create a user input box
        label.grid(row=0, column=0) #Place the label and entry box
        entry.grid(row=0, column=1)
        entry.bind("<Leave>", self.calWindChill) #Bind the event to the entry box
        
        
    def setWind(self):
        wind_speed = Label(window, text="Wind Speed:")
        wind_speed.grid(row=2, column=0) #Create a scale for the wind speed
        scale = Scale(window, orient=HORIZONTAL, from_=0, to=50, activebackground="green", variable=self.velocity, command=self.calWindChill, resolution=0.1)
        scale.grid(row=2, column=1)   

    def calWindChill(self, event):
        if self.temp.get().isdecimal(): #Check if the input is a number
            floatVelocity = self.velocity.get() #Get the values from the entry box and scale
            floatTemp = float(self.temp.get())
            chill = 35.74 + 0.6215 * floatTemp - 35.75 * (floatVelocity ** 0.16) + 0.4275 * floatTemp * (floatVelocity ** 0.16) #Calculate the wind chill
            self.wind_chill.set(round(chill, 2))
        else:
            self.wind_chill.set("Invalid Input") # If the input is not a number, display an error message
    
    def setWindChill(self): # Create the wind chill label
        wind_chill = Label(window, text="Wind Chill: ")
        wind_chill.grid(row=3, column=0)
        display = Label(window, textvariable=self.wind_chill)
        display.grid(row=3, column=1)


def main(): # Main function
    WindChill(window) # Create an instance of the WindChill class
    window.mainloop() # Create an event loop

if __name__ == '__main__':
    main()
