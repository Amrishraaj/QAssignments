def concatenate_list_elements(input_list):
    result = ""
    for i in input_list:
        result += str(i)
    return result

list = ["Hello", " ", "World"]
result = concatenate_list_elements(list)
print(result)  

#------------------------------------------------------------#

def find_colors_not_in_list(color_list_1, color_list_2):
    result_set = set()
    for color in color_list_1:
        if color not in color_list_2:
            result_set.add(color)
    return result_set

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
result = find_colors_not_in_list(color_list_1, color_list_2)
print(result)  

