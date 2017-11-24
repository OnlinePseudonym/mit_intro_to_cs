import math
""" Sum the area and squared perimeter of a regular polygon.
    takes number of sides (n) and length of sides (s) as input.
    Output is rounded to 4 decimal places"""
def polysum(n,s):

    area = (0.25*n*s**2)/(math.tan(math.pi/n)) #Calculate area
    perim = n * s #Calculate perimeter
    squared = perim**2

    return round(area + squared, 4) #Return answer rounded to 4 decimal places
