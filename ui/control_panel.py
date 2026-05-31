
from tkinter import *
from tkinter.colorchooser import askcolor
from math import pi

from shapes.square import create_square
from shapes.rectangle import create_rectangle
from shapes.triangle import create_triangle
from shapes.circle import create_circle
from shapes.oval import create_oval

from ui.navigation_panel import NavigationPanel


class ControlPanel(Frame):

    def __init__(self, parent, canvas, formula, table):
        super().__init__(parent, bd=2, relief="groove")

        self.canvas = canvas
        self.formula = formula
        self.table = table

        Label(self, text="PILIH BANGUN",
              font=("Arial", 9, "bold")).grid(row=0, column=0, columnspan=12)

        Button(self, text="Persegi", width=8,
               command=self.pick_square).grid(row=1, column=0)

        Button(self, text="Panjang", width=8,
               command=self.pick_rectangle).grid(row=1, column=1)

        Button(self, text="Segitiga", width=8,
               command=self.pick_triangle).grid(row=1, column=2)

        Button(self, text="Lingkaran", width=8,
               command=self.pick_circle).grid(row=1, column=3)

        Button(self, text="Oval", width=8,
               command=self.pick_oval).grid(row=1, column=4)

        self.nav = NavigationPanel(self, self.canvas)
        self.nav.grid(row=2, column=7, rowspan=5, padx=5, pady=15, sticky="nw")

        # warna
        Label(self, text="WARNA", font=("Arial",8)).grid(row=2, column=4)

        Button(self, text="Fill Color",
               bg="lightblue",
               command=self.choose_fill).grid(row=2, column=5)

        Button(self, text="Outline Color",
               bg="lightyellow",
               command=self.choose_outline).grid(row=2, column=6)

        # translasi
        Label(self, text="TRANSLASI", font=("Arial",8)).grid(row=3, column=0)

        Label(self, text="Tx", font=("Arial",8)).grid(row=3, column=1)
        self.tx = Entry(self, width=4)
        self.tx.grid(row=3, column=2)

        Label(self, text="Ty", font=("Arial",8)).grid(row=3, column=3)
        self.ty = Entry(self, width=4)
        self.ty.grid(row=3, column=4)

        Button(self, text="Apply",
               command=self.do_translate).grid(row=3, column=5)

        # scaling
        Label(self, text="SCALING", font=("Arial",8)).grid(row=4, column=0)

        Label(self, text="Sx", font=("Arial",8)).grid(row=4, column=1)
        self.sx = Entry(self, width=4)
        self.sx.grid(row=4, column=2)

        Label(self, text="Sy", font=("Arial",8)).grid(row=4, column=3)
        self.sy = Entry(self, width=4)
        self.sy.grid(row=4, column=4)

        Button(self, text="Apply",
               command=self.do_scale).grid(row=4, column=5)

        # rotasi
        Label(self, text="ROTASI", font=("Arial",8)).grid(row=5, column=0)

        Label(self, text="Sudut", font=("Arial",8)).grid(row=5, column=1)
        self.angle = Entry(self, width=7)
        self.angle.grid(row=5, column=2, columnspan=2)

        Label(self, text="Derajat / Persamaan",
              fg="blue").grid(row=5, column=4)

        Button(self, text="Apply",
               bg="lightgreen",
               command=self.do_rotate).grid(row=5, column=5)

        # refleksi
        Label(self, text="REFLEKSI", font=("Arial",8)).grid(row=6, column=0)

        Button(self, text="X",
               command=lambda: self.do_reflect("x")).grid(row=6, column=1)

        Button(self, text="Y",
               command=lambda: self.do_reflect("y")).grid(row=6, column=2)

        Button(self, text="O",
               command=lambda: self.do_reflect("origin")).grid(row=6, column=3)

        Button(self, text="y=x",
               command=lambda: self.do_reflect("yx")).grid(row=6, column=4)

        # shear
        Label(self, text="SHEAR", font=("Arial",8)).grid(row=7, column=0)

        Label(self, text="Shx", font=("Arial",8)).grid(row=7, column=1)
        self.shx = Entry(self, width=4)
        self.shx.grid(row=7, column=2)

        Label(self, text="Shy", font=("Arial",8)).grid(row=7, column=3)
        self.shy = Entry(self, width=4)
        self.shy.grid(row=7, column=4)

        Button(self, text="Apply",
               command=self.do_shear).grid(row=7, column=5)

        # custom reflection
        Label(self, text="GARIS CUSTOM",
              fg="red").grid(row=8, column=0)

        Label(self, text="a", font=("Arial",8)).grid(row=8, column=1)
        self.ca = Entry(self, width=4)
        self.ca.grid(row=8, column=2)

        Label(self, text="b", font=("Arial",8)).grid(row=8, column=3)
        self.cb = Entry(self, width=4)
        self.cb.grid(row=8, column=4)

        Label(self, text="c", font=("Arial",8)).grid(row=8, column=5)
        self.cc = Entry(self, width=4)
        self.cc.grid(row=8, column=6)

        Button(self, text="Refleksi",
               bg="pink",
               command=self.do_custom_reflection).grid(row=8, column=7)

        Button(self,
               text="Bersihkan Canvas",
               bg="tomato",
               fg="white",
               command=self.canvas.clear_canvas).grid(row=9, column=0, columnspan=3, pady=10)

    # ─── Shape Pickers (buat bangun + tampilkan rumus) ───

    def _format_points(self, points):
        return "\n".join(f"  ({x}, {y})" for x, y in points)

    def pick_square(self):
        pts = create_square()
        self.canvas.set_shape(pts)

        rumus = f"""MEMBUAT BANGUN: PERSEGI

Rumus:
  Titik didefinisikan secara langsung
  sebagai 4 vertex persegi.

  points = [(-2,-2), (2,-2), (2,2), (-2,2)]

Sisi = 4 satuan

Titik-titik yang dihasilkan:
{self._format_points(pts)}
"""
        self.formula.update_formula(rumus)

    def pick_rectangle(self):
        pts = create_rectangle()
        self.canvas.set_shape(pts)

        rumus = f"""MEMBUAT BANGUN: PERSEGI PANJANG

Rumus:
  Titik didefinisikan secara langsung
  sebagai 4 vertex persegi panjang.

  points = [(-4,-2), (4,-2), (4,2), (-4,2)]

Panjang = 8 satuan
Lebar   = 4 satuan

Titik-titik yang dihasilkan:
{self._format_points(pts)}
"""
        self.formula.update_formula(rumus)

    def pick_triangle(self):
        pts = create_triangle()
        self.canvas.set_shape(pts)

        rumus = f"""MEMBUAT BANGUN: SEGITIGA

Rumus:
  Titik didefinisikan secara langsung
  sebagai 3 vertex segitiga.

  points = [(0,4), (-3,-3), (3,-3)]

Titik-titik yang dihasilkan:
{self._format_points(pts)}
"""
        self.formula.update_formula(rumus)

    def pick_circle(self):
        pts = create_circle()
        self.canvas.set_shape(pts)

        rumus = f"""MEMBUAT BANGUN: LINGKARAN

Rumus (persamaan parametrik):
  x = r × cos(θ)
  y = r × sin(θ)

Parameter:
  r = 3
  θ = 0°, 10°, 20°, ..., 350°

Jumlah titik: {len(pts)}

Kode:
  for θ in range(0, 360, 10):
      rad = radians(θ)
      x = 3 × cos(rad)
      y = 3 × sin(rad)

Titik-titik yang dihasilkan:
{self._format_points(pts)}
"""
        self.formula.update_formula(rumus)

    def pick_oval(self):
        pts = create_oval()
        self.canvas.set_shape(pts)

        rumus = f"""MEMBUAT BANGUN: OVAL / ELIPS

Rumus (persamaan parametrik):
  x = a × cos(θ)
  y = b × sin(θ)

Parameter:
  a = 5  (semi-major axis)
  b = 2  (semi-minor axis)
  θ = 0°, 10°, 20°, ..., 350°

Jumlah titik: {len(pts)}

Kode:
  for θ in range(0, 360, 10):
      rad = radians(θ)
      x = 5 × cos(rad)
      y = 2 × sin(rad)

Titik-titik yang dihasilkan:
{self._format_points(pts)}
"""
        self.formula.update_formula(rumus)

    def get_value(self, entry, default=0):
        value = entry.get().strip()

        if value == "":
            return default

        return float(value)

    def choose_fill(self):
        color = askcolor()[1]

        if color:
            self.canvas.set_colors(color, self.canvas.outline_color)

            rumus = f"""SCAN LINE FILL

Warna fill: {color}

Algoritma:
  1. Bangun Edge Table (ET) dari semua
     sisi polygon (abaikan sisi horizontal)

  2. Untuk setiap edge, simpan:
     - y_min, y_max
     - x pada y_min
     - inverse slope (dx/dy = 1/m)

  3. Scan dari y_min ke y_max:
     Untuk setiap scan line y:
       a. Cari intersection x dengan
          setiap edge yang aktif
          (y_min ≤ y < y_max)
       b. x = x_start + (y - y_min) × (1/m)
       c. Urutkan intersection
       d. Gambar garis antara pasangan
          intersection (fill antar x)

Rumus intersection:
  x_intersect = x₀ + (y - y_min) × (Δx/Δy)
"""
            self.formula.update_formula(rumus)

    def choose_outline(self):
        color = askcolor()[1]

        if color:
            self.canvas.set_colors(self.canvas.fill_color, color)

    def parse_rotation_input(self, value):
        value = value.strip().lower()

        if value == "":
            return 0

        value = value.replace("pi", str(pi))
        value = value.replace("π", str(pi))

        return float(eval(value))

    def build_point_process(self, before, after):

        text = ""

        for b, a in zip(before, after):
            text += f"{b} -> {a}\n"

        return text

    def update_all(self, before, after, text):

        try:
            self.table.update_table(before, after)
        except:
            pass

        try:
            self.formula.update_formula(text)
        except Exception as e:
            print("FORMULA ERROR:", e)

    def do_translate(self):

        tx = self.get_value(self.tx)
        ty = self.get_value(self.ty)

        before, after = self.canvas.translate(tx, ty)

        proses = self.build_translation_detail(before, after, tx, ty)

        rumus = f"""TRANSLASI

Rumus:
x' = x + Tx
y' = y + Ty

Input:
Tx = {tx}
Ty = {ty}

Perubahan Titik:
{proses}
"""

        self.update_all(before, after, rumus)

    def do_scale(self):

        sx = self.get_value(self.sx, 1)
        sy = self.get_value(self.sy, 1)

        before, after = self.canvas.scale(sx, sy)

        proses = self.build_scaling_detail(before, after, sx, sy)

        rumus = f"""SCALING

Rumus:
x' = x × Sx
y' = y × Sy

Input:
Sx = {sx}
Sy = {sy}

Perubahan Titik:
{proses}
"""

        self.update_all(before, after, rumus)

    def do_rotate(self):

        raw = self.angle.get()
        angle = self.parse_rotation_input(raw)

        before, after = self.canvas.rotate(angle)

        proses = ""

        for (x, y), (xr, yr) in zip(before, after):

            proses += f"""
Titik ({x},{y})

Rumus:
x' = x cos θ - y sin θ
y' = x sin θ + y cos θ

Sudut:
θ = {angle}°

Hasil:
({x},{y}) -> ({xr},{yr})

----------------------------

"""


        rumus = f"""ROTASI

Sudut:
{angle}°

Rumus:
x' = x cos θ - y sin θ
y' = x sin θ + y cos θ

Perubahan Titik:
{proses}
"""

        self.update_all(before, after, rumus)

    def do_reflect(self, mode):

        before, after = self.canvas.reflect(mode)

        proses = self.build_reflection_detail(before, after, mode)

        rumus = f"""REFLEKSI

Mode:
{mode}

Perubahan Titik:
{proses}
"""

        self.update_all(before, after, rumus)

    def do_shear(self):

        shx = self.get_value(self.shx)
        shy = self.get_value(self.shy)

        before, after = self.canvas.shear(shx, shy)

        proses = self.build_shear_detail(before, after, shx, shy)

        rumus = f"""SHEAR

Rumus:
x' = x + shx·y
y' = y + shy·x

Input:
shx = {shx}
shy = {shy}

Perubahan Titik:
{proses}
"""

        self.update_all(before, after, rumus)

    def do_custom_reflection(self):

        a = self.get_value(self.ca, 1)
        b = self.get_value(self.cb, -1)
        c = self.get_value(self.cc, 0)

        before, after = self.canvas.reflect_custom(a, b, c)

        proses = ""

        for (x, y), (xr, yr) in zip(before, after):

            proses += f"""
Titik ({x},{y})

Rumus:
x' = x - 2a(ax+by+c)/(a²+b²)
y' = y - 2b(ax+by+c)/(a²+b²)

Input:
a={a}, b={b}, c={c}

Hasil:
({x},{y}) -> ({xr},{yr})

----------------------------

"""


        rumus = f"""REFLEKSI GARIS CUSTOM

Persamaan Garis:
{a}x + {b}y + {c} = 0

Rumus:
x' = x - 2a(ax+by+c)/(a²+b²)
y' = y - 2b(ax+by+c)/(a²+b²)

Perubahan Titik:
{proses}
"""

        self.update_all(before, after, rumus)


    def build_translation_detail(self, before, after, tx, ty):

        text = ""

        for (x, y), (xr, yr) in zip(before, after):

            text += f"""
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

        return text

    def build_scaling_detail(self, before, after, sx, sy):

        text = ""

        for (x, y), (xr, yr) in zip(before, after):

            text += f"""
Titik ({x},{y})

x' = x × Sx
x' = {x} × {sx}
x' = {xr}

y' = y × Sy
y' = {y} × {sy}
y' = {yr}

Hasil:
({x},{y}) -> ({xr},{yr})

----------------------------

"""

        return text

    def build_reflection_detail(self, before, after, mode):

        text = ""

        for (x, y), (xr, yr) in zip(before, after):

            text += f"""
Titik ({x},{y})

Mode refleksi:
{mode}

Hasil:
({x},{y}) -> ({xr},{yr})

----------------------------

"""

        return text

    def build_shear_detail(self, before, after, shx, shy):

        text = ""

        for (x, y), (xr, yr) in zip(before, after):

            text += f"""
Titik ({x},{y})

x' = x + shx·y
x' = {x} + ({shx} × {y})
x' = {xr}

y' = y + shy·x
y' = {y} + ({shy} × {x})
y' = {yr}

Hasil:
({x},{y}) -> ({xr},{yr})

----------------------------

"""

        return text

