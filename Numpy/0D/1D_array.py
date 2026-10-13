import numpy as np
list1=[10]
array=np.array(list1)
print(array)


import numpy as hp
list1=[10,20,30,40]
array=hp.array(list1,dtype=float)
array1=hp.array(list1,dtype='U32')
print(array)
print(array1)


import numpy as vp
list1=[10,2.0,30,40,"hello"]
array=vp.array(list1,dtype=object)
print(array)


import numpy as ap
array1= ap.arange(10,21)
print(array1)