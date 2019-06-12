import os
import os
from qgis.core import *
import qgis.utils

# Working directory
data_dir = os.path.join('D:\\', 'Repositories', 'PythonInGIS_EagleOwl')
    
# path to shapefile
shape_file = os.path.join(data_dir, 'eagle_owl', 'lines.shp')

# load the shapefile
shape_layer = iface.addVectorLayer(shape_file, "shape:", "ogr")
if not shape_layer:
    print("Shapefile failed to load!")
else: print("Shapefile loaded!")  

# First add the required field 
caps = shape_layer.dataProvider().capabilities()
if caps & QgsVectorDataProvider.AddAttributes:
    # We require a String field
    res = shape_layer.dataProvider().addAttributes(
        [QgsField("time_str", QVariant.String)])

# Update to propagate the changes  
shape_layer.updateFields()

# Get the index of the new field
field_name_i_search = 'time_str'
fields = shape_layer.dataProvider().fields()
index = 0
for field in shape_layer.fields():
    if field.name() == field_name_i_search:
        break
    index += 1
print(index)

# Use the created dictionary to update the field for all features
shape_layer.dataProvider().changeAttributeValues(updates)
# Update to propagate the changes  
shape_layer.updateFields()

QgsProject.instance().removeMapLayer(shape_layer.id())
    
def my_open_function(path):
    # Check if it exists
    if os.path.exists(path):
        # If yes, open and put content in variable
        with open(path) as f:
            data = f.read()
    else:
        # If no, put None in the same variable
        data = None
    return data



# Execute function
# Test with correct path
print(my_open_function(in_path))
# And with incorrect path
print(my_open_function('nonsense'))