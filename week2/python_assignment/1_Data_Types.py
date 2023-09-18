def mini_string(input_string):
    if len(input_string) < 2:
        return ""
    else:
        return input_string[:2] + input_string[-2:]


print(mini_string('w3resource'))  
print(mini_string('w3'))  
print(mini_string('w'))  

#--------------------------------------------

def get_largest_number(numbers_list):
    if len(numbers_list) == 0:
        return None
    else:
        return max(numbers_list)


print(get_largest_number([10, 20, 5, 40])) 

#--------------------------------------------


def concatenate_dictionaries(*dictionaries):
    result = {}
    for dictionary in dictionaries:
        result.update(dictionary)
    return result

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result_dict = concatenate_dictionaries(dic1, dic2, dic3)
print(result_dict)  


