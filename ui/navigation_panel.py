
from tkinter import *

class NavigationPanel(Frame):

    def __init__(self, parent, canvas):
        super().__init__(parent, bd=1, relief="solid")

        self.canvas = canvas

        Label(
            self,
            text="NAVIGASI",
            font=("Arial",8,"bold")
        ).grid(row=0,column=1)

        # atas
        Button(
            self,
            text="↑",
            width=4,
            command=lambda:self.move(0,1)
        ).grid(row=1,column=1)

        # diagonal atas kiri
        Button(
            self,
            text="↖",
            width=4,
            command=lambda:self.move(-1,1)
        ).grid(row=1,column=0)

        # diagonal atas kanan
        Button(
            self,
            text="↗",
            width=4,
            command=lambda:self.move(1,1)
        ).grid(row=1,column=2)

        # kiri
        Button(
            self,
            text="←",
            width=4,
            command=lambda:self.move(-1,0)
        ).grid(row=2,column=0)

        # reset
        Button(
            self,
            text="○",
            width=4,
            command=canvas.reset
        ).grid(row=2,column=1)

        # kanan
        Button(
            self,
            text="→",
            width=4,
            command=lambda:self.move(1,0)
        ).grid(row=2,column=2)

        # diagonal bawah kiri
        Button(
            self,
            text="↙",
            width=4,
            command=lambda:self.move(-1,-1)
        ).grid(row=3,column=0)

        # bawah
        Button(
            self,
            text="↓",
            width=4,
            command=lambda:self.move(0,-1)
        ).grid(row=3,column=1)

        # diagonal bawah kanan
        Button(
            self,
            text="↘",
            width=4,
            command=lambda:self.move(1,-1)
        ).grid(row=3,column=2)

    def move(self, tx, ty):

        before, after = self.canvas.translate(tx, ty)

        proses = ""

        for (x, y), (xr, yr) in zip(before, after):

            proses += f"""
Titik ({x},{y})

x' = x + Tx
x' = {x} + {tx}
x' = {xr}

y' = y + Ty
y' = {y} + {ty}
y' = {yr}

Hasil:
({x},{y}) -> ({xr},{yr})

----------------------------

"""

        rumus = f"""NAVIGASI / PERPINDAHAN POSISI

Rumus:
x' = x + Tx
y' = y + Ty

Input:
Tx = {tx}
Ty = {ty}

Perubahan Titik:
{proses}
"""

        try:
            parent = self.master

            while parent:

                if hasattr(parent, "formula"):
                    parent.formula.update_formula(rumus)
                    break

                parent = parent.master

        except:
            pass
