# import numpy as np 
# arrange_arr = np.arrange(0,10,2)
# print(arrange_arr)

# import numpy as np 
# b = np.array([1,2,3])
# c = np.array([4,5,6])
# print(b+c)

# import numpy as np 
# a = np.array([1,2,3])
# b = np. array([4,5,6])
# c = np. array([1, 3, 6])
# print(a+b+c)
# print(b.shape)

import numpy as np 
# a = np.array([1,2,3])
# b = np. array([4,5,6])
# c = np. array([1, 3, 6])
# print(a*b*c)

# a=9
# b=4
# result=a//b #return quotients
# result=a%b #return remainder
# print(result)

# import numpy as np 
# arr = np.array([1,2,3,4])
# print(arr[1])

# import numpy as np 
# arr = np.array([1,2,3,4])
# print(arr[2]+arr[3])

# import numpy as np
# arr = np.array([[1,2,3],[2,4,3],[2,4,6],[3,3,7]])
# print(arr[1,0])

# import numpy as np 
# arr = np.array([[110,120,30,25,65,75],[26,70,85,59,130,75],[45,7989,523,459,111,457]])
# print(arr)
# print(arr[0:2,:-2])
# print(arr[-1:,:-4])
# print(arr[:-1,:-3])
# print(arr[::-1])
# print(arr[::-1,::-1])
# print(arr[1::-1,1::-1])
# print(arr[1::-1])
# print(arr[1,:2])

# import numpy as np 

# arr = np.array([1, 2, 3, 4, 5, 6])  # Define the array
# arr = np.reshape(arr, (2, 3))  # Reshape it into a 2x3 matrix

# print(arr[1, 2])  # Access valid element (row index 1, column index 2)

# import numpy as np 
# a = np.array([23,45,78])
# b = np. array([45,78,89])
# result = np.add(a,b)
# result = np.subtract(b,a)
# result = np.multiply(a,b)
# result = np.divide(b,a)
# print(result)


a = np.array([1,2],[3,4])
b = np.array([5,6],[7,8])
result=np.dot(a,b)