from lib2to3.pgen2.token import OP
from ssl import Options
from tkinter import *
import serial
import time
from functools import partial

master = Tk()
variable_aantal= IntVar(master)
variable_aantal.set(0)
kwaliteit_dict={}
variable_kwaliteit= {}
delaytime = 100

def start():
    print("kwaliteit is:" + variable_kwaliteit.get())
    
def stop():
    print("Stop")
    
def reset():
    print("reset")

def option_change(event=None):
    print("value is: " + str(variable_aantal.get()))
    #TODO: When a different option is selected
    #clear dictionary (clear/pop) doesn't work (yet)
    #otherwise substract new value from old value
    #and remove the result (number) from the end of the dictionary
    for key in kwaliteit_dict:
             kwaliteit_dict[key].destroy()
    
    kwaliteit_dict.clear()
        
    for x in range(variable_aantal.get()):
        print(x)
        variable_kwaliteit[x] = IntVar(master)
        kwaliteit_dict[x] = OptionMenu(frame, variable_kwaliteit[x], *OPTIONS_KWALITEIT,command=partial(option_kwaliteit_change, x))
        kwaliteit_dict[x].grid(row=x +6, column=3)

def option_kwaliteit_change(i, event=None):
    print(variable_kwaliteit)
    
def after():
    
    master.after(100, after)
                   
#variable_aantal.set(0) # default value
#variable_kwaliteit.set("Selecteer kwaliteit...") # default value

OPTIONS_AANTAL = [1,2,3,4]
OPTIONS_KWALITEIT = [1,2,3,4]

frame = Frame(master)
frame.grid(row=5, column=5)

button_start = Button(frame, text="Start", command=start)
button_stop = Button(frame, text="Stop", command=stop)
button_reset = Button(frame, text="Reset", command=reset)

button_start.grid(row=0, column=0)
button_stop.grid(row=0, column=5)
button_reset.grid(row=0, column=3)

popupmenu=OptionMenu(frame, variable_aantal, *OPTIONS_AANTAL, command=option_change)
popupmenu.grid(row=3, column=3)
                      
Label(frame, text="Selecteer aantal...").grid(row=2, column=3)
Label(frame, text="Selecteer kwaliteit...").grid(row=4, column=3)


master.after(100, after)
master.mainloop()