def caching_fibonacci():
    cache = {} # creating an empty dict to store the results
    def fibonacci(n):  # create inner function fibonacci
        if n<=0: # if the number is smaller or equals 0 
            return 0 # return 0
        elif n==1: # if the number equals 1
            return 1 # return 1
        elif n in cache: # if the number is present in the dict
            return cache[n] # return the number 
        else: # if the number is not present in cache we calculate it recursively 
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2) # calculate the number recursively
            return cache[n]  # return the calculated number     
    return fibonacci # return inner function fibonacci


if __name__ == "__main__":
    # Отримуємо функцію fibonacci
    fib = caching_fibonacci()

    # Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
    print(fib(10))  # Виведе 55
    print(fib(15))  # Виведе 610

