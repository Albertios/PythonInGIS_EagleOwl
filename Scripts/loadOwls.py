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

  
  


# Funktion soll array ausgeben mit arraylen = jahresanzahl und an zweiter stelle distanz pro jahr
def computeYearlyDist(years):
    
    result = []
    p1 = []
    p2 = []
    

    for i in years:
        p2 = [i['lat'],i['long']]
        
        if not p1:
            p1 = p2
        else:
            dist = computeDistance(p1,p2)
            result.append(dist)
            
    p1 = p2
    return sum(result)
    



def getYears():
    layer = iface.activeLayer()
    years = []
    curYear = []
    noYears = 0
    
    for f in layer.getFeatures():
        
        if not curYear:
            curYear.append(f)
            year = f['timestamp']
            year = year[0:4]
            #print(year)
            
        else:
            tempYear = f['timestamp']
            tempYear = tempYear[0:4]
            if tempYear == year:
                curYear.append(f)
                
            else:
                years.append([year ,computeYearlyDist(curYear)]) # next year
                year = f['timestamp']
                year = year[0:4]
                tempYear = f['timestamp']
                tempYear = tempYear[0:4]
                noYears += 1
                #print(year)
       
    years.append([tempYear ,computeYearlyDist(curYear)])
       
    return years
    
    
    
#Tabelle mit monat bzw monat und jahr und distanz und prozentzahl
def getMonth():
    layer = iface.activeLayer()
    months = []
    curMonth = []
    noMonths = 0
    
    
    for f in layer.getFeatures():
        
        if not curMonth:                #starting Iteration
            curMonth.append(f)
            timestamp = f['timestamp']
            month = timestamp[5:7]
            year = timestamp[0:4]

        else:
            timestamp = f['timestamp']
            tempMonth = timestamp[5:7]
            tempYear = timestamp[0:4]
            
            if tempYear == year and tempMonth == month:
                curMonth.append(f)
                #print(tempMonth)
                
            else:
                months.append([year , month, computeYearlyDist(curMonth)]) # next month computeYearlyDist(curYear)
                curMonth = []
                timestamp = f['timestamp']
                month = timestamp[5:7]
                tempMonth = timestamp[5:7]
                year = timestamp[0:4]
                tempYear = timestamp[0:4]
                noMonths += 1
                #print(year)

    months.append([year , month, computeYearlyDist(curMonth)])

    return months

    
    
    
    
    
    
    
    
    
    
    
    
    
