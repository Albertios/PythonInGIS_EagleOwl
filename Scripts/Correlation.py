import numpy as np
import numpy.ma as ma


x = []
y = []


#print(ma.corrcoef(ma.masked_invalid(x), ma.masked_invalid(z)))




autocorrelation = []

for i in range(len(lines)):
    x = lines[i-1]

    for j in range(len(lines)-1):
        if i != j:
            y = lines[j-1]
        
            correlation = ma.corrcoef(ma.masked_invalid(x), ma.masked_invalid(y))
            
            #print(correlation)
            #print(correlation[0])
            #print(correlation[1])
            
            
            autocorrelation.append(correlation)
    autocorrelation.append([])
    


owls = ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec"]


sum = 0.0
c = 0

for i in autocorrelation:
    
    val = i[1][0]
    
    if val != "--" and val > 0.0 :
       sum = sum + val
       c +=1

 
    
for i in autocorrelation:
    print(i)

    
    
    
    
    
    
    
    
    
    
    