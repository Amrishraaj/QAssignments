def add_is_to_string(input_string):
    if input_string.startswith("Is"):
        return input_string
    else:
        return "Is" + input_string

given_string = input("Enter a string: ")
result = add_is_to_string(given_string)
print(result)

#--------------------------------------------

def check_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

user_number = int(input("Enter a number: "))
result = check_even_or_odd(user_number)
print(f"The number {user_number} is {result}.")

#--------------------------------------------

def is_vowel(letter):
    vowels = "AEIOUaeiou"
    if letter in vowels:
        return True
    else:
        return False

user_letter = input("Enter a letter : ")
if is_vowel(user_letter):
    print(f"{user_letter} is a vowel.")
else:
    print(f"{user_letter} is not a vowel.")

