
import math
import time
import numpy as np
#max_val as the maximum value for the prime
#min_val as the minimum value for the prime

max_val = input("please select up to which number you want to check primes: ")
t1=time.monotonic()
primes_list= np.array([2])
appendable: bool = True
prime_end={1,3,7,9}

# @njit
# def marina(list, )
#     for i in range (2,int(max_val)+1,1):
#     if i % 10 in prime_end:
#         for primes in primes_list[primes_list<math.sqrt(i)]:
#             if i%primes==0:
#                 appendable=False
#         if appendable==True:
#             primes_list=np.append(primes_list, i)
#     appendable=True
# t2=time.monotonic()
# print(primes_list)
# print(t2-t1)