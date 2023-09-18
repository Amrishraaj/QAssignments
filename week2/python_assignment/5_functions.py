def compute_gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

num1 = 48
num2 = 18
gcd = compute_gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {gcd}.")

#--------------------------------------------

def compute_expression_result(x, y):
    result = (x + y) * (x + y)
    return result

x_value = 5
y_value = 3
result = compute_expression_result(x_value, y_value)
print(f"The result of ({x_value} + {y_value}) * ({x_value} + {y_value}) is {result}.")
