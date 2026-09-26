from keyboard import hook, unhook, wait



def simple_printer(event):
    print(event.name, event.scan_code, event.time, event.event_type)
hook(simple_printer)



wait('enter')
unhook(simple_printer)





