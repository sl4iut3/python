

from Tkinter import *

def callback():
    global e
    print e.get()
    
master = Tk()

e = Entry(master)
#e.pack()

#e.focus_set()



b = Button(master, text="get", width=10, command=callback)
b.pack()

##e = Entry(master, width=50)
##e.pack()
##
##text = e.get()
##def makeentry(parent, caption, width=None, **options):
##    Label(parent, text=caption).pack(side=LEFT)
##    entry = Entry(parent, **options)
##    if width:
##        entry.config(width=width)
##    entry.pack(side=LEFT)
##    return entry
##
##user = makeentry(parent, "User name:", 10)
##password = makeentry(parent, "Password:", 10, show="*")
##content = StringVar()
##entry = Entry(parent, text=caption, textvariable=content)
##
##text = content.get()
##content.set(text)

mainloop()
