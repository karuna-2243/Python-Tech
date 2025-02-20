import numpy as np 
arr3d = np.array([
    [[1,2,3],[4,5,6]],
      [ [7,8,9],[10,11,12]]
       ])
print(arr3d)
print(arr3d.shape)
print(arr3d[0,1,2])
print(arr3d[1,0,1])
print(arr3d[:,:,1])  
print(arr3d[:,1,:])  #extract the second row from all matrix
print(arr3d[::,-1]) #remove matrix
print(arr3d[1,0,2])
print(arr3d[1,1,2])
print(arr3d[1,0,1])
print(arr3d[1,1,1])

import numpy as np
mat =np.array([[1,2],[3,4]])
print(np.linalg.inv(mat))  #inverse of matrix

import numpy as np 
arr = np.array([[3,1],[3,4]])
print(np.sort(arr,axis=1))   #sorting

import numpy as np 
arr = np.array([1,3,5,7])
print(np.where(arr>3))  #searching

