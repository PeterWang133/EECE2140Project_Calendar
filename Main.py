import tkinter as tk
from object.c_eventlibrary import EventLibrary
from gui.c_main_menu import HomeScreen

events = EventLibrary()

root = tk.Tk()
h = HomeScreen(root,events)

#https://zoom.us/

root.mainloop()
