import matplotlib.pyplot as plt




def getOwl(monthTable):
    
    curOwl = ""
    result = []
    
    for feature in monthTable:
        curOwl = feature[0]
        print(feature)
        
        

        
        #if feature[0] != 1751:
        #    temp = []
        #    break
        


def visualizeOwls(monthTable):
    year = ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec"]
    
    getOwl(monthTable)


    pop_pakistan = [44.91, 58.09, 78.07, 107.7, 138.5, 170.6, 170.6, 170.6, 170.6, 170.6, 170.6, 170.6]
    pop_india = [449.48, 553.57, 696.783, 870.133, 1000.4, 1309.1, 170.6, 170.6, 170.6, 170.6, 170.6, 170.6]





    plt.plot(year, pop_pakistan, color='g')
    plt.plot(year, pop_india, color='orange')
    plt.xlabel('Month')
    plt.ylabel('Total Distance (km)')
    plt.title('Distance Per month')
    plt.show()
    
    
visualizeOwls(monthTable)