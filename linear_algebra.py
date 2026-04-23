import numpy as np

study_hours= np.array([2,4,5,4,3,])
exam_scores= np.array([42,74,85,72,63,])
a= np.array([[2,4,5,4,3,],[2,4,2,5,7]])
b= np.array([[42,74,85,72,63],[3,2,7,9,8]])
c= np.array([[42,74,85],[3,21,7],[3,2,17]])


# data= np.array([study_hours,exam_scores])

# correlation= np.corrcoef(data)

dot_product= np.dot(a,b.T)


print(dot_product)
print(np.linalg.det(c))
print(np.linalg.matrix_rank(c))