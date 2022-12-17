import numpy as np
nd_array = np.linspace(4, 50, 24, dtype=int).reshape(4, -1)
print(nd_array)
mask_div_3 = nd_array % 3 == 0
print("mask divisible by 3",mask_div_3)
print(nd_array[mask_div_3])
divisible_by_3 = nd_array[nd_array % 3 == 0]
print("filtered divisible by 3",divisible_by_3)