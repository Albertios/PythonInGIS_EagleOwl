
def keepDataOverTenDays(fullTable):

    id = 0
    year = "0000"
    month = "00"
    day = "00"

    dayCounter = 0

    for i, array in enumerate(fullTable):

        if id == array[0]:
            timeStampString = str(array[1])
            
            
            if year == timeStampString[0:4]:

                if month == timeStampString[5:7]:
                    if day != timeStampString[8:10]:
                        dayCounter +=1
                        endDelete = i
                        day = timeStampString[8:10]
                else:
                    month = timeStampString[5:7]
                    day = timeStampString[8:10]
                    endDelete = i-1
                    if dayCounter < 10:
                        del(fullTable[startDelete:endDelete])
                        dayCounter = 0
                    startDelete = i
                    dayCounter = 0
            else:
                year = timeStampString[0:4]
        else:
            id = array[0]
            timeStampString = str(array[1])
            year = timeStampString[0:4]
            month = timeStampString[5:7]
            day = timeStampString[8:10]
            
            
    #extra if statement to check the last values after the loop ends
    if dayCounter < 10:
        del(fullTable[startDelete:endDelete])
        
    return(fullTable)
    