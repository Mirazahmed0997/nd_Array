import numpy as np

arr = np.random.randint(1, 100, size=(10, 5))
# print(arr.shape)
# print(arr)

b= arr.reshape(5,10)
# print(b.shape)
# print(b)

# print(b)

conv_1dim_row= b.flatten()


conv_1dim_col= np.ravel(b,order="F")
# print(conv_1dim_col)



a = np.random.randint(1, 10, size=(2, 3))
b = np.random.randint(20, 30, size=(2, 3))

#concatenate

ab_row_wise= np.concatenate((a,b),axis=0)
ab_col_wise= np.concatenate((a,b),axis=1)

print("a:\n ",a)
print("b :\n",b)
print("ab_row_wise:\n", ab_row_wise)
print("ab_col_wise:\n ",ab_col_wise)





