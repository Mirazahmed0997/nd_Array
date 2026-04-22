import numpy as np

arr = np.random.randint(1, 100, size=(100,))

#values greater than 60
values=np.count_nonzero(arr >=40)

#unique values

unique_values,count= np.unique(arr,return_counts=True)
common_values_count=np.count_nonzero(unique_values == 40)


print(unique_values)
print(count)