import numpy as np
import numpy.ma as ma


np.random.seed(1)

# 1000 random integers between 0 and 50
x = lines[3]

# Positive Correlation with some noise
y = lines[16]


#print(ma.corrcoef(ma.masked_invalid(x), ma.masked_invalid(z)))




autocorrelation = []

for i in range(len(lines)-1):
    x = lines[i]
    
    for j in range(len(lines)-1):
        if i != j:
            y = lines[j]
        
            correlation = ma.corrcoef(ma.masked_invalid(x), ma.masked_invalid(y))
            
            #print(correlation)
            #print(correlation[0])
            #print(correlation[1])
            
            
            autocorrelation.append(correlation)
        


owls = ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec"]

plt.scatter(autocorrelation[2], months)
plt.show()


for i in autocorrelation
    print(i)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    