'''
1] Given the below code
snippet, answer the following questions.

def num_square(num):
    square = num * num
    return square

input_num = 121

if input_num > 100:
    result = num_square(5)
    
print(result)
'''

#--------------------------------------------

''' 
Qn: What is the scope of num,
 square, input_num, result?
 
-> num,square, are local variables and defined within function
-> input_num, result are global variables and defined outside function

'''

#--------------------------------------------

'''
QN: What is the lifetime of each
variable? When will they be created and destroyed?

-> num,square are created when function is called and destroyed when function is returned
-> input_num, result are created when program starts and destroyed when program ends

'''

#--------------------------------------------

'''
Qn: What would happen if
input_num had a value of less than 100?

-> If input_num is less than 100, the condition input_num > 100 will be False, and the code block inside the if statement will not be executed.
'''

#--------------------------------------------

'''
QN: What would be the scope and
value of `result` if input_num has a value of less than 100?

If input_num is less than 100, result will not be assigned a value.
Since result has no default value assigned outside of the if block, it will not exist, and trying to print it will result in a NameError.

'''