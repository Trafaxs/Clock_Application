#use tkinter for ui
from tkinter import *
#import time will be the database of the codes
import time
#Message box for choices
from tkinter import ttk, messagebox
#importing playsound for the alarm lock
from playsound import playsound
#multiprocessing is a package that supports spawning processes using an API similar to the threading module. To do multistask
import multiprocessing
#for the dates and time
from datetime import datetime
from threading import *

# The Class: Alarm Clock._____________________________________
class Alarm_Clock:
    def __init__(self, root):
        #size of the main menu
        self.window = root
        self.window.geometry("680x420")
        self.window.title("Clock Application")
        root.configure(bg='#16213E')

        # Display the time in the main menu
        self.display = Label(self.window, font=('Cascadia Mono SemiBold', 34),
                             bg='#16213E', fg='yellow')
        self.display.place(x=100, y=150)
# Calling the the function.
        self.menu_time()
# Placing the set alarm button.
        button = Button(self.window,width=9, text="Set Alarm",
                            font=('Cascadia Mono SemiBold', 15), bg="#0F3460", fg="yellow",
                            command=self.another_window)
        button.place(x=270, y=250)
#direct to another window that contains the class Stopwatch code
        set_button2 = Button(text="Stopwatch",width=9, font=('Cascadia Mono SemiBold',15),bg="#0F3460", fg ="yellow",command=self.another_window1)
        set_button2.place(x=270,y=310)

# This function shows the current time in the main menu window.
    def menu_time(self):
        current = time.strftime('%H:%M:%S %p, %A')
        # Placing the time format level.
        self.display.config(text=current)
        self.display.after(100, self.menu_time)

# Another Window: This window will show, when the "Set Alarm" is pressed
#window design for the alarm
    def another_window(self):
        self.window_2 = Tk()
        self.window_2.title("Set Alarm")
        self.window_2.geometry("680x620")
        self.window_2.config(bg="#16213E")

        # Hour Text
        hours_label = Label(self.window_2, text="Hours",bg="#16213E",fg='yellow',
                            font=("times new roman", 20))
        hours_label.place(x=150, y=50)
        #  Minute text
        minute_label = Label(self.window_2, text="Minutes",bg="#16213E",fg='yellow',
                             font=("times new roman", 20))
        minute_label.place(x=275, y=50)
        # Hour message box design
        self.hours = StringVar()
        self.hours_b = ttk.Combobox(self.window_2,
                                    width=10, height=10, textvariable=self.hours,
                                    font=("times new roman", 15))
        self.hours_b['values'] = hours_list
        self.hours_b.current(0)
        self.hours_b.place(x=150, y=90)

        #Minute Box design.
        self.minutes = StringVar()
        self.minutes_b = ttk.Combobox(self.window_2,
                                      width=10, height=10, textvariable=self.minutes,
                                      font=("times new roman", 15))
        self.minutes_b['values'] = minutes_list
        self.minutes_b.current(0)
        self.minutes_b.place(x=275, y=90)

        # Ringtone Text.
        ringtone_label = Label(self.window_2, text="Ringtones",bg="#16213E",fg='yellow',
                               font=("times new roman", 20))
        ringtone_label.place(x=150, y=130)

        # Ringtone box to choose ringtones.
        self.ringtones = StringVar()
        self.ringtones_b = ttk.Combobox(self.window_2,
                                        width=15, height=10, textvariable=self.ringtones,
                                        font=("times new roman", 15))
        self.ringtones_b['values'] = ringtones_list
        self.ringtones_b.current(1)
        self.ringtones_b.place(x=150, y=170)

        # Title or Message Label.
        message = Label(self.window_2, text="Message",bg="#16213E",fg='yellow',
                              font=("times new roman", 20))
        message.place(x=150, y=210)

        # Message Entrybox: This Message will show, when the alarm is ringing.
        self.message = StringVar()
        self.message_entry = Entry(self.window_2,textvariable=self.message, font=("times new roman", 14), width=30)
        self.message_entry.insert(0, 'WAKE UP!!!')
        self.message_entry.place(x=150, y=250)


        # The Cancel Button: For cancel the alarm.
        cancel_b = Button(self.window_2,
                               text='Cancel', font=('Helvetica', 15), bg="red",
                               fg="black", command=self.window_2.destroy)
        cancel_b.place(x=390, y=300)

        # The Start Button: For set the alarm time
        start_b = Button(self.window_2, text='Start', \
                         font=('Helvetica', 15), bg="green", fg="white", command=self.Thread)
        start_b.place(x=490, y=300)

        self.window_2.mainloop()

        # calling the Test class for the stopwatch
    def another_window1(self):
            import Test
            Test.mainloop()

            self.another_window1().mainloop()


    # Creating a thread
    def Thread(self):
        x = Thread(target=self.set_time)
        x.start()

    # This function will run when the start button is selected in the main menu
    def set_time(self):
        alarm_time = f"{self.hours_b.get()}:{self.minutes_b.get()}"
        messagebox.showinfo("Alarm", f"Alarm is set for {alarm_time}")
        while True:
            # The current time is in 24 hour format
            current_time = datetime.now()
            # Converting the current time into hour and minute
            current_time_format = current_time.strftime("%H:%M")
            if current_time_format == alarm_time:
                process = multiprocessing.Process(target=playsound,
                                                  args=(ringtones_path[self.ringtones_b.get()],))
                process.start()
                #This messagebox will show, when the alarm is ringing.
                messagebox.showinfo("ALARM",f"{self.message_entry.get()} IT'S {alarm_time}")
                process.terminate()
                break

#hours in for the selection box.
hours_list = ['00', '01', '02', '03', '04', '05', '06', '07',
              '08', '09', '10', '11', '12', '13', '14', '15',
              '16', '17', '18', '19', '20', '21', '22', '23', '24']

#minutes in for the selection box.
minutes_list = ['00', '01', '02', '03', '04', '05', '06', '07',
                '08', '09', '10', '11', '12', '13', '14', '15',
                '16', '17', '18', '19', '20', '21', '22', '23',
                '24', '25', '26', '27', '28', '29', '30', '31',
                '32', '33', '34', '35', '36', '37', '38', '39',
                '40', '41', '42', '43', '44', '45', '46', '47',
                '48', '49', '50', '51', '52', '53', '54', '55',
                '56', '57', '58', '59']

# customed ringtones list to use for the selection box.
ringtones_list = ['Samsung', 'super_idol', 'bing_chilling','Giorno','Pillar_men']

# ringtone directory or pathway.
ringtones_path = {
    'Samsung': 'C:/Users/USER/PycharmProjects/Clock/Alarm_clock/Ringtones/Samsung.mp3',
    'super_idol': 'C:/Users/USER/PycharmProjects/Clock/Alarm_clock/Ringtones/super_idol.mp3',
    'bing_chilling': 'Ringtones/bing_chilling.mp3',
    'Giorno': 'C:/Users/USER/PycharmProjects/Clock/Alarm_clock/Ringtones/Giorno.mp3',
    'Pillar_men':'C:/Users/USER/PycharmProjects/Clock/Alarm_clock/Ringtones/Pillar_men.mp3',
}



root = Tk()
obj = Alarm_Clock(root),
root.mainloop()