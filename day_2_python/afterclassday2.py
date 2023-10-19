# Write a Python function called max_num()to find the maximum of three numbers.

def max_num (a, b, c):
    return max(a, b, c)


result = max_num(10, 20, 15)
print(f"The maximum of 10, 20, and 15 is: {result}")  # Output: The maximum of 10, 20, and 15 is: 20


# Write a Python function called mult_list() to multiply all the numbers in a list

def mult_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


my_list = [2, 3, 4, 5]
result = mult_list(my_list)
print(f"The product of the numbers in the list is: {result}")  # Output: The product of the numbers in the list is: 120


# Write a Python function called rev_string() to reverse a string

def rev_string(input_str):
    return input_str[::-1]


result = rev_string("Hello, World!")
print(f"The reversed string is: {result}")  # Output: The reversed string is: !dlroW ,olleH



# Write a Python function called num_within() to check whether a number falls in a given range

def num_within(number, start_range, end_range):
    return start_range <= number <= end_range


result1 = num_within(5, 1, 10)
result2 = num_within(15, 1, 10)

print(f"Is 5 within the range of 1 to 10? {result1}")  # Output: Is 5 within the range of 1 to 10? True
print(f"Is 15 within the range of 1 to 10? {result2}")  # Output: Is 15 within the range of 1 to 10? False



# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
def pascal(n):
    def generate_row(prev_row):
        row = [1]
        for i in range(1, len(prev_row)):
            row.append(prev_row[i-1] + prev_row[i])
        row.append(1)
        return row

    triangle = [[1]]
    for _ in range(n-1):
        new_row = generate_row(triangle[-1])
        triangle.append(new_row)

    for row in triangle:
        print(row)

pascal(5)
