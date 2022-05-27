from tkinter import *

def start_loop():
    loop_invoer = invoer.get()
    if(loop_invoer != ""): #controleer of de invoer niet leeg is
        loop_invoer = int(invoer.get())
        print(loop_invoer)
        for i in range(loop_invoer):
            ser.write(b'H')
            time.sleep(1)
            ser.write(b'L')
            time.sleep(1)
    else:
        print("geen aantal ingevoerd")

OPTIONS = [
"1",
"2"
] #etc

master = Tk()

frame1=Frame(master)

variable = StringVar(master)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(master, variable, *OPTIONS)
w.pack()

def ok():
    print ("value is:" + variable.get())

button = Button(master, text="Start", command=ok)
label = Label(frame1, text="Vul aantal keer in:")
invoer = Entry(frame1, width=10)
button.pack()
label.pack()
invoer2.pack(side=RIGHT, padx=20, pady=20)

mainloop()