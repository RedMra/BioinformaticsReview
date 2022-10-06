def fibonacci_loop(number):
    old = 1 
    new = 1 
    for itr in range(number - 1):
        tmpVal = new
        new = old 
        old = old + tmpVal
    return new 

print (fibonacci_loop(10))
