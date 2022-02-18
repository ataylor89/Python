#!/usr/bin/env python      
import tkinter as tk       

class Application(tk.Frame):              
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)   
        self.grid()                       
        self.createWidgets()

    def createWidgets(self):
        rows = 5
        cols = 5
        for i in range(rows):
            for j in range(cols):
                cell = tk.Entry(self, text="")
                cell.grid(row=i, column=j)       

app = Application()                       
app.master.title('Sample application')    
app.mainloop()                   