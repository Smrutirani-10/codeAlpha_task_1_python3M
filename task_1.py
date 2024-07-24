#function of fibonacci generatorcls
def fibonacci_with_list(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series
 
# Example usage:
#Entering the nth Number
num = int(input("Enter the number  : "))

#Result of the fibonacci series initialization
result = fibonacci_with_list(num)

#Result display
print("Fibonacci series with ",num," elements:" ,end=" ")
print(result)