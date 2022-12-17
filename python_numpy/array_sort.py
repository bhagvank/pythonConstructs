import numpy as np
nd_array = np.array([
 [6, 1, 4],
       [9, 7, 3],
    [12, 2, 5]
    ])
print("sorting the array",np.sort(nd_array))
print("sorting the array with no axis",np.sort(nd_array, axis=None))
print("sorting the array using axis 0",np.sort(nd_array, axis=0))