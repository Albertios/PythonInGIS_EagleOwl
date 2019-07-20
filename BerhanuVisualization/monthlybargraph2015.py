from matplotlib import pyplot as plt
# Create the plot
f, axarr = plt.subplots(1)
# And plot them
x=[785.57,1016.27,1216,403,371,206.4054915]
y=["May","Jun","July","Aug","Sep","Oct"]
axarr.bar(y,x)
plt.xlabel('Months ')
plt.ylabel(' Eagle owl flight distance in  2015')
plt.title('Bar graph of Eagle owl flight distance in 2015')
plt.show()
