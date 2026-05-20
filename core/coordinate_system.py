
from core.helpers import *

def draw_grid(canvas):
    for x in range(0, CANVAS_WIDTH, GRID_SIZE):
        canvas.create_line(x,0,x,CANVAS_HEIGHT, fill="#dddddd")

    for y in range(0, CANVAS_HEIGHT, GRID_SIZE):
        canvas.create_line(0,y,CANVAS_WIDTH,y, fill="#dddddd")

def draw_axis(canvas):
    ox = CANVAS_WIDTH // 2
    oy = CANVAS_HEIGHT // 2

    canvas.create_line(ox,0,ox,CANVAS_HEIGHT, width=2)
    canvas.create_line(0,oy,CANVAS_WIDTH,oy, width=2)

    for i in range(-10,11):
        x = ox + i*GRID_SIZE
        y = oy - i*GRID_SIZE

        canvas.create_text(x, oy+10, text=str(i))
        canvas.create_text(ox+10, y, text=str(i))
