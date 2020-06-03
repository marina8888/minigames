# a prime sieve using the sieve of atkin implementation:

import math
import time

# generates a list of tuples containing all values to check.
# initially all values are False, where 'True' means the value is a prime.
def generate_sieve_list(max_val):
    sieve_list=[]
    for i in range(1,max_val,1):
        sieve_list.append((i, False))
    return sieve_list

# max_val as the value up to which primes are checked

def main():
    max_val = int(input("please select up to which number you want to check primes: "))
    t1=time.monotonic()
    results_list= [2,3,5]
    iter=0
    appendable: bool = True
    # a list of numbers to examine, initally containing all numbers marked as non-prime:
    sieve_list:list = []
    sieve_list=generate_sieve_list(max_val)
    print(sieve_list)
if __name__ == "__main__":
    main()


