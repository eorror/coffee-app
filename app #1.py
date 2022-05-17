#coffee app v1

#import
from cgitb import text
from curses import window
from email.mime import image
import imghdr
from telnetlib import LOGOUT
import tkinter as tk
from tkinter import StringVar, simpledialog
import tkinter.ttk as ttk
from tkinter import Frame, Image, PhotoImage, font as tkfont
import time
from turtle import bgcolor, width, window_height, window_width
from unicodedata import name
from webbrowser import get

from setuptools import Command


#class def

class MainFrame(tk.Tk):
    #frame object holding all the pages
    #controller of the pages
    def __init__(self, *args, **kwargs) :
        tk.Tk.__init__(self, *args, **kwargs)

        
        #window size
        window_width = 390
        window_height = 844

        

        OffsetLeft = int((self.winfo_screenwidth() - window_width) / 2)
        OffsetTop = int((self.winfo_screenheight() - window_height) / 2)

        self.geometry('{}x{}+{}+{}'.format(window_width, window_height, OffsetLeft, OffsetTop))

        self.minsize(300, 754)

        self.titlefont = tkfont.Font(family = "Bely Display", size = 50)

        



        container = tk.Frame(self, width = 390, height= 844)
        container.config(background='#815940')
        container.grid(row = 0, column = 0, sticky = "nesw")
        container.grid_propagate(0)

        self.id = tk.StringVar()
        self.name = name


        
        self.listing = {} #holding 2 arguments 

        for p in (WelcomePage, info, fw, moc, lat, cap):
            page_name = p.__name__
            frame = p(parent = container, controller = self)
            frame.grid(row=0, column=0, sticky="nsew")
            self.listing[page_name] = frame
        
        self.up_frame('WelcomePage')
    


    def up_frame(self, page_name) :
        page = self.listing[page_name]
        page.tkraise()



class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id

        self.configure(background="#815940")


        
        logo = tk.Button(self, fg = 'black', highlightbackground='#4A3223', text = "Ros Coffee", 
        font = controller.titlefont, command= lambda: controller.up_frame("info"))
        logo.pack(padx= 60, pady= 300)

    

class info(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id

        self.configure(background="#815940")

        name = StringVar()


        logo = tk.Label(self, fg = 'black', font = controller.titlefont, background='#815940', text = "Ros Coffee")
        logo.grid(padx= 30, pady= 100)

        name_label = tk.Label(self, text = 'add your name', background='#815940', font=('calibre',10, 'bold'))

        name_label.grid(padx= 120, pady = 1)

        name_entry = tk.Entry(self, textvariable= name,  font=('bely',10,'normal'))


        name_entry.grid(padx= 130, pady= 1)

        sub_btn=tk.Button(self, text = 'continue', highlightbackground='#4A3223', 
        command = lambda: controller.up_frame("fw"))

        print("welcome ", name)

        sub_btn.grid(padx= 150, pady= 5)




class fw(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id
        
        self.configure(background="#815940")

        name = self.name.get()


        welcome = tk.Label(self, text = "welcome, " + controller.name.get())

        welcome.pack(padx= 30)

        Label = tk.Label(self, text= "flat white", background='#815940', font = controller.titlefont)

        Label.pack()

        fw = tk.Button(self, text = "fw", command= lambda: controller.up_frame("fw"))
        fw.pack()

        moc = tk.Button(self, text = "moc", command= lambda: controller.up_frame("moc"))
        moc.pack()

        lat = tk.Button(self, text = "lat", command= lambda: controller.up_frame("lat"))
        lat.pack()

        cap = tk.Button(self, text = "cap", command= lambda: controller.up_frame("cap"))
        cap.pack()


class moc(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id
        
        self.configure(background="#815940")

        Label = tk.Label(self, text= "mocha", font = controller.titlefont)

        Label.pack()

        fw = tk.Button(self, text = "fw", command= lambda: controller.up_frame("fw"))
        fw.pack()

        moc = tk.Button(self, text = "moc", command= lambda: controller.up_frame("moc"))
        moc.pack()

        lat = tk.Button(self, text = "lat", command= lambda: controller.up_frame("lat"))
        lat.pack()

        cap = tk.Button(self, text = "cap", command= lambda: controller.up_frame("cap"))
        cap.pack()


class lat(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id
        
        self.configure(background="#815940")

        Label = tk.Label(self, text= "Latte", font = controller.titlefont)

        Label.pack()

        fw = tk.Button(self, text = "fw", command= lambda: controller.up_frame("fw"))
        fw.pack()

        moc = tk.Button(self, text = "moc", command= lambda: controller.up_frame("moc"))
        moc.pack()

        lat = tk.Button(self, text = "lat", command= lambda: controller.up_frame("lat"))
        lat.pack()

        cap = tk.Button(self, text = "cap", command= lambda: controller.up_frame("cap"))
        cap.pack()

class cap(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id
        
        self.configure(background="#815940")

        Label = tk.Label(self, text= "Cappucino", font = controller.titlefont)

        Label.pack()

        fw = tk.Button(self, text = "fw", command= lambda: controller.up_frame("fw"))
        fw.pack()

        moc = tk.Button(self, text = "moc", command= lambda: controller.up_frame("moc"))
        moc.pack()

        lat = tk.Button(self, text = "lat", command= lambda: controller.up_frame("lat"))
        lat.pack()

        cap = tk.Button(self, text = "cap", command= lambda: controller.up_frame("cap"))
        cap.pack()

if __name__ == '__main__':
    app = MainFrame()
    app.mainloop()



    














        
        

    


    


