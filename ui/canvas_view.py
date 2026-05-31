
from tkinter import *
from core.helpers import *
from core.transformations import *
from core.scanline_fill import scanline_fill

class CanvasView(Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.canvas = Canvas(
            self,
            width=1200,
            height=850,
            bg="white"
        )

        self.canvas.pack(fill="both", expand=True)

        self.original_points = []
        self.points = []
        self.previous_points = []

        self.fill_color = "lightblue"
        self.outline_color = "blue"

        self.camera_x = 0
        self.camera_y = 0

        self.last_x = 0
        self.last_y = 0

        self.reflection_mode = None
        self.custom_reflection_line = None

        self.canvas.bind("<Button-1>", self.start_pan)
        self.canvas.bind("<B1-Motion>", self.pan_canvas)

    def set_colors(self, fill_color, outline_color):
        self.fill_color = fill_color
        self.outline_color = outline_color
        self.draw()

    def start_pan(self, event):
        self.last_x = event.x
        self.last_y = event.y

    def pan_canvas(self, event):
        dx = event.x - self.last_x
        dy = event.y - self.last_y

        self.camera_x += dx
        self.camera_y += dy

        self.last_x = event.x
        self.last_y = event.y

        self.draw()

    def set_shape(self, points):
        self.original_points = points[:]
        self.points = points[:]
        self.previous_points = []
        self.reflection_mode = None
        self.draw()

    def convert(self, x, y):
        ox = 1200 // 2 + self.camera_x
        oy = 850 // 2 + self.camera_y

        return ox + x * GRID_SIZE, oy - y * GRID_SIZE

    def draw_grid_custom(self):

        for x in range(-50, 51):
            px = 1200 // 2 + self.camera_x + x * GRID_SIZE

            self.canvas.create_line(
                px,
                0,
                px,
                850,
                fill="#dddddd"
            )

        for y in range(-50, 51):
            py = 850 // 2 + self.camera_y + y * GRID_SIZE

            self.canvas.create_line(
                0,
                py,
                1200,
                py,
                fill="#dddddd"
            )

    def draw_axis_custom(self):

        ox = 1200 // 2 + self.camera_x
        oy = 850 // 2 + self.camera_y

        self.canvas.create_line(ox, 0, ox, 850, width=2)
        self.canvas.create_line(0, oy, 1200, oy, width=2)

        for i in range(-20, 21):

            px = ox + i * GRID_SIZE

            self.canvas.create_text(
                px,
                oy + 15,
                text=str(i),
                font=("Arial", 8)
            )

        for i in range(-20, 21):

            if i == 0:
                continue

            py = oy - i * GRID_SIZE

            self.canvas.create_text(
                ox - 15,
                py,
                text=str(i),
                font=("Arial", 8)
            )

    def draw_reflection_visual(self):

        if self.reflection_mode is None:
            return

        ox = 1200 // 2 + self.camera_x
        oy = 850 // 2 + self.camera_y

        for (x1, y1), (x2, y2) in zip(self.previous_points, self.points):

            px1, py1 = self.convert(x1, y1)
            px2, py2 = self.convert(x2, y2)

            self.canvas.create_line(
                px1,
                py1,
                px2,
                py2,
                fill="purple",
                dash=(5, 3),
                width=2,
                arrow="last"
            )

            self.canvas.create_text(
                (px1 + px2) / 2,
                (py1 + py2) / 2 - 10,
                text="pantulan",
                fill="purple",
                font=("Arial", 8, "bold")
            )

        if self.reflection_mode == "x":

            self.canvas.create_line(
                0, oy,
                1200, oy,
                fill="red",
                width=3,
                dash=(6, 3)
            )

        elif self.reflection_mode == "y":

            self.canvas.create_line(
                ox, 0,
                ox, 850,
                fill="red",
                width=3,
                dash=(6, 3)
            )

        elif self.reflection_mode == "yx":

            self.canvas.create_line(
                ox - 1000,
                oy + 1000,
                ox + 1000,
                oy - 1000,
                fill="red",
                width=3,
                dash=(6, 3)
            )

        elif self.reflection_mode == "custom":

            a, b, c = self.custom_reflection_line

            x1 = -100
            y1 = (-a * x1 - c) / b if b != 0 else 0

            x2 = 100
            y2 = (-a * x2 - c) / b if b != 0 else 0

            px1, py1 = self.convert(x1, y1)
            px2, py2 = self.convert(x2, y2)

            self.canvas.create_line(
                px1,
                py1,
                px2,
                py2,
                fill="red",
                width=3,
                dash=(6, 3)
            )

            self.canvas.create_text(
                px1 + 120,
                py1 - 20,
                text=f"GARIS CERMIN : {a}x + {b}y + {c} = 0",
                fill="red",
                font=("Arial", 10, "bold")
            )

    def draw(self):

        self.canvas.delete("all")

        self.draw_grid_custom()
        self.draw_axis_custom()
        self.draw_reflection_visual()

        if not self.points:
            return

        if self.reflection_mode is not None:

            gray = []

            for x, y in self.previous_points:

                px, py = self.convert(x, y)

                gray.extend([px, py])

            self.canvas.create_polygon(
                gray,
                outline="gray",
                dash=(4, 2),
                fill="#d9d9d9",
                stipple="gray25"
            )

            self.canvas.create_text(
                gray[0],
                gray[1] - 20,
                text="BANGUN MAYA",
                fill="gray",
                font=("Arial", 10, "bold")
            )

        pts = []

        for x, y in self.points:

            px, py = self.convert(x, y)

            pts.extend([px, py])

            self.canvas.create_oval(
                px - 4,
                py - 4,
                px + 4,
                py + 4,
                fill="red"
            )

            self.canvas.create_text(
                px + 25,
                py,
                text=f"({round(x,2)}, {round(y,2)})"
            )

        # Scan Line Fill
        screen_pts = [(pts[i], pts[i+1]) for i in range(0, len(pts), 2)]
        scanline_fill(self.canvas, screen_pts, self.fill_color)

        # Outline saja (tanpa fill bawaan)
        self.canvas.create_polygon(
            pts,
            fill="",
            outline=self.outline_color,
            width=2
        )

        if self.reflection_mode is not None:

            self.canvas.create_text(
                pts[0],
                pts[1] - 20,
                text="BANGUN NYATA",
                fill="blue",
                font=("Arial", 10, "bold")
            )

    def apply(self, func):

        before = self.points[:]

        self.points = [func(x, y) for x, y in self.points]

        self.draw()

        return before, self.points

    def translate(self, tx, ty):
        self.reflection_mode = None
        return self.apply(
            lambda x, y: translate_point(x, y, tx, ty)
        )

    def scale(self, sx, sy):
        self.reflection_mode = None
        return self.apply(
            lambda x, y: scale_point(x, y, sx, sy)
        )

    def rotate(self, angle):
        self.reflection_mode = None
        return self.apply(
            lambda x, y: rotate_point(x, y, angle)
        )

    def reflect(self, mode):

        self.previous_points = self.points[:]

        self.reflection_mode = mode

        return self.apply(
            lambda x, y: reflect_point(x, y, mode)
        )

    def reflect_custom(self, a, b, c):

        self.previous_points = self.points[:]

        self.reflection_mode = "custom"
        self.custom_reflection_line = (a, b, c)

        return self.apply(
            lambda x, y: reflect_point_custom(x, y, a, b, c)
        )

    def shear(self, shx, shy):
        self.reflection_mode = None
        return self.apply(
            lambda x, y: shear_point(x, y, shx, shy)
        )

    def reset(self):
        self.points = self.original_points[:]
        self.previous_points = []
        self.reflection_mode = None
        self.draw()

    def clear_canvas(self):
        self.points = []
        self.original_points = []
        self.previous_points = []
        self.reflection_mode = None
        self.canvas.delete("all")
