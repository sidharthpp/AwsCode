import numpy as np
import matplotlib.pyplot as plt


a = np.array([(1,2,3),(3,4,5)])

#Dimension of array
print(" Dimension of array ",a.ndim)

#Byte SIze
print(" Byte SIze ", a.itemsize) # Each element Occupies 4 bytes

#Find DataType
print(" DataType ",a.dtype)

#Size of Array
print(" Size of Array ",a.size)

#Shape of Array
print("Shape of Array ", a.shape)  # 2 rows 3 Columns

#Reshape OPeration
print(" Reshape ",a.reshape(3,2))

# Slicing
print("Slicing 1", a[0,1]) # Means Extracting particular element from array
print("Slicing 2", a[1,2])

print("Slicing 3", a[0:,2])  # 0: means all the rows

b = np.array([(1,2,3),(3,4,5),(8,9,10)])
print("Slicing 4", b[0:2,2])

# Line Space

c = np.linspace(1,10,5)
print(" Line Space" , c)


#Maximum value
print("Maximum value", a.max())

#Minimum VaLUE
print("Minimum value", a.min())

#Sum
print("Sum", a.sum())

# AXIS Operation #

print("AXIS Operation : Sum of Columns ",a.sum(axis=0))

print("AXIS Operation : Sum of Rows ",a.sum(axis=1))


# FInd Square Root
print("Square Root", np.sqrt(a))

#Deviation

print(" Deviation ",np.std(a))


#Normal Arithmetic OPeration #

d = np.array([1,2,3])
e = np.array([4,5,6])

print("Add ",d+e)

print("Sub ",d-e)

print("Mul ",d*e)

print("DIvide ",d/e)


#########################

# Concatenate


f = np.array([(1,2,3),(8,9,10)])
g = np.array([(4,5,6),(10,12,14)])

print(" Concatenate : Vertically ",np.vstack((f,g)))

print(" Concatenate : Horizontally ",np.hstack((f,g)))

############################################3
# COnvert multi array into single Line
#print("Single", f.revel())

# NumPy Special Operations
# Cosine , Sine , Tan
# import matplotlib.pyplot

# x & y are Two coordinates
x = np.arange(0,5*np.pi,0.1)

#y = np.sin(x)
y = np.cos(x)

plt.plot(x,y)

#plt.show()


# Exponential Function : e^x

print("Exponential ", np.exp(a))

# Log Function : logx

print(" LOG ",np.log(a))

print(" Log10 ",np.log10(a))


