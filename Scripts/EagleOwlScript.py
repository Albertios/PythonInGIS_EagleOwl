import os
import os
from qgis.core import *
import qgis.utils
import glob

os.system("python loadOwls.py")

# Working directory
data_dir = os.path.join('D:\\', 'Repositories', 'PythonInGIS_EagleOwl', 'eagle_owl')
#data_dir = os.path.join('/Users/Alf/Documents/GitHub', 'PythonInGIS_EagleOwl', 'eagle_owl', 'owls')




def start():
    QgsProject.instance().removeAllMapLayers()
    
    result = []
        
    #BaseMap
    urlWithParams = 'type=xyz&url=https://a.tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png&zmax=19&zmin=0&crs=EPSG3857'
    rlayer = QgsRasterLayer(urlWithParams, 'OpenStreetMap', 'wms')  
    
    dirs = [d for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))]

    # Do for every owl
    for i in dirs:
        owl = i
        file = owl + '.shp'
        # path to shapefile
        shape_file = os.path.join(data_dir, owl, file)
        
        if rlayer.isValid():
            QgsProject.instance().addMapLayer(rlayer)
        else:
            print('invalid layer')
            
        # load the shapefile
        shape_layer = iface.addVectorLayer(shape_file, "shape:", "ogr")
        if not shape_layer:
            print("Shapefile failed to load!")
        else: print("Shapefile loaded!")  
        
        ####################################################################################################
        
        currentOwl = computeMonthTable()
                
        if len(currentOwl) > 1:
            for tempOwl in currentOwl:
                finalOwl = np.append(tempOwl, owl)
                
                result.append(finalOwl)
                
        else:
            finalOwl = np.append(currentOwl, owl)
            
            result.append(finalOwl)
        
                
        ####################################################################################################
    return result

   
def computeTable():
    years = getYears()
    years = np.array(years)
    return(years)
    
   
def computeMonthTable():
    months = getMonth()
    months = np.array(months)
    return(months)
    



#dir = "/Users/Alf/Documents/GitHub/PythonInGIS_EagleOwl/"

#f = open(dir + "owlYearDistance.shp", 'w')

#f.write(str(owlTable))
#f.closed

def computeDifference():
    owlTable = start()
    
    i = 0
    while i < len(owlTable) - 1:
        
        prevOwl = owlTable[i]
        nextOwl = owlTable[i+1]
        val = float(nextOwl[2]) - float(prevOwl[2])
        
        if val >= 0 :
            #ist mehr geworden
            owlTable[i+1] = np.append(owlTable[i+1], "+")
        else:
            owlTable[i+1] = np.append(owlTable[i+1], "-")
            
        i += 1
        
    return owlTable
  
table = computeDifference()

for i in table:
    print(i)




