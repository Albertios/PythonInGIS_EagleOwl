from math import sin, cos, sqrt, atan2, radians
import numpy as np




def computeMonthTable(input):
    
    result = []
    curDistance = 0
    
    for f in input:
        curID = str(f[0])
        timestamp = str(f[1])
        year = timestamp[0:4]
        month = timestamp[5:7]
        distance = f[4]
        
        
        curDistance = curDistance + distance
        
        
        if(curID != "1751"):
            break
    
    
    return result
    

table = computeMonthTable(distanceTable)
print(table[0])





    