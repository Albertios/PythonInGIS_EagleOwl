import matplotlib.pyplot as plt
import numpy as np

countries = {'sep': [1405, 7392, 7392], 'Jan': [5862, 9426, 7392], 
             'Feb': [11689, 11339, 7392], 'Mar': [7969, 2987, 7392],
             'Apr': [7969, 5894, 7392],'May': [7969, 1000, 7392],'Jun': [7969, 9000, 7392],'Jul': [7969, 2987, 7392]
             }

c = []
v = []            
for key, val in countries.items():
    c.append(key)
    v.append(val)
v = np.array(v)

plt.bar(range(len(c)), v[:,0])
plt.bar(range(len(c)), v[:,1], bottom=v[:,0])
plt.xticks(range(len(c)), c)
plt.ylabel('Distance')
plt.xlabel('Year')
plt.title('bar_stacked plot of Eagle flight distance(x-axis) and years(y-axis)')
plt.show()