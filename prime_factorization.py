from collections import Counter
#https://www.geeksforgeeks.org/python-counter-objects-elements/#
print("Welcome to my prime factorization program!")

def is_prime(n):
    if n<=1:
        return False
    if n ==2:
        return True
    if n % 2 ==0:
        return False
    
    for i in range(3, n//2, 2 ):
        if n%i == 0:
            return False
    
    return True

def exponents(n):
    x = Counter(n)
    list_count = []
    for y in range(len(x)):
        list_count.append(str(list(x.keys())[y]) + "^" + str(list(x.values())[y]) )
        
    return list_count

def prime_factorization(n):
    factors = []
    
    if n<=1:
        return "error, please enter a value greater than 1"
    while True:
        # print(n)
        if n == 0 or n == 1:
            break
        for i in range(2, n+1):
            if n%i == 0:
                if(is_prime(i)):
                    factors.append(i) 
                    n = n//i 
                    break

    # print("prime", factors)
    factors = exponents(factors) 
    return factors
    # unique  = list(set(prime_factors))
    # return unique 
    

input_number = int(input("Enter a number to find its prime factors: "))
print(prime_factorization(input_number))
                