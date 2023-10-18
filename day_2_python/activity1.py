# Function to print arbitrary number of arguments
def arb_args(*args):
    for arg in args:
        print(arg)

# Function with nested functions performing math operations on two integers
def inner_func(x, y):
    def operation1(a, b):
        return a * b
    
    def operation2(a, b):
        return a + b
    
    result = operation1(x, y) + operation2(x, y)
    print(result)

# Function to print student's name and lunch preference
def lunch_lady(name, preference="Mystery Meat"):
    print(f"Student Name: {name}, Lunch Preference: {preference}")

# Function to return sum and product of two integers
def sum_n_product(a, b):
    return a + b, a * b

# Alias for arb_args
alias_arb_args = arb_args

# Function to print average of arbitrary number of integers
def arb_mean(*args):
    if len(args) == 0:
        print("No arguments provided")
    else:
        avg = sum(args) / len(args)
        print(f"The average is: {avg}")

# Function to return the longest string among a set of strings
def arb_longest_string(*args):
    if len(args) == 0:
        return None
    longest = max(args, key=len)
    return longest

# Example usage of the functions
arb_args(1, 2, 3, 4, 5)
inner_func(3, 4)
lunch_lady("John", "Pizza")
lunch_lady("Jane")
sum_result, product_result = sum_n_product(3, 4)
print(f"Sum: {sum_result}, Product: {product_result}")
alias_arb_args(10, 20, 30)
arb_mean(1, 2, 3, 4, 5)
longest_string = arb_longest_string("apple", "banana", "cherry", "date")
print(f"The longest string is: {longest_string}")
