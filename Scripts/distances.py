from math import sin, cos, sqrt, atan2, radians
import numpy as np


# approx. radius of earth
R = 6373.0

#computes distance in km between to given points with lat and long
def computeDistance(p1,p2):
    
#adds a distance column to a table
    
    
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
    
    curOwl = "" # current Owl. Changes when reaching a new tag ID
    p1 = []
    p2 = []
    
    for f in table:
        
        if curOwl == "" :
            curOwl = f[0]
            p1 = [f[1], f[2]]
            np.append(f, "0" )
            
        else:
            if curOwl == f[0]:
                p2 = [f[1], f[2]]
                #[f['lat'],f['long']]
            
                distance = computeDistance(p1, p2)
                
                np.append(f, distance)
                
                
            else:
                curOwl = ""
                np.append(f, "0")
        
        p1 = p2
        np.append(result, f)
        
    print(result)
    
    return result
    
    
    
    
    
    
    
    return result
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    














