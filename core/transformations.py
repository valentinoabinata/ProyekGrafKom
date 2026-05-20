
import math

def translate_point(x, y, tx, ty):
    return x + tx, y + ty

def scale_point(x, y, sx, sy):
    return x * sx, y * sy

def rotate_point(x, y, angle):
    rad = math.radians(angle)
    nx = x * math.cos(rad) - y * math.sin(rad)
    ny = x * math.sin(rad) + y * math.cos(rad)
    return round(nx, 2), round(ny, 2)

def reflect_point(x, y, mode):
    if mode == "x":
        return x, -y
    if mode == "y":
        return -x, y
    if mode == "origin":
        return -x, -y
    if mode == "yx":
        return y, x
    if mode == "y-x":
        return -y, -x
    return x, y

def shear_point(x, y, shx, shy):
    return x + shx * y, y + shy * x
