import numpy as np
from time import time , sleep
import sys

list=[i for i in range(int(1e8))]
array=np.array(list)


list_size=sys.getsizeof(list)
array_size=sys.getsizeof(array)
print(f"list size : {list_size/1000000} Mega bytes")
print(f"array size : {array_size/1000000} Mega bytes")
print((array_size-list_size)/list_size*100)


start = time()
list_sum=sum(list)
end = time()
print(f"\nsummation of list time : {end-start} seconds")


start = time()
array_sum=np.sum(array)
end = time()
print(f"summation of array time : {end-start} seconds")



#   try to use numpy functions with arrays as posible
start = time()
array_sum=sum(array)
end = time()
print(f"summation array using normal method time : {end-start} seconds")



# accessing values and changing it
start = time()
for i in range(len(list)):
    list[i]=1
end = time()
print(f"\nchanging list values time : {end-start} seconds")


start = time()
array[:]=1
end = time()
print(f"changing array values time : {end-start} seconds")
