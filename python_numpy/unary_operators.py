import numpy as np 
nd_array1 = np.arange(16, dtype = np.float_).reshape(4,4) 

print('First array:', nd_array1) 
  
nd_array2 = np.array([12,12,12,12]) 
print('Second array:',nd_array2)

print('Add the two arrays:',np.add(nd_array1,nd_array2) )
 
print('Subtract the two arrays:',np.subtract(nd_array1,nd_array2))
 
print('Multiply the two arrays:' ,np.multiply(nd_array1,nd_array2) )
  
print('Divide the two arrays:',np.divide(nd_array1,nd_array2))