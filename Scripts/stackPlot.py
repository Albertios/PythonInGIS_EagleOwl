
def stackBarPlot(table):
    monthTable = table

    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib
    
    #import colors
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

    oldID = ''
    header = []
    dataset = []
    counter = 1

    data = [0,0,0,0,0,0,0,0,0,0,0,0]
    
    #separate data from id
    for i, item in enumerate(monthTable):
        id = item[0]
        if oldID != id:
            #print(i)
            header.append(id)
            oldID=id
            #counter +=1
            dataset.append(data)
            
            data = [0,0,0,0,0,0,0,0,0,0,0,0]
            
        if oldID == id:
            for x, place in enumerate(data):
                monthNumber = int(item[2])
                if x == monthNumber -1:
                    #print(x ,place, item[2])
                    data[x] = item[3]


    # y axis limitations
    Y_AXIS = [0, 500, 1000,1500, 2000,2500, 3000, 3500]


    matplotlib.rc('font', serif='Helvetica Neue')
    matplotlib.rc('text', usetex='false')
    matplotlib.rcParams.update({'font.size': 40})

    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(18.5, 10.5)

    configs = dataset[0]
    N = len(configs) 
    ind = np.arange(N) + 1
    width = 0.4

    ########stack for loop########
    bottomStack.append(dataset)

    for x, item in enumerate(dataset):
        for i in range(len(dataset[0])):
            
            if x>0:
                
                one = bottomStack[x-1][i]
                two = item[i]
                bottomStack[x][i] =  one + two
            else:
                bottomStack[x][i] = item[i]


    ################################


    p1 = plt.bar(ind, dataset[1], width, color=cnames[44])
    p2 = plt.bar(ind, dataset[2], width, bottom=bottomStack[1], color=cnames[10])
    p3 = plt.bar(ind, dataset[3], width, bottom=bottomStack[2], color= cnames[111])
    p4 = plt.bar(ind, dataset[4], width, bottom=bottomStack[3], color= cnames[33])
    p5 = plt.bar(ind, dataset[5], width, bottom=bottomStack[4], color= cnames[55])
    p6 = plt.bar(ind, dataset[6], width, bottom= bottomStack[5], color=cnames[80])
    p7 = plt.bar(ind, dataset[7], width, bottom=bottomStack[6], color=cnames[77])
    p8 = plt.bar(ind, dataset[8], width, bottom=bottomStack[7], color=cnames[23])
    p9 = plt.bar(ind, dataset[9], width, bottom=bottomStack[8], color=cnames[99])
    p10 = plt.bar(ind, dataset[10], width, bottom=bottomStack[9], color=cnames[7])
    p11 = plt.bar(ind, dataset[11], width, bottom=bottomStack[10], color=cnames[12])
    p12 = plt.bar(ind, dataset[12], width, bottom=bottomStack[11], color=cnames[130])
    p13 = plt.bar(ind, dataset[13], width, bottom=bottomStack[12], color=cnames[133])
    p14 = plt.bar(ind, dataset[14], width, bottom=bottomStack[13], color=cnames[138])
    p15 = plt.bar(ind, dataset[15], width, bottom=bottomStack[14], color=cnames[115])
    p16 = plt.bar(ind, dataset[16], width, bottom=bottomStack[15], color=cnames[125])
    p17 = plt.bar(ind, dataset[17], width, bottom=bottomStack[16], color=cnames[25])
    p18 = plt.bar(ind, dataset[18], width, bottom=bottomStack[17], color=cnames[95])


    plt.title('Compares individual owl flight distance with each other.', fontsize=33)
    plt.xlim([0,13])
    plt.xticks(fontsize=12)
    plt.yticks( Y_AXIS, fontsize=12, rotation=90)
    plt.ylabel('km', fontsize=12)
    plt.xlabel('Month', fontsize=12)
    plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0], p8[0], p9[0], p10[0], 
        p11[0], p12[0], p13[0], p14[0], p15[0], p16[0],p17[0],p18[0]), 
        (header[0], header[1], header[2], header[3], header[4], header[5], header[6], header[7], 
        header[8], header[9], header[10], header[11],header[12], header[13],header[14], 
        header[15],header[16], header[17]), fontsize=12, ncol=1, framealpha=1, fancybox=True)
    plt.show()

    
    