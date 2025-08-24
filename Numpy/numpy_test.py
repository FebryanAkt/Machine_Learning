import numpy as np

# --------- matrix ---------
a = np.array([1,2,3,4,5]) #default
b = np.arange(1,10,2) #range
c = np.linspace(1,10,5)  #linspace
d = np.array([(1,2,3) , (4,5,6)]) #matrix
e = np.zeros((3,3)) #matrix 0
f = np.identity(5) #matrix identitas
g = np.eye(5) #matrix identitas

# --------- perkalian matrix ---------
h = np.array(([1,2], [4,5]))
i = np.ones((2,2))
hasilKali = np.dot(h,i)

# --------- transpose matrix ---------
j = np.array(([1,2,3], [4,5,6]))
# print(j.transpose())
# print(np.transpose(j))

# --------- vektor baris ---------
print(j.ravel())
print(np.ravel(j))

# --------- reshape matrix ---------
print(j.reshape(3,2))

# print (j)