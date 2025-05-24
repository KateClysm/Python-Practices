def arithmetic_arranger(problems, show_answers=False):
    #check number of problems
    if len(problems) > 5:
        return('Error: Too many problems.')
    elif len(problems) > 0:
        first_operands = []
        second_operands = []
        lines = []
        results = []

        for problem in problems:
            problem_parts = problem.split()
            if len(problem_parts) != 3:
                return "Error: Invalid problem format"
            
            #assignations
            first_number = problem_parts[0]
            operator = problem_parts[1]
            second_number = problem_parts[2]

            #validation checks
            if not first_number.isdigit() or not second_number.isdigit():
                return "Error: Numbers must only contain digits."
            if operator not in ["+", "-"]:
                return "Error: Operator must be '+' or '-'."
            if len(first_number) > 4 or len(second_number) > 4:
                return "Error: Numbers cannot be more than four digits."
            
            # width of largest number plus spaces
            width = max(len(first_number), len(second_number)) + 2
            #assignations of elements for each row
            first_operands.append((' ' * (width - len(first_number))) + first_number)
            second_operands.append(operator + ' ' + (' ' * (width - len(second_number) - 2)) + second_number)
            lines.append('-' * width)

            if operator == '+':
                result = str(int(first_number) + int(second_number))
                results.append(' ' * (width - len(result)) + result) 
            else:
                result = str(int(first_number) - int(second_number))
                results.append(' ' * (width - len(result)) + result) 

        #construction of rows
        arrange = '\n'.join([
            '    '.join(first_operands),
            '    '.join(second_operands),
            '    '.join(lines)
        ])

        if show_answers:
            arrange += '\n' + '    '.join(results)
        
        return arrange


print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
#          32         1      9999      523
        #+  8    - 3801    + 9999    -  49
        #----    ------    ------    -----
        #  40     -3800     19998      474

#---------------------------------------------------------------------------------------        

print(arithmetic_arranger(["3801 - 2", "123 + 49"]) )
#should return    3801      123
#               -    2    +  49
#               ------    -----.
#PASSES

print(arithmetic_arranger(["1 + 2", "1 - 9380"]) )
#should return   1         1
#              + 2    - 9380
#              ---    ------.
#PASSES

print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]) )
#should return     3      3801      45      123
#              + 855    -    2    + 43    +  49
#              -----    ------    ----    -----.
#PASSES

print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]) )
#should return   11      3801      1      123         1
#              +  4    - 2999    + 2    +  49    - 9380
#              ----    ------    ---    -----    ------.
#PASSES

#---------------------------------------------------------------------------------------

print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]) )
#should return 'Error: Too many problems.'.
#PASSES

print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]) )
#should return "Error: Operator must be '+' or '-'.".
#PASSES

print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]) )
#should return 'Error: Numbers cannot be more than four digits.'.
#PASSES

print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]) )
#should return 'Error: Numbers must only contain digits.'.
#PASSES

print(arithmetic_arranger(["3 + 855", "988 + 40"], True) )
#should return     3      988
#              + 855    +  40
#              -----    -----
#                858     1028
#PASSES

print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True) )
#should return    32         1      45      123      988
#              - 698    - 3801    + 43    +  49    +  40
#              -----    ------    ----    -----    -----
#               -666     -3800      88      172     1028.
#PASSES
