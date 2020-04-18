
#max_val as the maximum value for the prime
#min_val as the minimum value for the prime

max_val = input("please select up to which number you want to check primes: ")
primes_list = [2]
appendable: bool = True
non_primelist=[2,4,5,6,8,0]
for i in range (3,int(max_val)+1,1):
    if i % 10 in non_primelist:
        i+=1

        for prime in primes_list:
            if i%prime==0:
                appendable=False

        if appendable==True:
            primes_list.append(i)
        appendable=True

print(primes_list)