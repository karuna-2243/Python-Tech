import numpy as np
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([[1,2,3],[4,5,6]])
arr3 = np.array([[1,2],[3,4],[5,6],[7,8]])
print(arr1)
print(arr2)
print(arr3)


import numpy as np
zeros_arr = np.zeros((3,3))
ones_arr = np.ones((2,4))
rand_arr = np.random.rand(3,3)
full_arr = np.full((2,2),9)
print(zeros_arr)
print(ones_arr)
print(rand_arr)
print(rand_arr)

import numpy as np
arr = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(arr[0,1])
print(arr[2,2])
print(arr[:,1])
print(arr[1:,:2])

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
reshaped = arr.reshape((5,1))
print(reshaped)
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.vstack((a,b)))
print(np.hstack((a,b)))

import numpy as np
arr = np.array([10,20,30,40,50])
filtered_arr = arr[arr > 25]
print(filtered_arr)
bool_index = (arr % 20 == 0)
print(arr[bool_index])

import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
print(arr1 + arr2)
print(arr1 * arr2)
print(np.exp(arr1))
print(np.sqrt(arr2))

import numpy as np
arr = np.array([[1,2],[3,4]])
print(arr.T)
arr2 = np.array([[5,6],[7,8]])
print(np.dot(arr,arr2))
unsorted = np.array([3,1,2,5,4])
print(np.sort(unsorted))g