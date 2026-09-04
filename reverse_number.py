# Python Program to Reverse a Number

def reverse_number(n):
    return int(str(n)[::-1])

# Example usage
number = 12345
reversed_number = reverse_number(number)
print(f'Reversed Number: {reversed_number}')