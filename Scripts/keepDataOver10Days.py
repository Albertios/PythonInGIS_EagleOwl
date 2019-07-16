layer = iface.activeLayer()
    
fullTable = filteredOwlData(layer)

print("old table length", len(fullTable))

#timeStampString = fullTable[0][1]

#year = timeStampString[:4]

#month = timeStampString[5:7]

#day = timeStampString[8:10]

#(1292, '2014-05-22 23:28:56', 51.8506758, 7.3554622)

#del(fullTable[0])

id = 0
year = "0000"
month = "00"
day = "00"

dayCounter = 0

for i, array in enumerate(fullTable):

    if id == array[0]:
        timeStampString = array[1]
        #print("id")
        if year == timeStampString[:4]:
            #print("year")
            if month == timeStampString[5:7]:
                #print("month")
                if day != timeStampString[8:10]:
                    print(day)
                    dayCounter +=1
                    endDelete = i
                    day = timeStampString[8:10]
            else:
                month = timeStampString[5:7]
                day = timeStampString[8:10]
                endDelete = i-1
                #print(dayCounter)
                if dayCounter < 10:
                    del(fullTable[startDelete:endDelete])
                    dayCounter = 0
                    print(startDelete, endDelete)
                    print(len(fullTable))
                    #print("delete")
                startDelete = i
                dayCounter = 0
        else:
            year = timeStampString[:4]
    else:
        id = array[0]
        timeStampString = array[1]
        #print(timeStampString)
        year = timeStampString[:4]
        #print(year)
        month = timeStampString[5:7]
        #print(month)
        day = timeStampString[8:10]
        #print(day)
        
        
#extra if statement to check the last values after the loop ends
#print(dayCounter)
if dayCounter < 10:
    del(fullTable[startDelete:endDelete])
    print("new table length", len(fullTable))