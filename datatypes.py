integer_var = 10
float_var = 10.5
complex_var = 1 + 2j
list_var = [1, 2, 3, 4, 5]
tuple_var = (1, 2, 3, 4, 5)
dict_var = {'one': 1, 'two': 2, 'three': 3}
set_var = {1, 2, 3, 4, 5}
bool_var = True

print("Type of integer_var:", type(integer_var))
print("Type of float_var:", type(float_var))
print("Type of complex_var:", type(complex_var))
print("Type of list_var:", type(list_var))
print("Type of tuple_var:", type(tuple_var))
print("Type of dict_var:", type(dict_var))
print("Type of set_var:", type(set_var))
print("Type of bool_var:", type(bool_var))

converted_to_float = float(integer_var)
converted_to_int = int(float_var)

print("Integer variable converted to float:", converted_to_float)
print("Float variable converted to integer:", converted_to_int)