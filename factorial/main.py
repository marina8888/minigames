# factorial of n is n*(n-1)!
# call a function that multiplies n!


# target is the xth number of fibonacci - number of elements
n = 6
i = 1
result = i

# going up

# while i < n:
#     result=result*(i+1)
#     i+=1
#     print(result)


while i>1:
    result = result*(i-1)
    i-=1
    print(result)




