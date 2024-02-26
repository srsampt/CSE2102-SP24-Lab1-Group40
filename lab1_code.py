class NumStorage:
    def __init__(self):
        self.number = [0] * 100                             # list containing 100 zeros, which will be used to store numbers
        self.top = -1                                       # initializes top to -1, used to keep track of the top element of the stack

class SymbolStorage:
    def __init__(self):              
        self.symbol = [''] * 100                            # list containing 100 empty strings, which will be used to store symbols
        self.top = -1                                       # initializes top to -1, used to keep track of the top element of the stack

def init_operate_num(stack_num):
    stack_num.top = -1                                      # reset top attribute of stack_num object to -1, effectively resetting the stack

def init_operate_symbol(stack_symbol):  
    stack_symbol.top = -1                                   # reset top attribute of stack_symbol object to -1, effectively resetting the stack

def in_num_storage(stack_num, num):                         ### PUSH method for NumStorage
    stack_num.top += 1                                      # increment self.top
    stack_num.number[stack_num.top] = num                   # assign the value to the corresponding index in the stack

def in_symbol_storage(stack_symbol, ch):                    ### PUSH method for SymbolStorage
    stack_symbol.top += 1                                   # increment self.top
    stack_symbol.symbol[stack_symbol.top] = ch              # assign the value to the corresponding index in the stack

    
def read_num_storage(stack_num):                            ### PEEK method for NumStorage
    return stack_num.number[stack_num.top]                  # return top item of stack without removing it

def read_symbol_storage(stack_symbol):                      ### PEEK method for SymbolStorage
    return stack_symbol.symbol[stack_symbol.top]            # return top item of stack without removing it

def get_num_data(stack_num):                                ### POP method for NumStorage
    num = stack_num.number[stack_num.top]                   # remove the TOP item of the stack
    stack_num.top -= 1
    return num

def get_symbol(stack_symbol):                               ### POP method for SymbolStorage
    symbol = stack_symbol.symbol[stack_symbol.top]          # remove the TOP item of the stack
    stack_symbol.top -= 1
    return symbol

def judge_symbol_priority(ch):                              ### ORDER OF OPERATIONS - assigning priorities for mathematical symbols used in an expression 
    if ch == '(':
        return 1
    elif ch == '+' or ch == '-':
        return 2
    elif ch == '*' or ch == '/':
        return 3
    elif ch == ')':
        return 4

def math(v1, v2, c):                                        ### performs basic arthimetic operations based on the given operator and returns the result
    if c == '+':
        return v1 + v2
    elif c == '-':
        return v1 - v2
    elif c == '*':
        return v1 * v2
    elif c == '/':
        return v1 / v2

def main():                                                     ### where the main computation is occurring
    
    print("Enter the expression (no blank, no decimals): ")         # prompts the user to enter an expression
    data = NumStorage()                                             # initialize instance of NumStorage
    symbol = SymbolStorage()                                        # initialize instance of SymbolStorage
    init_operate_num(data)                                          # initialize the top index of the stack to -1 -- ensure stack is empty before any operations are performed
    init_operate_symbol(symbol)                                     # initialize the top index of the stack to -1 -- ensure stack is empty before any operations are performed
    
    
    # t is used as an index to keep track of the current position within the array v
    # v is used to temporarily store characters from the input string - TEMPORARY LIST
    i = t = sum_val = 0                                             # simultaneously initialize three variables to 0 (shorthand to assign same initial value to multiple variables)
    
    v1 = v2 = 0                                                     # same as above
    c = ''                                                          # initialize to an empty string
    i = t = sum_val = 0                                             # redundant? doing the same thing as line 68?
    v = [''] * 100                                                  # initialize a list with 100 elements (each initialized to an empty string)
    
    
    user_input = input()                                            # take user input
    for i in range(len(user_input)):                                # read the user input character by character
        
        # CASE 1 - does the input expression start with a negative number?
        if i == 0 and user_input[i] == '-':                                                     # if the 1st character is minus sign -- read the num and store it in NumStorage
            v[t] = user_input[i]
            t += 1
        
        # CASE 2 - is the current character an opening parenthesis and is the next character a minus sign? (and makes sure we're not at the end of the input string)
        elif user_input[i] == '(' and i + 1 < len(user_input) and user_input[i + 1] == '-':      
            i += 1                                                                              # we know that the current character is a (, so skip to the next char, which is the minus sign
            v[t] = user_input[i]                                                                # add that next character (the minus sign) to the v list
            t += 1                                                                              # move to the next position in the v list (by incrementing t)
            
            # while loop continues as long as the index i is within the bounds of the input string and the current character is a digit
            while i < len(user_input) and user_input[i] >= '0' and user_input[i] <= '9':        
                v[t] = user_input[i]                                                            # append the current digit character to the v list at position t
                t += 1                                                                          # increment t to prepare for the next character
                i += 1                                                                          # increment i to move to the next character in the user input
            # once all of the digits of the negative num have been collected, convert the list v into an integer
            # then PUSH this negative num to the NumStorage stack
            in_num_storage(data, int(''.join(v)))    

            # while loop to reset the temporary list v                                           
            while t > 0:
                v[t] = ''                                                                       # clear the element at position t in v
                t -= 1                                                                          # decrement t to move to the prev position in v
            
            # check that the for loop has not reached the end of the user string and that the current character is not a closing parenthesis
            if i < len(user_input) and user_input[i] != ')':                                    
                i -= 1                                                                          # decrement i by 1
                in_symbol_storage(symbol, '(')                                                  # PUSH an opening parenthesis to SymbolStorage

        
        # CASE 3 - is the current character a digit? (and makes sure we're not at the end of the input string)
        elif i < len(user_input) and user_input[i] >= '0' and user_input[i] <= '9':

            # while loop continues as long as the index i is within the bounds of the input string and the current character is a digit
            while i < len(user_input) and user_input[i] >= '0' and user_input[i] <= '9':
                v[t] = user_input[i]                                                            # append the current digit character to the v list at position t
                t += 1                                                                          # increment t to prepare for the next character
                i += 1                                                                          # increment i to move to the next character in the user input
            
            # once all of the digits of the negative num have been collected, convert the list v into an integer
            # then PUSH this negative num to the NumStorage stack
            in_num_storage(data, int(''.join(v)))

            # while loop to reset the temporary list v 
            while t > 0:
                v[t] = ''
                t -= 1
            
            # decrement i by 1, to ensure that the next iration of the main loop handles the next character correctly
            # since the current character is not part of the number, we need to revisit it in the next iteration
            i -= 1


        # CASE 4 - is the current character a symbol? 
        else:
            if symbol.top == -1:                                                    # check if the SymbolStorage stack is empty (i.e. its top index is -1)
                in_symbol_storage(symbol, user_input[i])                                # PUSH the current symbol to the SymbolStorage stack
            elif judge_symbol_priority(user_input[i]) == 1:                         # check if the priority of the current symbol is 1, indicating a (
                in_symbol_storage(symbol, user_input[i])                                # PUSH the ( to the SymbolStorage stack
            elif judge_symbol_priority(user_input[i]) == 2:                         # check if the priority of the current symbol is 2, indicating either a + or -
                if judge_symbol_priority(read_symbol_storage(symbol)) == 1:             # check if the element at the top of the SymbolStorage stack is a (
                    in_symbol_storage(symbol, user_input[i])                                # PUSH the +/- to the SymbolStorage stack
                elif judge_symbol_priority(read_symbol_storage(symbol)) == 2:           # check if the element at the top of the SymbolStorage stack is a + or -
                    
                    # while loop continues while there are at least two numbers in NumStorage stack
                    # perform + or - operations on the top two numbers using the top symbol
                    # then store the result back in the NumStorage stack
                    while symbol.top >= 0 and data.top >= 1:                                
                        v2 = get_num_data(data)
                        v1 = get_num_data(data)
                        sum_val = math(v1, v2, get_symbol(symbol))
                        in_num_storage(data, sum_val)
                    in_symbol_storage(symbol, user_input[i])
                elif judge_symbol_priority(read_symbol_storage(symbol)) == 3:
                    while symbol.top >= 0 and data.top >= 1:
                        v2 = get_num_data(data)
                        v1 = get_num_data(data)
                        sum_val = math(v1, v2, get_symbol(symbol))
                        in_num_storage(data, sum_val)
                    in_symbol_storage(symbol, user_input[i])

            elif judge_symbol_priority(user_input[i]) == 3:
                if judge_symbol_priority(read_symbol_storage(symbol)) == 1:
                    in_symbol_storage(symbol, user_input[i])
                elif judge_symbol_priority(read_symbol_storage(symbol)) == 2:
                    in_symbol_storage(symbol, user_input[i])
                elif judge_symbol_priority(read_symbol_storage(symbol)) == 3:
                    while symbol.top >= 0 and data.top >= 1:
                        v2 = get_num_data(data)
                        v1 = get_num_data(data)
                        sum_val = math(v1, v2, get_symbol(symbol))
                        in_num_storage(data, sum_val)
                    in_symbol_storage(symbol, user_input[i])
            elif judge_symbol_priority(user_input[i]) == 4:
                while symbol.top >= 0 and judge_symbol_priority(read_symbol_storage(symbol)) != 1:
                    v2 = get_num_data(data)
                    v1 = get_num_data(data)
                    sum_val = math(v1, v2, get_symbol(symbol))
                    in_num_storage(data, sum_val)
                get_symbol(symbol)
    while symbol.top != -1:
        v2 = get_num_data(data)
        v1 = get_num_data(data)
        sum_val = math(v1, v2, get_symbol(symbol))
        in_num_storage(data, sum_val)
    print("The result is: ", data.number[0])

main()


