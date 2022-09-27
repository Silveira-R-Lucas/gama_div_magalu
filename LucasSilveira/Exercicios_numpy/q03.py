import numpy as np


array = np.full([12,4,7], 'D')
array[:,0:4,[0,6]] = 'W' 
array[:,0,0] = 'S'
array[:,-1,-1] = 'E'
array[0,0,0] = 'F'
array[3,2,0] = 'F'
array[3,2,-1] = 'F'
array[4,0,0] = 'F'
array[8,0,0] = 'F'
array[11,1,4] = 'F'
array[10,0,1] = 'F'
array[10,2,0] = 'F'
array[11,3,3] = 'F'

print(array)

