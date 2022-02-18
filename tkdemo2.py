#!/usr/bin/env python      
import tkinter as tk       

class Application(tk.Frame):              
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)   
        self.grid()                       
        self.createWidgets()

    def createWidgets(self):
        username_label = tk.Label(self, text="Username")
        username_label.grid(row=0, column=0)
        email_label = tk.Label(self, text="Email")
        email_label.grid(row=0, column=1)
        join_date_label = tk.Label(self, text="Join date")
        join_date_label.grid(row=0, column=2)
        group_label = tk.Label(self, text="Group")
        group_label.grid(row=0, column=3)
        institution_label = tk.Label(self, text="Institution")
        institution_label.grid(row=0, column=4)
        for i in range(1, 10):
            for j in range(5):
                if j < 4:
                    cell = tk.Entry(self, text="", state=tk.DISABLED, disabledbackground="white")
                    cell.grid(row=i, column=j)      
                else:
                    cell = tk.Entry(self, text="")
                    cell.grid(row=i, column=j)       

app = Application()                       
app.master.title('User Report')    
app.mainloop()                   