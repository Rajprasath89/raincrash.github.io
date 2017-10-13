
#load the library and check its version, just to make sure we aren't using an older version


import numpy as np
np.__version__
'1.12.1'


#create a list comprising numbers from 0 to 9
L = list(range(10))


# Converting integers to string - this style of handling lists is known as list comprehension.
# List comprehension offers a versatile way to handle list manipulations tasks easily. 
# We'll learn about them in future tutorials. Here's an example.  

[str(c) for c in L]
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

[type(item) for item in L]
[int, int, int, int, int, int, int, int, int, int]


#creating arrays
np.zeros(10, dtype='int')
array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


#creating a 3 row x 5 column matrix
np.ones((3,5), dtype=float)
array([[ 1.,  1.,  1.,  1.,  1.],
      [ 1.,  1.,  1.,  1.,  1.],
      [ 1.,  1.,  1.,  1.,  1.]])


#creating a matrix with a predefined value
np.full((3,5),1.23)
array([[ 1.23,  1.23,  1.23,  1.23,  1.23],
      [ 1.23,  1.23,  1.23,  1.23,  1.23],
      [ 1.23,  1.23,  1.23,  1.23,  1.23]])


#create an array with a set sequence
np.arange(0, 20, 2)
array([0, 2, 4, 6, 8,10,12,14,16,18])


#create an array of even space between the given range of values
np.linspace(0, 1, 5)
array([ 0., 0.25, 0.5 , 0.75, 1.])


#create a 3x3 array with mean 0 and standard deviation 1 in a given dimension
np.random.normal(0, 1, (3,3))
array([[ 0.72432142, -0.90024075,  0.27363808],
      [ 0.88426129,  1.45096856, -1.03547109],
      [-0.42930994, -1.02284441, -1.59753603]])


#create an identity matrix
np.eye(3)
array([[ 1.,  0.,  0.],
      [ 0.,  1.,  0.],
      [ 0.,  0.,  1.]])


#set a random seed
np.random.seed(0)


x1 = np.random.randint(10, size=6) #one dimension
x2 = np.random.randint(10, size=(3,4)) #two dimension
x3 = np.random.randint(10, size=(3,4,5)) #three dimension


print("x3 ndim:", x3.ndim)
print("x3 shape:", x3.shape)
print("x3 size: ", x3.size)
('x3 ndim:', 3)
('x3 shape:', (3, 4, 5))
('x3 size: ', 60)


x1 = np.array([4, 3, 4, 4, 8, 4])
x1
array([4, 3, 4, 4, 8, 4])

#assess value to index zero
x1[0]
4

#assess fifth value
x1[4]
8

#get the last value
x1[-1]
4

#get the second last value
x1[-2]
8

#in a multidimensional array, we need to specify row and column index
x2
array([[3, 7, 5, 5],
      [0, 1, 5, 9],
      [3, 0, 5, 0]])


#1st row and 2nd column value
x2[2,3]
0

#3rd row and last value from the 3rd column
x2[2,-1]
0


#replace value at 0,0 index
x2[0,0] = 12
x2
array([[12,  7,  5,  5],
      [ 0,  1,  5,  9],
      [ 3,  0,  5,  0]])


x = np.arange(10)
x
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


#from start to 4th position
x[:5]
array([0, 1, 2, 3, 4])


#from 4th position to end
x[4:]
array([4, 5, 6, 7, 8, 9])


#from 4th to 6th position
x[4:7]
array([4, 5, 6])


#return elements at even place
x[ : : 2]
array([0, 2, 4, 6, 8])


#return elements from first position step by two
x[1::2]
array([1, 3, 5, 7, 9])


#reverse the array
x[::-1]
array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

#You can concatenate two or more arrays at once.
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
z = [21,21,21]
np.concatenate([x, y,z])
array([ 1,  2,  3,  3,  2,  1, 21, 21, 21])


#You can also use this function to create 2-dimensional arrays.
grid = np.array([[1,2,3],[4,5,6]])
np.concatenate([grid,grid])
array([[1, 2, 3],
      [4, 5, 6],
      [1, 2, 3],
      [4, 5, 6]])


#Using its axis parameter, you can define row-wise or column-wise matrix
np.concatenate([grid,grid],axis=1)
array([[1, 2, 3, 1, 2, 3],
      [4, 5, 6, 4, 5, 6]])



x = np.array([3,4,5])
grid = np.array([[1,2,3],[17,18,19]])
np.vstack([x,grid])
array([[ 3,  4,  5],
      [ 1,  2,  3],
      [17, 18, 19]])


#Similarly, you can add an array using np.hstack
z = np.array([[9],[9]])
np.hstack([grid,z])
array([[ 1,  2,  3,  9],
      [17, 18, 19,  9]])

x = np.arange(10)
x
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


x1,x2,x3 = np.split(x,[3,6])
print x1,x2,x3
[0 1 2] [3 4 5] [6 7 8 9]

grid = np.arange(16).reshape((4,4))
grid
upper,lower = np.vsplit(grid,[2])
print (upper, lower)
(array([[0, 1, 2, 3],
       [4, 5, 6, 7]]), array([[ 8,  9, 10, 11],
       [12, 13, 14, 15]]))




