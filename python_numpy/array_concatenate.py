import numpy as np
nd_array1 = np.array([
       [5, 9],
      [16, 10]
    ])
nd_array2 = np.array([
      [13, 15],
       [71, 27],
    ])

print("hstack",np.hstack((nd_array1, nd_array2)))
print("vstack",np.vstack((nd_array2, nd_array1)))
print("concatenate",np.concatenate((nd_array1, nd_array2)))
print("concatenate with no axis",np.concatenate((nd_array1, nd_array2), axis=None))