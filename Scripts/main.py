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
#data_dir = os.path.join('D:\\', 'Repositories', 'PythonInGIS_EagleOwl', 'eagle_owl')
data_dir = os.path.join('/Users/Alf/Documents/GitHub', 'PythonInGIS_EagleOwl', 'eagle_owl')

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
    
    #init()
    
    layer = iface.activeLayer()
    
    fullTable = filteredOwlData(layer)

    print(len(fullTable))
    

    minimizedTable = keepDataOverTenDays(fullTable)
    
    # output file direction
    dir = "/Users/Alf/Documents/GitHub/PythonInGIS_EagleOwl/"

    #output file name
    output_file = open(dir + "minimizedTableUTF.csv", 'w')


    for i,f in enumerate(minimizedTable):

        line = str('%s, %s, %f, %f\n' % f)
        unicode_line = line.encode('utf-8')
        #unicode_line = line
        #output_file.write(str(unicode_line))
        output_file.write(unicode_line.decode("utf-8") )
    
    output_file.close()

    print(len(minimizedTable))
    
    distanceTable = getDistances(minimizedTable)


    
main()





