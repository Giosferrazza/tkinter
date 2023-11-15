from tkinter import *

window = Tk() # Create a root window
window.title("WindChill Calculator")
window.geometry("300x100")


class WindChill():
    def __init__(self, parent):
        self.parent = parent

        self.temp = StringVar()
        self.velocity = StringVar()

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
        scale = Scale(window, orient=HORIZONTAL, from_=0, to=50, activebackground="green", variable=self.velocity, command=self.velocityPrint)
        scale.grid(row=2, column=1)

    def setWindChill(self):
        wind_chill = Label(window, text="Wind Chill: ")
        wind_chill.grid(row=3, column=1)
        display = Label(window, text="0")
        display.grid(row=3, column=2)


    def calWindChill(self, event, temp, velocity):
        floatVelocity = float(velocity)
        floatTemp = float(temp)
        wind_chill = 35.74 + 0.6215 * floatTemp - 35.75 * (floatVelocity ** 0.16) + 0.4275 * floatTemp * (floatVelocity ** 0.16)
        label = Label(window, text=wind_chill)

    def tempPrint(self, event):
        print(self.temp.get())

    def velocityPrint(self, event):
        print(self.velocity.get())


def main():   
    WindChill(window)

    window.mainloop() # Create an event loop

if __name__ == '__main__':
    main()
