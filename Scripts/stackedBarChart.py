import matplotlib.pyplot as plt
import numpy as np

cnames = [
        '#F0F8FF',
        '#FAEBD7',
        '#00FFFF',
        '#7FFFD4',
        '#F0FFFF',
        '#F5F5DC',
        '#FFE4C4',
        '#000000',
        '#FFEBCD',
        '#0000FF',
        '#8A2BE2',
        '#A52A2A',
        '#DEB887',
        '#5F9EA0',
        '#7FFF00',
        '#D2691E',
        '#FF7F50',
        '#6495ED',
        '#FFF8DC',
        '#DC143C',
        '#00FFFF',
        '#00008B',
        '#008B8B',
        '#B8860B',
        '#A9A9A9',
        '#006400',
        '#BDB76B',
        '#8B008B',
        '#556B2F',
        '#FF8C00',
        '#9932CC',
        '#8B0000',
        '#E9967A',
        '#8FBC8F',
        '#483D8B',
        '#2F4F4F',
        '#00CED1',
        '#9400D3',
        '#FF1493',
        '#00BFFF',
        '#696969',
        '#1E90FF',
        '#B22222',
        '#FFFAF0',
        '#228B22',
        '#FF00FF',
        '#DCDCDC',
        '#F8F8FF',
        '#FFD700',
        '#DAA520',
        '#808080',
        '#008000',
        '#ADFF2F',
        '#F0FFF0',
        '#FF69B4',
        '#CD5C5C',
        '#4B0082',
        '#FFFFF0',
        '#F0E68C',
        '#E6E6FA',
        '#FFF0F5',
        '#7CFC00',
        '#FFFACD',
        '#ADD8E6',
        '#F08080',
        '#E0FFFF',
        '#FAFAD2',
        '#90EE90',
        '#D3D3D3',
        '#FFB6C1',
        '#FFA07A',
        '#20B2AA',
        '#87CEFA',
        '#778899',
        '#B0C4DE',
        '#FFFFE0',
        '#00FF00',
        '#32CD32',
        '#FAF0E6',
        '#FF00FF',
        '#800000',
        '#66CDAA',
        '#0000CD',
        '#BA55D3',
        '#9370DB',
        '#3CB371',
        '#7B68EE',
        '#00FA9A',
        '#48D1CC',
        '#C71585',
        '#191970',
        '#F5FFFA',
        '#FFE4E1',
        '#FFE4B5',
        '#FFDEAD',
        '#000080',
        '#FDF5E6',
        '#808000',
        '#6B8E23',
        '#FFA500',
        '#FF4500',
        '#DA70D6',
        '#EEE8AA',
        '#98FB98',
        '#AFEEEE',
        '#DB7093',
        '#FFEFD5',
        '#FFDAB9',
        '#CD853F',
        '#FFC0CB',
        '#DDA0DD',
        '#B0E0E6',
        '#800080',
        '#FF0000',
        '#BC8F8F',
        '#4169E1',
        '#8B4513',
        '#FA8072',
        '#FAA460',
        '#2E8B57',
        '#FFF5EE',
        '#A0522D',
        '#C0C0C0',
        '#87CEEB',
        '#6A5ACD',
        '#708090',
        '#FFFAFA',
        '#00FF7F',
        '#4682B4',
        '#D2B48C',
        '#008080',
        '#D8BFD8',
        '#FF6347',
        '#40E0D0',
        '#EE82EE',
        '#F5DEB3',
        '#FFFFFF',
        '#F5F5F5',
        '#FFFF00',
        '#9ACD32']
months =    {'Jan': [], 
             'Feb': [], 
             'Mar': [],
             'Apr': [],
             'May': [],
             'Jun': [],
             'Jul': [],
             'Aug': [],
             'Sep': [],
             'Oct': [],
             'Nov': [],
             'Dec': []
             }


def getOwl(monthTable, ID):
    result = []
    
    for f in monthTable:
        if f[0] == ID:
            result.append(f)
    return result
    
def fillNull(months):
    months["Jan"].append(0)
    months["Feb"].append(0)
    months["Mar"].append(0)
    months["Apr"].append(0)
    months["May"].append(0)
    months["Jun"].append(0)
    months["Jul"].append(0)
    months["Aug"].append(0)
    months["Sep"].append(0)
    months["Oct"].append(0)
    months["Nov"].append(0)
    months["Dec"].append(0)
    return months

def fillMonths(monthTable, months):
    
    curOwl = monthTable[0][0]
    
    for feature in monthTable:
        tempOwl = feature[0]
        
        month = feature[2]
        dist = feature[3]
        owl = getOwl(monthTable, "1751")
        
        # get all Data for one owl
        # fill all month with distance
        # missing data = 0 distance
        months = fillNull(months)
        
        if month == "01":
            months["Jan"][len(months["Jan"])-1] = dist
        if month == "02":
            months["Feb"][len(months["Feb"])-1] = dist
        if month == "03":
            months["Mar"][len(months["Mar"])-1] = dist
        if month == "04":
            months["Apr"][len(months["Apr"])-1] = dist
        if month == "05":
            months["May"][len(months["May"])-1] = dist
        if month == "06":
            months["Jun"][len(months["Jun"])-1] = dist
        if month == "07":
            months["Jul"][len(months["Jul"])-1] = dist
        if month == "08":
            months["Aug"][len(months["Aug"])-1] = dist
        if month == "09":
            months["Sep"][len(months["Sep"])-1] = dist
        if month == "10":
            months["Oct"][len(months["Oct"])-1] = dist
        if month == "11":
            months["Nov"][len(months["Nov"])-1] = dist
        if month == "12":
            months["Dec"][len(months["Dec"])-1] = dist
        
    return months
    

months = fillMonths(monthTable, months)


X = np.arange(12)

curOwl = [np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,]
counter = 0

tempOwl = "0"

lastOwl="none"

for feature in monthTable:
    
    owl = feature[0]
    
    if owl != tempOwl:
        
        tempOwl = owl
        t = getOwl(monthTable, feature[0])
        
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
            
        
        col = cnames[counter]
        if lastOwl == "none":
            plt.bar(X, curOwl, color = col)
        else:
            plt.bar(X, curOwl, color = col, bottom = lastOwl)
            
        lastOwl = curOwl

        counter = counter + 5




plt.show()





