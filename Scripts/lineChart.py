import numpy as np
import matplotlib.pyplot as plt

def getOwl(monthTable, ID):
    result = []
    
    for f in monthTable:
        if f[0] == ID:
            result.append(f)
    return result


def visualizeLine(monthTable):
    x = ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec"]
    
    tempOwl = monthTable[0][0]
    
    legend = []
    for feature in monthTable:
        curOwl = [np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan]
    
        owl = feature[0]
        
        
        if owl != tempOwl:
            
            tempOwl = owl
            t = getOwl(monthTable, feature[0])
            
            if len(t) > 1 :
                legend.append(str(owl))

                for i in t:
                    
                    month = i[2]
                    
                    if month == "01":
                        curOwl[0] = i[3]
                    if month == "02":
                        curOwl[1] = i[3]
                    if month == "03":
                        curOwl[2] = i[3]
                    if month == "04":
                        curOwl[3] = i[3]
                    if month == "05":
                        curOwl[4] = i[3]
                    if month == "06":
                        curOwl[5] = i[3]
                    if month == "07":
                        curOwl[6] = i[3]
                    if month == "08":
                        curOwl[7] = i[3]
                    if month == "09":
                        curOwl[8] = i[3]
                    if month == "10":
                        curOwl[9] = i[3]
                    if month == "11":
                        curOwl[10] = i[3]
                    if month == "12":
                        curOwl[11] = i[3]
        
    
            y = curOwl
            global lines
            lines.append(y)
            plt.plot(x, y)
        
        

    plt.legend(legend, loc=2)
    plt.xlabel('Month')
    plt.ylabel('Total Flight Distance [km]')
    plt.title('Individual Eagle Owl Flight Distance (2011 - 2017)')
    plt.show()
    return lines
    
    
    

lines = []    
visualizeLine(monthTable)

#for i in monthTable:
#    print(i)
