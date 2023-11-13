
def factorial(num):
    if(num == 0 or num ==1):
        return 1
    else:
        return(num * factorial(num-1))


print(factorial(5))  
print(factorial(3))  

def fibonacci(num):
    if(num ==0):
        return 0
    elif(num == 1):
        return 1
    elif(num == 2):
        return(fibonacci(1)+fibonacci(0))
    else:
        return(fibonacci(num-1)+fibonacci(num-2))
    
print(fibonacci(6))