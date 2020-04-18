
#max_val as the maximum value for the prime
#min_val as the minimum value for the prime
min_val=input("please select up from which number you want to check primes: ")
max_val=input("please select up to which number you want to check primes: ")
primes_list=[2]
appendable=True
for i in range (int(min_val),int(max_val)+1,1):
    for prime in primes_list:
        if i%prime==0:
            appendable=False

    if appendable==True:
        primes_list.append(i)
    appendable=True

print(primes_list)