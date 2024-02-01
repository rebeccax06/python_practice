print("Welcome to my prime factorization program!")

def prime_factorization(n):
    factors = []
    composite = True
    
    if n<=1:
        return "not prime"
    for i in range(2, n):
        if n%i == 0:
            factors.append(i)  
    print("initial", factors)    
    prime_factors = [] 
    while composite:
        composite = False
        for x in factors:
            for i in range(2,x):
                if x%i == 0:
                    prime_factors.append(i)
                    print("prime", x , " i: ", i)
                    composite = True

    unique  = list(set(prime_factors))
    return unique 
    
    # prime_factors.sort()
    # print(prime_factors)
    # count = 1;
    # prime_with_count = []
    # for x in range(len(prime_factors)):
    #     if x ==0:
    #         pass
    #     else: 
    #         while prime_factors[x] == prime_factors[x-1]:
    #             x+-1
    #             count += 1
    #         prime_with_count.append(prime_factors[x-1], "^",count)

    # return prime_with_count

input_number = int(input("Enter a number to find its prime factors: "))
print(prime_factorization(input_number))
                