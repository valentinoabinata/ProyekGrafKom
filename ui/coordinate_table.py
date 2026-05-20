
from tkinter import *
from tkinter import ttk

class CoordinateTable(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.tree = ttk.Treeview(self, columns=("before","after"), show="headings", height=5)
        self.tree.heading("before", text="Koordinat")
        self.tree.heading("after", text="Hasil")
        self.tree.pack(fill="x")

    def update_table(self, before, after):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for b,a in zip(before,after):
            self.tree.insert("", "end", values=(str(b), str(a)))
