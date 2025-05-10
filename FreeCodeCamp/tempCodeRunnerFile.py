def arithmetic_arranger(problems, show_answers=False):
    #check number of problems
    if len(problems) > 5:
        return('Error: Too many problems')
    elif len(problems) > 0:
        visualization = ''
        #check full numbers & max digits
        for problem in problems:
            operator = ''
            index_operator = -1
            first_number = ''
            second_number = ''
            result = 0
            index_char = 0
            for char in problem:
                #chek existence and right operators
                if char == '+' or char == '-':
                    operator = char
                    index_operator = index_char
                    if index_operator == 0:
                        return('Error: There must be a first operand.')
                    
                #numbers
                elif char.isdigit():
                    if index_operator == -1:  # First number
                        if len(first_number) < 5:
                            first_number += char
                        else:
                            return('Error: Numbers cannot be more than four digits.')
                    else:  # Second number
                        if len(second_number) < 5:
                            second_number += char
                        else:
                            return('Error: Numbers cannot be more than four digits.')
                else: 
                    return ('Error: Numbers must only contain digits.')
                index_char += 1 #Increment

            if index_operator == -1:
                return("Error: Operator must be '+' or '-'.")
            
            if operator == '+':
                result = int(first_number) + int(second_number)
            else:
                result = int(first_number) - int(second_number)

            print(f"{first_number} {operator} {second_number}")
            print(result)
            
        #  32         1      9999      523
        #+  8    - 3801    + 9999    -  49
        #----    ------    ------    -----
        #  40     -3800     19998      474

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
