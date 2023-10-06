my_list = [1, 'apple', 42, 'banana', 'cherry']

# Define a lambda function to check if an element is an integer or a string
is_int_or_str = lambda x: isinstance(x, (int, str))

# Use the map() function to apply the lambda function to each element in the list
result = all(map(is_int_or_str, my_list))

# Print the result
if result:
    print("All elements in the list are integers or strings.")
else:
    print("Not all elements in the list are integers or strings.")