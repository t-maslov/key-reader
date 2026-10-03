from keyboard import hook, unhook, wait
from tkinter import *
from tkinter import ttk

def simple_printer(event):
    last_key_press.set(' '.join(tuple(map(str, (event.name, event.scan_code, event.time, event.event_type)))))

hook(simple_printer)

root = Tk()
root.title("Keyboard press")
mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
last_key_press = StringVar()
ttk.Label(mainframe, textvariable=last_key_press).grid(column=0, row=0, sticky=(W, E))

root.mainloop()
wait('enter')
unhook(simple_printer)





