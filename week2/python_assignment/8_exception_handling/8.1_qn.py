def get_exceptions():
    try:
        result = 3 / 0
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")

    try:
        print(value)
    except NameError as e:
        print(f"NameError: {e}")
    
    try:
        my_list = [1, 2, 3]
        print(my_list[10])
    except IndexError as e:
        print(f"IndexError: {e}")

    try:
        my_dict = {"key1": "value1"}
        print(my_dict["key2"])
    except KeyError as e:
        print(f"KeyError: {e}")

    try:
        result = "snake_babu" + 10
    except TypeError as e:
        print(f"TypeError: {e}")

get_exceptions()
