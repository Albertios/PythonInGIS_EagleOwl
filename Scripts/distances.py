from math import sin, cos, sqrt, atan2, radians
import numpy as np


# approximate radius of earth in km
R = 6373.0

def computeDistance(p1,p2):
    
    
    lat1 = radians(p1[0])
    lon1 = radians(p1[1])
    lat2 = radians(p2[0])
    lon2 = radians(p2[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance
    
    
    
def getDistances(table):
    result = []
    
    
    
    
    
    
    
    
    
    
    return result
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    














