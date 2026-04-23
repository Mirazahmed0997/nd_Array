import numpy as np

data= np.genfromtxt('st_scores.csv',delimiter=',',skip_header=1)

sliced_data = data[:, 2:]

math_marks=sliced_data[:,:1]
science_marks=sliced_data[:,1:2]
english_marks=sliced_data[:,2:3]
max_math_marks=np.max(math_marks)
min_math_marks=np.min(math_marks)

avg_math_marks=np.mean(math_marks)
median_math_marks=np.median(math_marks)
std_math_marks=np.std(math_marks)



# print(sliced_data)
print("Maximum mark of math : ",max_math_marks)
print("Minimum mark of math : ",min_math_marks)
print("Average mark of math : ",avg_math_marks)
print("Median mark of math : ",median_math_marks)
print("Std mark of math : ",std_math_marks)

