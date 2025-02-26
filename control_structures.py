def is_even(number):
    return number % 2 == 0

user_input = int(input("Enter an integer: "))
if is_even(user_input):
    print(f"{user_input} is even.")
else:
    print(f"{user_input} is odd.")

even_numbers = [num for num in range(1, 51) if is_even(num)]
print("Even numbers from 1 to 50:", even_numbers)

count = 10
while count > 0:
    print(count)
    count -= 1