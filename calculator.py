def apply_operator(operators, values):
    
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    
    if operator == '+':
        values.append(left + right)
    elif operator == '-':
        values.append(left - right)
    elif operator == '*':
        values.append(left * right)
    elif operator == '/':
        if right == 0:
            raise ValueError("Ошибка: деление на ноль")
        values.append(left / right)


def precedence(op):
    
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0


def evaluate_expression(expression):
    values = []  
    operators = []  

    i = 0  
    while i < len(expression):
        char = expression[i]

        
        if char == ' ':
            i += 1
            continue

        
        if char.isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])  
                i += 1
            values.append(num)
        
        
        elif char == '(':
            operators.append(char)
            i += 1
        
        
        elif char == ')':
            while operators and operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop() 
            i += 1
        
        
        else:
            
            while operators and precedence(operators[-1]) >= precedence(char):
                apply_operator(operators, values)
            operators.append(char)  
            i += 1

    
    while operators:
        apply_operator(operators, values)

    return values[-1]


expression = "2 + (3 * 4) - 5 / (1 + 1)"
try:
    result = evaluate_expression(expression)
    print(f"Результат: {result}")
except Exception as e:
    print(f"Ошибка: {e}")
