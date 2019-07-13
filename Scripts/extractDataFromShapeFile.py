##################create a filtered CSV file#######################
##load poits.shp file 
#layer = iface.activeLayer()
#
## output file direction
#dir = "/Users/Alf/Documents/GitHub/PythonInGIS_EagleOwl/"
#
##output file name
#output_file = open(dir + "filteredOwlData.csv", 'w')
#
#
#for f in layer.getFeatures():
#    geom = f.geometry()
#    line = '%s, %s, %f, %f\n' % (f['tag_ident'], f['timestamp'],
#        geom.asPoint().y(), geom.asPoint().x())
#    unicode_line = line.encode('utf-8')
#    output_file.write(unicode_line.decode("utf-8") )
#    
#output_file.close()

#_________________________________________________________________


##################create a filtered array#######################

def filteredOwlData(layer):
    
#layer = iface.activeLayer()
    
    owlIdTimestampXY = []
    
    #goes through layer and save the ID, timestamp, coordiantes into 2D array
    for f in layer.getFeatures():
        geom = f.geometry()
        line = int(f['tag_ident']), f['timestamp'], geom.asPoint().y(), geom.asPoint().x()
        owlIdTimestampXY.append(line)
    
    return(owlIdTimestampXY)
    
