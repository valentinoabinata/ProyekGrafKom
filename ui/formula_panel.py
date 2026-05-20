
from tkinter import *
from tkinter.scrolledtext import ScrolledText

class FormulaPanel(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        Label(self,text="FORMULA PANEL",font=("Arial",11,"bold")).pack()
        self.text = ScrolledText(self,width=40,height=35)
        self.text.pack(fill="both", expand=True)

    def update_formula(self, text):
        self.text.delete("1.0",END)
        self.text.insert(END,text)
