import time

def function_timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} took {execution_time:.6f} seconds to execute.")
        return result
    return wrapper



@function_timer
def is_vowel(letter):    
    time.sleep(2)
    vowels = "AEIOUaeiou"
    if letter in vowels:
        return True
    else:
        return False
    

user_letter = 'a'
if is_vowel(user_letter):
    print(f"{user_letter} is a vowel.")
else:
    print(f"{user_letter} is not a vowel.")


