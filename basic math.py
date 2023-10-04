def basic_op(operator, value1, value2):
    x = value1
    y = value2
    if operator == '+':  
        sum = x + y  
        return sum
    if operator == '-':
        sub = x - y  
        return sub
    elif operator == '*':
        mul = x*y
        return mul
    elif operator == '/':
        div = x/y
        return div

print(basic_op('-',15,18))