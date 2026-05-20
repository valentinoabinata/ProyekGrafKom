
from tkinter import *
from core.helpers import *
from core.transformations import *

class CanvasView(Frame):
    def __init__(self,parent):
        super().__init__(parent)

        self.canvas = Canvas(
            self,
            width=CANVAS_WIDTH,
            height=CANVAS_HEIGHT,
            bg="white"
        )

        self.canvas.pack(fill="both", expand=True)

        self.original_points=[]
        self.points=[]

        self.camera_x = 0
        self.camera_y = 0

        self.last_x = 0
        self.last_y = 0

        self.canvas.bind("<Button-1>", self.start_pan)
        self.canvas.bind("<B1-Motion>", self.pan_canvas)

    def start_pan(self,event):
        self.last_x = event.x
        self.last_y = event.y

    def pan_canvas(self,event):
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
        self.draw()

    def convert(self,x,y):
        ox = CANVAS_WIDTH//2 + self.camera_x
        oy = CANVAS_HEIGHT//2 + self.camera_y

        return ox + x*GRID_SIZE, oy - y*GRID_SIZE

    def draw_grid_custom(self):
        for x in range(-50,51):
            px = CANVAS_WIDTH//2 + self.camera_x + x*GRID_SIZE
            self.canvas.create_line(px,0,px,CANVAS_HEIGHT,fill="#dddddd")

        for y in range(-50,51):
            py = CANVAS_HEIGHT//2 + self.camera_y + y*GRID_SIZE
            self.canvas.create_line(0,py,CANVAS_WIDTH,py,fill="#dddddd")

    def draw_axis_custom(self):
        ox = CANVAS_WIDTH//2 + self.camera_x
        oy = CANVAS_HEIGHT//2 + self.camera_y

        self.canvas.create_line(ox,0,ox,CANVAS_HEIGHT,width=2)
        self.canvas.create_line(0,oy,CANVAS_WIDTH,oy,width=2)

    def draw(self):
        self.canvas.delete("all")

        self.draw_grid_custom()
        self.draw_axis_custom()

        if not self.points:
            return

        gray=[]

        for x,y in self.original_points:
            px,py = self.convert(x,y)
            gray.extend([px,py])

        self.canvas.create_polygon(
            gray,
            outline="gray",
            dash=(4,2),
            fill=""
        )

        pts=[]

        for x,y in self.points:
            px,py = self.convert(x,y)

            pts.extend([px,py])

            self.canvas.create_oval(
                px-4,py-4,px+4,py+4,
                fill="red"
            )

            self.canvas.create_text(
                px+25,
                py,
                text=f"({round(x,2)},{round(y,2)})"
            )

        self.canvas.create_polygon(
            pts,
            fill="lightblue",
            outline="blue",
            width=2
        )

    def apply(self, func):
        before = self.points[:]

        self.points = [func(x,y) for x,y in self.points]

        self.draw()

        return before, self.points

    def translate(self,tx,ty):
        return self.apply(
            lambda x,y: translate_point(x,y,tx,ty)
        )

    def scale(self,sx,sy):
        return self.apply(
            lambda x,y: scale_point(x,y,sx,sy)
        )

    def rotate(self,angle):
        return self.apply(
            lambda x,y: rotate_point(x,y,angle)
        )

    def reflect(self,mode):
        return self.apply(
            lambda x,y: reflect_point(x,y,mode)
        )

    def shear(self,shx,shy):
        return self.apply(
            lambda x,y: shear_point(x,y,shx,shy)
        )

    def reset(self):
        self.points=self.original_points[:]
        self.draw()
