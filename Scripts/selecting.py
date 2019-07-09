
layer = iface.activeLayer()

#ADDING NEW FIELD
from PyQt5.QtCore import QVariant
layer_provider=layer.dataProvider()

rowNames = layer.fields().names()

print(rowNames)
yearExist = False

for i in rowNames:
    if i == 'year':
        yearExist = True


if yearExist == False:
    layer_provider.addAttributes([QgsField("year",QVariant.Double)])
    layer.updateFields()
print (layer.fields().names())






field_to_update = 'year' #Change
field_index = layer.dataProvider().fieldNameIndex(field_to_update)
layer.startEditing()

for feature in layer.getFeatures():
    tempYear = feature['timestamp']
    tempYear = tempYear[0:4]
    _=layer.changeAttributeValue(feature.id(),field_index,tempYear)

layer.commitChanges()