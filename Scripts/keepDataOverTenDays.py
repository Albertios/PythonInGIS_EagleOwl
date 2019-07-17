
def keepDataOverTenDays(fullTable):

    id = "0"
    year = "0000"
    month = "00"
    day = "00"

    dayCounter = 0
    startDelete = 0

    for i, array in enumerate(fullTable):

        if id == array[0]:
            timeStampString = str(array[1])
            yearStamp = timeStampString[0:4]
            monthStamp = timeStampString[5:7]
            dayStamp = timeStampString[8:10]
            endDelete = i + 1
            if year == yearStamp:
                endDelete = i + 1
                if month == monthStamp:
                    endDelete = i + 1
                    if day != dayStamp:
                        dayCounter +=1
                        day = dayStamp
                        endDelete = i + 1
                        
                else:
                    month = monthStamp
                    day = dayStamp
                    endDelete = i + 1
                    if dayCounter < 10:
                        del(fullTable[startDelete:endDelete])
                        dayCounter = 0
                    startDelete = i
                    dayCounter = 0
            else:
                year = yearStamp
                endDelete = i + 1
                if dayCounter < 10:
                    del(fullTable[startDelete:endDelete])
                    dayCounter = 0
                startDelete = i
                dayCounter = 0
        else:
            endDelete = i + 1
            if dayCounter < 10 and id != "0":
                del(fullTable[startDelete:endDelete])
                dayCounter = 0
            startDelete = i
            dayCounter = 0
            
            id = array[0]
            timeStampString = str(array[1])
            yearStamp = timeStampString[0:4]
            monthStamp = timeStampString[5:7]
            dayStamp = timeStampString[8:10]
            
            year = yearStamp
            month = monthStamp
            day = dayStamp
            
            
    #extra if statement to check the last values after the loop ends
    if dayCounter < 10:
        del(fullTable[startDelete:endDelete])
        
    return(fullTable)
    

