from math import sin, cos, sqrt, atan2, radians
import numpy as np

#returns table of given owl
def getOwlTable(fullTable, ID):
    
    
    owlTable = []
    
    for i in fullTable:
        if i[0] == str(ID):
            owlTable.append(i)
            
    return owlTable
    
def getMonthTable(inputOwl, month):
    
    
    monthTable = []

    for feature in inputOwl:
        timestamp = str(feature[1])
        year = timestamp[0:4]
        curMonth = timestamp[5:7]
    
        if curMonth == month:
            monthTable.append(feature)
            
    return monthTable
    
def getDayTable(inputMonth, day):
    
    
    dayTable = []
    
    for feature in inputMonth:
        timestamp = str(feature[1])
        year = timestamp[0:4]
        curMonth = timestamp[5:7]
        curDay = timestamp[8:10]

        if curDay == day:
            dayTable.append(feature)
            

    return dayTable
    
def getDay(dayTable):
    
    
    
    
    sumDay = []
    
    timestamp = str(dayTable[0][1])
    year = timestamp[0:4]
    month = timestamp[5:7]
    day = timestamp[8:10]
    
    sumDay.append(dayTable[0][0])
    sumDay.append(year)
    sumDay.append(month)
    sumDay.append(day)
    
    sum = 0
    for feature in dayTable:
        sum =sum + float(feature[4])
    
    sumDay.append(sum)
    
    return sumDay


def getDailyTable(monthTable):
        
    result = []
    tempDay = ""

    for feature in monthTable:
        timestamp = str(feature[1])
        year = timestamp[0:4]
        month = timestamp[5:7]
        curDay = timestamp[8:10]


        if tempDay != curDay:
            curDayTable = getDayTable(monthTable, curDay)
            day = getDay(curDayTable)
            result.append(day)
            tempDay = curDay
            
        else:
            tempDay = curDay
    
    return result

def fillTable(dailyTable):

    if len(dailyTable) < 28:
        print("needRefill, length is: ", len(dailyTable))
        
        return dailyTable
    else:
        return dailyTable


def getMonthDist(dailyFilled):
    result = []
    
    id = dailyFilled[0][0]
    year = dailyFilled[0][1]
    month = dailyFilled[0][2] 

    sum = 0
    for i in dailyFilled:
        sum += i[4]
    
    result.append(id)
    result.append(year)
    result.append(month)
    result.append(sum)
    
    return result


def getAllMonthOfOwl(curOwlTable):
    result = []
    
    id = curOwlTable[0][0]
    year = curOwlTable[0][1]
    tempMonth = ""
    
    for feature in curOwlTable:
        curMonth = feature[1][5:7]
        
        if tempMonth != curMonth:
            
            curMonthTable = getMonthTable(curOwlTable, curMonth)
            
            dailyTable = getDailyTable(curMonthTable)

            dailyFilled = fillTable(dailyTable)

            monthWithDistance = getMonthDist(dailyFilled)

            result.append(monthWithDistance)
            
            tempMonth = curMonth
        

    return result

def computeMonthTable(input):

    result = []
    tempID = ""
    
    for feature in input:
        curOwlID = feature[0]
        
        if tempID != curOwlID:
            
            
            curOwlTable = getOwlTable(input,curOwlID)

            allMonthOfOneOwl = getAllMonthOfOwl(curOwlTable)


            for i in allMonthOfOneOwl:
                result.append(i)
                
            tempID = curOwlID
        
        
    
    print(len(result))
    print(result[0])
    print(result[1])
    print(result[2])
    print(result[3])
    return result
    

table = computeMonthTable(distanceTable)





    