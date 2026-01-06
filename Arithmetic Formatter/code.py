def arithmetic_arranger(expression, show_answer=False):

    num1_list = []
    operator_list = []
    result_list = []
    dash_list = []


    if len(expression) > 5:
        return('Error: Too many problems.')

    for exp in expression:
        left, operator, right = exp.split()

        if operator !=  '+' and operator != '-':
            return("Error: Operator must be '+' or '-'.")
            
        if not left.isdigit() or not right.isdigit():
            return('Error: Numbers must only contain digits.')
          
        if len(str(left)) > 4 or len(str(right)) > 4:
            return('Error: Numbers cannot be more than four digits.')
        
    for exp in expression:
        left, operator, right = exp.split()
        result = eval(str(exp))

        spacing = max(len(left), len(right))+2 

        num1_list.append(f"{left:>{spacing}}")
        operator_list.append(f"{operator}{right:>{spacing-1}}")
        dash_list.append("-"*spacing)
        result_list.append(f"{result:>{spacing}}")

    arranged = "    ".join(num1_list) + "\n" + \
                "    ".join(operator_list) + "\n" + \
                "    ".join(dash_list)

    if show_answer == True:
        arranged += "\n" + "    ".join(result_list)

    return arranged    
