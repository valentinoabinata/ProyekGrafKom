
import math
def create_oval():
    pts=[]
    for a in range(0,360,10):
        r=math.radians(a)
        pts.append((5*math.cos(r),2*math.sin(r)))
    return pts
