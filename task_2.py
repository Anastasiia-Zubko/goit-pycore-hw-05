import re
from typing import Callable

def generator_numbers(text: str):
    numbers = r"\d+\.\d+"  # create a regular expression for all the numbers 
    for number in re.findall(numbers, text): # iterate throgh all the numbers in the txt
        yield float(number) # return the number 
    

def sum_profit(text: str, func: Callable):
    total_sum = sum(func(text)) # get the total sum of numbers found by func in text
    return total_sum # return the total sum 


if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
