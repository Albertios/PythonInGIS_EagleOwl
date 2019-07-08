import os
import os
from qgis.core import *
import qgis.utils

owl = "1753"
file = owl + '.shp'

# Working directory
data_dir = os.path.join('D:\\', 'Repositories', 'PythonInGIS_EagleOwl')
    
# path to shapefile
shape_file = os.path.join(data_dir, 'eagle_owl', owl, file)

urlWithParams = 'type=xyz&url=https://a.tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png&zmax=19&zmin=0&crs=EPSG3857'
rlayer = QgsRasterLayer(urlWithParams, 'OpenStreetMap', 'wms')  

if rlayer.isValid():
    QgsProject.instance().addMapLayer(rlayer)
else:
    print('invalid layer')
    

# load the shapefile
shape_layer = iface.addVectorLayer(shape_file, "shape:", "ogr")
if not shape_layer:
    print("Shapefile failed to load!")
else: print("Shapefile loaded!")  


