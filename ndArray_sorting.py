import numpy as np
x= np.array([10,20,30,70,16])
mat= np.array([[10,20,30,70,16],[12,32,43,23,45]])

sorted_array=np.sort(x)
horizental_sort= np.sort(mat,axis=1)
vertical_sort= np.sort(mat,axis=0)


# z=x.copy()

# z.sort()

print(mat)
print(horizental_sort)
print(vertical_sort)
# print(sorted_array)
# print(x)