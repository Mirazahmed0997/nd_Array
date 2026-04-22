import numpy as np
x= np.array([10,20,30,70,16])
mat= np.array([[10,20,30,70,16],[12,32,43,23,45]])


index= np.where(x==70)  # returns index
index1= np.where(x<70,x,0) #returns Array
max_val=np.argmax(x)
min_val=np.argmin(x)

mat_index= np.where(mat>16,0,mat)

print(x) 
print(min_val) 
# print(mat_index) 
