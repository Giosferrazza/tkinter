from tkinter import *

window = Tk() # Create a root window
window.title("WindChill Calculator")
window.geometry("300x100")


class WindChill():
    def __init__(self, parent):
        self.parent = parent
        self.framePadx = 10
        self.framePady = 5
        self.temp = StringVar()


        self.setTemperature()
        self.setWind()
        self.setWindChill()

    def setTemperature(self):
        label = Label(window, text = "Temperature:") # Create Temp
        entry = Entry(window, textvariable=self.temp) #create a user input box
        label.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        entry.bind("<Leave>", self.tempPrint)

    def setWind(self):
        wind_speed = Label(window, text="Wind Speed:")
        wind_speed.grid(row=2, column=0)
        scale  = Scale(window, orient=HORIZONTAL, from_=0, to=50, activebackground="green")
        scale.grid(row=2, column=1)

    def setWindChill(self):
        wind_chill = Label(window, text="Wind Chill: ")
        wind_chill.grid(row=3, column=1)

    def calWindChill(self, event):
            print('hello')

    def tempPrint(self, event):
         print(self.temp.get())
        
def main():    
    temp = WindChill(window)
    
    window.mainloop() # Create an event loop

if __name__ == '__main__':
    main()
