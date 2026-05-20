
GRID_SIZE = 38
CANVAS_WIDTH = 900
CANVAS_HEIGHT = 650

def cartesian_to_canvas(x, y):
    ox = CANVAS_WIDTH // 2
    oy = CANVAS_HEIGHT // 2
    return ox + x * GRID_SIZE, oy - y * GRID_SIZE
