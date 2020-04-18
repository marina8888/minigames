
import time
import math

#max_val as the maximum value for the prime
#min_val as the minimum value for the prime

max_val = input("please select up to which number you want to check primes: ")
t1=time.monotonic()


primes_list : list= [3,7]
iter=0
appendable: bool = True
prime_end={1,3,7,9}

for i in range (11,int(max_val),1):
    if i % 10 in prime_end:
        iter = 0
        while primes_list[iter]<math.sqrt(i):
            if i%primes_list[iter]==0:
                appendable=False
            iter += 1
        if appendable==True:
            primes_list.append(i)
        appendable=True
print(primes_list[-1])
t2=time.monotonic()
print(t2-t1)