
import math
def create_circle():
    pts=[]
    for a in range(0,360,10):
        r=math.radians(a)
        pts.append((3*math.cos(r),3*math.sin(r)))
    return pts
