import numpy as np
nd_array = np.array([
      [16, 31, 2, 13],
       [15, 10, 11, 8],
       [91, 6, 7, 12],
   [41, 15, 14, 12]
   ])

for i in range(4):
        print("row sum", nd_array[:, i].sum())
        print("column sum",nd_array[i, :].sum())
