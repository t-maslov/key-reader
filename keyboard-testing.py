from keyboard import hook, unhook, wait
from tkinter import *
from tkinter import ttk

def keyboard_processor(event):
    last_key_press.set(' '.join(tuple(map(str, (event.name, event.scan_code, event.time, event.event_type)))))
    if event.event_type == 'down' and event.name not in currently_held_keys:
        currently_held_keys.append(event.name)
    elif event.event_type == 'up' and event.name in currently_held_keys:
        currently_held_keys.remove(event.name)
    currently_held_keys_label.set(str(currently_held_keys))
    

        
hook(keyboard_processor)

currently_held_keys = []

root = Tk()
root.title("Keyboard press")
mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

last_key_press = StringVar()
ttk.Label(mainframe, textvariable=last_key_press).grid(column=0, row=0, sticky=(W, E))
currently_held_keys_label = StringVar()
ttk.Label(mainframe, textvariable=currently_held_keys_label).grid(column=0, row=1, sticky=(W, E))

root.mainloop()
wait('enter')
unhook(keyboard_processor)





