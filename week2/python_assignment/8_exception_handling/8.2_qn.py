# Custom exception classes
class InvalidNameError(Exception):
    def __init__(self, message="Invalid name"):
        super().__init__(message)


class InvalidAgeError(Exception):
    def __init__(self, message="Invalid age"):
        super().__init__(message)


class InvalidEmailError(Exception):
    def __init__(self, message="Invalid email"):
        super().__init__(message)


class InvalidPhoneNumberError(Exception):
    def __init__(self, message="Invalid phone number"):
        super().__init__(message)


# array to store valid person objects
persons = []


class Person:
    def __init__(self, name, age, email, phone_number):
        self.name = name
        self.age = age
        self.email = email
        self.phone_number = phone_number


def validate_and_add_person(person):
    try:
        if not person.name or not isinstance(person.name, str):
            raise InvalidNameError("Name must be a non-empty string")

        if not isinstance(person.age, int) or person.age <= 0:
            raise InvalidAgeError("Age must be a positive integer")

        if not person.email or "@" not in person.email:
            raise InvalidEmailError("Invalid email format")

        if not person.phone_number or not str(person.phone_number).isdigit():
            raise InvalidPhoneNumberError("Invalid phone number")

        persons.append(person)
        print("Person added successfully!")

    except (InvalidNameError, InvalidAgeError, InvalidEmailError, InvalidPhoneNumberError) as e:
        print(f"Validation Error: {e}")

try:
    person = Person("Sam Anderson", 30, "sam@google.com", "8976534525")

    validate_and_add_person(person)
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("Valid Persons:")
for p in persons:
    print(f"Name: {p.name}, Age: {p.age}, Email: {p.email}, Phone Number: {p.phone_number}")
