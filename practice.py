import math

def polysum(n,s):
    area = (0.25*n*s**2)/(math.tan(math.pi/n))
    perim = n * s
    return round((area + perim**2), 4)
