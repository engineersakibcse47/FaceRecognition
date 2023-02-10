from functools import reduce

# Final data structure
numbers = [1, 2, 3, 4, 5,6,7,8,9,10]

def side_effect_free_functions(numbers):
    return list(map(lambda x: x**2, numbers))

def higher_order_functions(numbers, func):
    return list(map(func, numbers))

def functions_as_parameters(numbers, func):
    return func(numbers)

def use_closures(numbers):
    def closure_func(n):
        return n**2
    return list(map(closure_func, numbers))

squared_numbers = side_effect_free_functions(numbers)
print("Squared Numbers:", squared_numbers)

squared_numbers = higher_order_functions(numbers, lambda x: x**2)
print("Squared Numbers using higher-order functions:", squared_numbers)

sum_of_squared_numbers = functions_as_parameters(squared_numbers, lambda x: reduce(lambda a, b: a + b, x))
print("Sum of Squared Numbers using functions as parameters:", sum_of_squared_numbers)

squared_numbers = use_closures(numbers)
print("Squared Numbers using closures:", squared_numbers)
