import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

y_pos = np.arange(len(objects))

def getMonthlyAverage(monthTable):
    
    result = []
    totalDist = 0
    curMonth = "01"
    counter = 0
    for i in range(1, 13):
        for feature in monthTable:
            tempMonth = feature[2]
            
            if curMonth == tempMonth:
                totalDist = totalDist + feature[3]
                counter += 1
            
            curMonth = str(i)
            
            if len(curMonth) == 1:
                curMonth = "0" + curMonth
            
            
            
        
        
        if counter != 0:
            result.append( (totalDist / counter ) )
        else:
            result.append(0)
        counter = 0
        totalDist = 0
        
    return result

average = getMonthlyAverage(monthTable)

ax = plt.axes()        
ax.yaxis.grid() 


plt.bar(y_pos, average, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Distance [km]')
plt.title('Eagle Owl Average Flight Distance')


plt.show()