#follow this syntax for the homework:
#File: even_sum.py
import numpy as np

def sum_even_numbers(numbers):
    #this function allows us to take the sum of all even numbers in a given list or array
    """
    returns the sum of all even numbers
    in a given list or array.
    Inputs:
    Outputs:
    """
    even_nums = []
    for num in list(numbers):
        if num % 2 == 0:
            even_nums.append(num)
    sum == sum(even_nums)
    return sum