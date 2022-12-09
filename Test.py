import tkinter
from tkinter import *



#class to start time from 0
class Stopwatch():

    def __init__(self,master=None):

        self.buttons()
        self.running = False
        self.timer = [00,00,00]
        self.timeString = str(self.timer[0]) + ':' + str(self.timer[1]) + ':' + str(self.timer[2])
        self.running_time()


    def buttons(self):
        self.time = Label(root, text="Stopwatch", bg="#0F3460", fg ="yellow")
        self.time.grid(row=0, column=0)

        self.start = Button(self.time, text='Start', command=self.start, bg="#0F3460", fg="yellow")
        self.start.grid(row=0, column=1)

        self.pause = Button(self.time, text='Pause', command=self.pause, bg="#0F3460", fg="yellow")
        self.pause.grid(row=1, column=1)

        self.reset = Button(self.time, text='Reset', command=self.resetTime, bg="#0F3460", fg ="yellow")
        self.reset.grid(row=2, column=1)

        self.display = Label(self.time, text='00:00:00', font=('Helvetica', 30), bg="#0F3460", fg ="yellow")
        self.display.grid(row=0, column=0)

        self.exit = Button(self.time, text='QUIT', command=self.quit, bg="#0F3460", fg ="yellow")
        self.exit.grid(row=3, column=1)


    def running_time(self):

        if (self.running == True):      #stopwatch
            self.timer[2] += 1

            if (self.timer[2] >= 100):
                self.timer[2] = 00
                self.timer[1] += 1

            if (self.timer[1] >= 60):
                self.timer[0] += 1
                self.timer[1] = 0

            self.timeString = str(self.timer[0]) + ':' + str(self.timer[1]) + ':' + str(self.timer[2])
            self.display.config(text=self.timeString)
        root.after(10, self.running_time)

    # Function to Start the clock
    def start(self):
        self.running = True


    # function to pause the clock
    def pause(self):
        self.running = False


    # function to reset the clock
    def resetTime(self):
        self.running = False
        self.timer = [0,0,0]
        self.display.config(text='00:00:00')

    # function to Quit the watch
    def quit(self):
        root.destroy()




root = tkinter.Tk()
up = Stopwatch(root)
