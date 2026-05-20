
from tkinter import *
from math import pi

from shapes.square import create_square
from shapes.rectangle import create_rectangle
from shapes.triangle import create_triangle
from shapes.circle import create_circle
from shapes.oval import create_oval


class ControlPanel(Frame):
    def __init__(self,parent,canvas,formula,table):
        super().__init__(parent,bd=2,relief="groove")

        self.canvas=canvas
        self.formula=formula
        self.table=table

        Label(self,text="PILIH BANGUN",font=("Arial",10,"bold")).grid(row=0,column=0,columnspan=6)

        Button(self,text="Persegi",command=lambda:self.canvas.set_shape(create_square())).grid(row=1,column=0)
        Button(self,text="Persegi Panjang",command=lambda:self.canvas.set_shape(create_rectangle())).grid(row=1,column=1)
        Button(self,text="Segitiga",command=lambda:self.canvas.set_shape(create_triangle())).grid(row=1,column=2)
        Button(self,text="Lingkaran",command=lambda:self.canvas.set_shape(create_circle())).grid(row=1,column=3)
        Button(self,text="Oval",command=lambda:self.canvas.set_shape(create_oval())).grid(row=1,column=4)

        Label(self,text="TRANSLASI").grid(row=2,column=0)
        self.tx=Entry(self,width=6)
        self.ty=Entry(self,width=6)
        self.tx.grid(row=2,column=1)
        self.ty.grid(row=2,column=2)
        Button(self,text="Apply",command=self.do_translate).grid(row=2,column=3)

        Label(self,text="SCALING").grid(row=3,column=0)
        self.sx=Entry(self,width=6)
        self.sy=Entry(self,width=6)
        self.sx.grid(row=3,column=1)
        self.sy.grid(row=3,column=2)
        Button(self,text="Apply",command=self.do_scale).grid(row=3,column=3)

        Label(self,text="ROTASI").grid(row=4,column=0)

        self.angle=Entry(self,width=10)
        self.angle.grid(row=4,column=1)

        Label(
            self,
            text="Derajat / Persamaan",
            fg="blue"
        ).grid(row=4,column=2,columnspan=2)

        Button(
            self,
            text="Apply",
            bg="lightgreen",
            command=self.do_rotate
        ).grid(row=4,column=4)

        Label(self,text="REFLEKSI").grid(row=5,column=0)
        Button(self,text="X",command=lambda:self.do_reflect("x")).grid(row=5,column=1)
        Button(self,text="Y",command=lambda:self.do_reflect("y")).grid(row=5,column=2)
        Button(self,text="O",command=lambda:self.do_reflect("origin")).grid(row=5,column=3)
        Button(self,text="y=x",command=lambda:self.do_reflect("yx")).grid(row=5,column=4)

        Label(self,text="SHEAR").grid(row=6,column=0)
        self.shx=Entry(self,width=6)
        self.shy=Entry(self,width=6)
        self.shx.grid(row=6,column=1)
        self.shy.grid(row=6,column=2)
        Button(self,text="Apply",command=self.do_shear).grid(row=6,column=3)

    def parse_rotation_input(self, value):
        value = value.strip().lower()

        replacements = {
            "pi": str(pi),
            "π": str(pi)
        }

        for k,v in replacements.items():
            value = value.replace(k,v)

        try:
            result = eval(value)
            return float(result)
        except:
            return float(value)

    def update_all(self,before,after,text):
        self.table.update_table(before,after)
        self.formula.update_formula(text)

    def do_translate(self):
        tx=float(self.tx.get())
        ty=float(self.ty.get())

        b,a=self.canvas.translate(tx,ty)

        self.update_all(
            b,
            a,
            f"""TRANSLASI

Rumus:
x' = x + Tx
y' = y + Ty

Input:
Tx = {tx}
Ty = {ty}
"""
        )

    def do_scale(self):
        sx=float(self.sx.get())
        sy=float(self.sy.get())

        b,a=self.canvas.scale(sx,sy)

        self.update_all(
            b,
            a,
            f"""SCALING

Rumus:
x' = x × Sx
y' = y × Sy

Input:
Sx = {sx}
Sy = {sy}
"""
        )

    def do_rotate(self):
        raw = self.angle.get()

        angle = self.parse_rotation_input(raw)

        b,a=self.canvas.rotate(angle)

        self.update_all(
            b,
            a,
            f"""ROTASI

Rumus:
x' = x cos θ - y sin θ
y' = x sin θ + y cos θ

Input:
θ = {raw}

Hasil Derajat:
{angle}°

Contoh Input:
90
45+45
180/2
pi*90/pi
"""
        )

    def do_reflect(self,mode):
        b,a=self.canvas.reflect(mode)

        self.update_all(
            b,
            a,
            f"""REFLEKSI

Mode:
{mode}
"""
        )

    def do_shear(self):
        shx=float(self.shx.get())
        shy=float(self.shy.get())

        b,a=self.canvas.shear(shx,shy)

        self.update_all(
            b,
            a,
            f"""SHEAR

Rumus:
x' = x + shx.y
y' = y + shy.x

Input:
shx = {shx}
shy = {shy}
"""
        )
