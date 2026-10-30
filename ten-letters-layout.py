import tkinter as tk
from tkinter import *
from tkinter import ttk
from keyboard import hook, unhook, wait

class Application:
    def __init__(self, root):
        self.root = root
        self.bar_list = []
        self.bar_variables = [IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar()]

        self.label_list = []
        self.label_variables = [StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()]

        for bar_number in range(10):
            self.bar_list.append(ttk.Progressbar(root, orient="vertical", variable=self.bar_variables[bar_number], mode="determinate"))
            self.bar_list[bar_number].grid(row=0, column=bar_number*2, sticky="e")
            self.label_list.append(tk.Label(root, textvariable=self.label_variables[bar_number], font=("Helvetica", 8)))
            self.label_list[bar_number].grid(row=1, column=bar_number*2, sticky="e")
        for column in range(10):
            root.columnconfigure(column*2, minsize=6, weight=1)
            root.columnconfigure(column*2+1, minsize=8, weight=2)
        root.rowconfigure(0, minsize=158)
        root.rowconfigure(1, minsize=28)

        self.keys = dict()
        self.total_keys_pressed = 0
    def keyboard_update(self, event):
        if event.event_type == "down":
            if event.name not in self.keys:
                self.keys[event.name] = 0
            self.keys[event.name] += 1
            self.total_keys_pressed += 1
            sorted_values = tuple(sorted(self.keys.items(), key=lambda item: item[1], reverse=True))
            for bar_index in range(min(len(self.keys), 10)):
                self.bar_variables[bar_index].set(99.9*sorted_values[bar_index][1]/self.total_keys_pressed)
                self.label_variables[bar_index].set(sorted_values[bar_index][0])





if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    hook(app.keyboard_update)
    root.mainloop()
