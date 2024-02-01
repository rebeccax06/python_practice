print("Hello, welcome to my Fibonacci sequence generator!")
print("This program will generate a Fibonacci sequence to the nth number you choose.")


def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    
    if n == 0:
        return "You didn't choose a number!"
    elif n==1:
        return [0]
    elif n==2:
        return [0, 1]
    
    return sequence

    
number = int(input("How many numbers do you want to generate? "))
print(fibonacci(number))