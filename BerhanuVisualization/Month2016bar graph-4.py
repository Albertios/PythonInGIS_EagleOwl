
from matplotlib import pyplot as plt
# Create the plot
f, axarr = plt.subplots(1)
# And plot them
x=[152.5562697,231.7387631,405,524.6619699,556.9017974,1125.783207,1080.634669,
643.7510137,377.0599226,441.1225102,261.9883422]
y=["Feb","Mar","Apr","May ","Jun","July","Aug","Sep","Oct","Nov","Dec"]

axarr.bar(y,x)
plt.xlabel('Months ')
plt.ylabel(' Eagle owl flight distance in  2016')
plt.title('Bar graph of Eagle owl flight distance in 2016')
plt.show()