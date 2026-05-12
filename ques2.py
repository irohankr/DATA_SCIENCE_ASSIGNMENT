# Function to add two numbers
def add_numbers(a, b):
    return a + b


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


lst = list(map(int, input("Enter list elements separated by space: ").split()))


mid_index = len(lst) // 2
mid_value = lst[mid_index]


total = add_numbers(num1, num2)

print("Sum =", total)
print("Middle Value =", mid_value)
if total > mid_value:

    result = set(lst[:mid_index + 1])
    print("Set:", result)

elif total == mid_value:

    result = {mid_index: mid_value}
    print("Dictionary:", result)

else:

    result = tuple(lst[mid_index + 1:])
    print("Tuple:", result)
