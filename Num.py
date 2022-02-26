import numpy as np
import time
import sys
import matplotlib.pyplot as plt

# np.random.seed(0)
#
# A = np.random.randint(10, size=(2, 3))
# print(A)
# # manual creating array
# print('----')
# a = np.array([(1, 2, 3), (4, 5, 6)])
# print(a)
#
# d_list = [[1, 2, 3], [4, 5, 6]]
# d_matrix = np.array(d_list)
# print(d_matrix)
#
# # numpy is better than list because it takes less memory and less time it takes to process data
# my_list = range(1000)
# print(sys.getsizeof(4) * len(my_list))
# b = np.arange(1000)
# print(b.size * b.itemsize)
#
# # numpy array is faster than list
# SIZE = 1000000
# list1 = range(SIZE)
# list2 = range(SIZE)
# A1 = np.arange(SIZE)
# A2 = np.arange(SIZE)
# start = time.time()
# res = [(x, y) for x, y in zip(list1, list2)]
# print((time.time() - start) * 1000)
# start = time.time()
# res = A1 + A2
# print((time.time() - start) * 1000)
#
# # we can find the dimension of array, bite size of each element, we can find the data types of each elements
# # dimensions :
# A = np.random.randint(10, size=(2, 3))
# print(A.ndim)
# B = np.array([(1, 2, 3), (4, 5, 6)])
# print(B.ndim)
#
# # find bite size
# print(A.itemsize)
# print(B.size * B.itemsize)
# # to know the datatype
# print(A.dtype)
# # to find size of an array
# print(A.size)
# # to know the shape
# print(A.shape)
#
# # re-shape of an array [when we change the number of rows with number of columns and vise-versa
# c = np.array([(4, 5, 6), (7, 5, 2)])
# c = c.reshape(3, 2)
# print(c)
# d = np.array([(4, 5, 6), (7, 5, 2)])
# print(d[0:, 2])
# # new thing learned line-space between 2 numbers which represents fractional differences like graph
# a = np.linspace(1, 3, 5)
# print(a)

# # minimum, maximum, sum in numpy arrays
# d = np.array([(4, 5, 6), (7, 5, 2)])
# print(d.max())
# print(d.min())
# print(d.sum())
#
# # axis concept: the rows are called axis 1 and columns are called axis 0
d = np.array([(4, 5, 6), (7, 5, 2)])
print(d.sum(axis=0))
print(d.sum(axis=1))
#
# # finding square root and standard deviation of using numpy
# d = np.array([(4, 5, 6), (7, 5, 2)])
# print(np.sqrt(d))
# print(np.std(d))
#
# # matrix operation like addition, subtraction, multiplication, division
# d = np.array([(4, 5, 6), (7, 5, 2)])
# a = np.array([(1, 2, 3), (4, 5, 6)])
# print(d+a)
# print(d-a)
# print(d*a)
# print(d/a)
#
# # special multiplication
# a = np.array([(1, 2, 3), (4, 5, 6)])
# f = np.array([(1, 2, 3), (4, 5, 2), (1, 3, 2)])
# result = np.matmul(a, f)
# print(result)

# concatenate two matrix is also possible in two ways vertical and horizontal standing
s = np.array([(4, 5, 6), (7, 5, 2)])
p = np.array([(1, 2, 3), (4, 5, 6)])
print(np.vstack((s, p)))
print(np.hstack((s, p)))

# if we want to convert a matrix just into a single column
s = np.array([(4, 5, 6), (7, 5, 2)])
print(np.ravel(s))

# numpy special functions
# for drawing sin and cosine graph we have to import matplotlib
x = np.arange(0, 3*np.pi, 0.1)
y = np.sin(x)
plt.plot(x, y)
# plt.show()
z = np.cos(x)
plt.plot(x, z)
plt.show()
p = np.tan(x)
plt.plot(x, p)
# plt.show()

# exponential and logarithmic function using numpy e = 2.7... we can log it will be log base 10 and
# when we call natural log it will be log base e we will call it as ln
# for exponential
ar = np.array([(1, 2, 3)])
print(np.exp(ar))
# for natural log which log base e
print(np.log(ar))
# for log base 10
print(np.log10(ar))

