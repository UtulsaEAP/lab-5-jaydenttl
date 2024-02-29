'''
Name: Jayden Ly
Lab time: thursday 11:43 am
'''
def int_to_reverse_binary(user_input):
    binary_val = ''
#write your while loop here
    while user_input > 0:
        moduloed = user_input %2
        binary_val = binary_val + str(moduloed)
        user_input = user_input // 2
    return binary_val;


def string_reverse(input_string): 
    reverse_input = ''
    for i in input_string:
        reverse_input = input_string [::-1]
    return reverse_input

if __name__ == '__main__':
    user_input = int(input())
    
    binary_string = str(int_to_reverse_binary(user_input))
    binary_string = str(string_reverse(binary_string))
    
    print(binary_string)