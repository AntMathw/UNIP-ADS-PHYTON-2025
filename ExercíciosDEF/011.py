#Sequência de Fibonacci

def fibonacci_recursive(n):
    
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

num_terms = 10
for i in range(num_terms):
    print(fibonacci_recursive(i), end=" ")





