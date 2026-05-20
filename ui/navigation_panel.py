
from tkinter import *

class NavigationPanel(Toplevel):
    def __init__(self,parent,canvas):
        super().__init__(parent)

        self.title("Navigasi Bangun")
        self.geometry("220x220")
        self.resizable(False,False)

        Label(
            self,
            text="NAVIGASI BANGUN",
            font=("Arial",10,"bold")
        ).grid(row=0,column=0,columnspan=3,pady=10)

        Button(
            self,text="↖",width=5,height=2,
            command=lambda:canvas.translate(-1,1)
        ).grid(row=1,column=0)

        Button(
            self,text="↑",width=5,height=2,
            command=lambda:canvas.translate(0,1)
        ).grid(row=1,column=1)

        Button(
            self,text="↗",width=5,height=2,
            command=lambda:canvas.translate(1,1)
        ).grid(row=1,column=2)

        Button(
            self,text="←",width=5,height=2,
            command=lambda:canvas.translate(-1,0)
        ).grid(row=2,column=0)

        Button(
            self,text="○",width=5,height=2,
            command=canvas.reset
        ).grid(row=2,column=1)

        Button(
            self,text="→",width=5,height=2,
            command=lambda:canvas.translate(1,0)
        ).grid(row=2,column=2)

        Button(
            self,text="↙",width=5,height=2,
            command=lambda:canvas.translate(-1,-1)
        ).grid(row=3,column=0)

        Button(
            self,text="↓",width=5,height=2,
            command=lambda:canvas.translate(0,-1)
        ).grid(row=3,column=1)

        Button(
            self,text="↘",width=5,height=2,
            command=lambda:canvas.translate(1,-1)
        ).grid(row=3,column=2)
