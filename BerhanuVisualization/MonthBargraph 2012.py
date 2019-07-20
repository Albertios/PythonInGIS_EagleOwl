from matplotlib import pyplot as plt
# Create the plot
f, axarr = plt.subplots(1)
# And plot them
x=[155.0624139,216.088007,216.3490667,137.6847495,185.24,171.8145028,134.8799083,87.10716925]
y=["May", "Jun","July","Augest","sep","Oct","Nov","Dec"]
axarr.bar(y,x)
plt.xlabel('Months ')
plt.ylabel('Eagle owl flight distance in  2012')
plt.title('Bar graph of Eagle owl flight distance in 2012')
plt.show()
