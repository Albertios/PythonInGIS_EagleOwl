################################################################################
import os
import os
from qgis.core import *
import qgis.utils
import glob
################################################################################

os.system("python extractDataFromShapeFile.py")
os.system("python distances.py")
os.system("python keepDataOverTenDays.py")

# Working directory
data_dir = os.path.join('D:\\', 'Repositories', 'PythonInGIS_EagleOwl', 'eagle_owl')
#data_dir = os.path.join('/Users/Alf/Documents/GitHub', 'PythonInGIS_EagleOwl', 'eagle_owl', 'EagleOwlReinhardVohwinkelMPIO')

def init():
    QgsProject.instance().removeAllMapLayers()
    
    #BaseMap
    #urlWithParams = 'type=xyz&url=https://a.tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png&zmax=19&zmin=0&crs=EPSG3857'
    #rlayer = QgsRasterLayer(urlWithParams, 'OpenStreetMap', 'wms')  
    
    shape_file = os.path.join(data_dir, "points.shp")
    
    #if rlayer.isValid():
    #    QgsProject.instance().addMapLayer(rlayer)
    #else:
    #    print('invalid layer')

    # load the shapefile
    shape_layer = iface.addVectorLayer(shape_file, "shape:", "ogr")
    if not shape_layer:
        print("Shapefile failed to load!")
    else: print("Shapefile loaded!") 
    

def main():
    
    init()
    
    layer = iface.activeLayer()
    
    fullTable = filteredOwlData(layer)
    print("1")
    minimizedTable = keepDataOverTenDays(fullTable)
    print("2")
    distanceTable = getDistances(minimizedTable)
    print("3")
    
main()





