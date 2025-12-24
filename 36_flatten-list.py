#comprehension
nested_list=[[1,2],[3,4],[5,6]]
flattened_list=[x for sublist in nested_list for x in sublist]
print(flattened_list)

#itertools.chain()
from itertools import chain
nested_list=[[1,2],[3,4],[5,6]]
flattened_list=list(chain.from_iterable(nested_list))
print(flattened_list)

#sum()
nested_list=[[1,2],[3,4],[5,6]]
flattened_list=sum(nested_list,[])
print(flattened_list)

#numpy.flatten()
import numpy as np
nested_list=[[1,2],[3,4],[5,6]]
flattened_list=np.array(nested_list).flatten()
print(flattened_list)