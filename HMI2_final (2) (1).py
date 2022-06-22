from lib2to3.pgen2.token import OP
from ssl import Options
from tkinter import *
import serial
import time
from functools import partial

try:
    ser = serial.Serial('COM6', 9600) #set com port, set BAUD-rate
except:
    ser = serial.Serial() #Geen seriële verbinding
    print("Geen seriële verbinding beschikbaar op COMX")

master = Tk()
variable_aantal= StringVar()
kwaliteit_dict={}
variable_kwaliteit= {}

options_kwaliteit = [1,2,3,4]

def start_loop(var, index, mode):
    inputValue = variable_aantal.get()
    if inputValue:
        loop_invoer = int(inputValue)
        print(loop_invoer)
        for i in range(loop_invoer):
            variable_kwaliteit[i] = IntVar(master)
            kwaliteit_dict[i] = OptionMenu(frame, variable_kwaliteit[i], *options_kwaliteit,command=partial(option_kwaliteit_change, i))
            kwaliteit_dict[i].grid(row=i +6, column=3)
    else:
        loop_invoer = None
        for x in kwaliteit_dict:
            kwaliteit_dict[x].destroy()
    time.sleep(1)

def start():
    for key, value in variable_kwaliteit.items():
        print("key",key)
        print("Value",value.get())
        ser.write((str(value.get())+"\n").encode())
    print("start")
   
def stop():
    print("S")
    ser.write(("Stop"+"\n").encode())
    
def reset():
    print("reset")

def option_change(event=None):
    print("value is: " + str(variable_aantal.get()))
    for key in kwaliteit_dict:
             kwaliteit_dict[key].destroy()
    kwaliteit_dict.clear()

def option_kwaliteit_change(i, event=None):
    print(variable_kwaliteit)
    
def aa():
    print("quit")
    ser.close()
    master.destroy()

frame = Frame(master)
frame_textvak = Frame(master)
frame.pack(side=LEFT)
frame_textvak.pack(side=RIGHT)

button_start = Button(frame, text="Start", command=start)
button_stop = Button(frame, text="Stop", command=stop)
button_reset = Button(frame, text="Reset", command=reset)

button_start.grid(row=0, column=0)
button_stop.grid(row=0, column=5)
button_reset.grid(row=0, column=3)

variable_aantal.trace_variable("w", start_loop)
e = Entry(frame, textvariable=variable_aantal)
e.grid(row=3, column=3)
     
Label(frame, text="Selecteer aantal...").grid(row=2, column=3)
Label(frame, text="Selecteer kwaliteit...").grid(row=4, column=3)

text_vak = Text(frame_textvak, height = 20, width = 20)
text_vak.grid(row=5, column=7)

def text_vakupdate():
    if ser.in_waiting > 0:
        try:
            gegeven = ser.readline().decode().strip()
        except UnicodeDecodeError:
            print("kon text niet aflezen")
            master.after(20, text_vakupdate)
            return
        text_vak.insert('1.0', gegeven)
    master.after(20, text_vakupdate)

master.after(20, text_vakupdate)
master.protocol("WM_DELETE_MASTER", aa)
master.mainloop()