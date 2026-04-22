import numpy as np

mat= np.random.randint(30,100, size=(10,))

splited_array= np.array_split(mat,3)

transpose= mat.T

print(splited_array)
# print(transpose)