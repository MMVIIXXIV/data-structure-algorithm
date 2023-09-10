
def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

Stack = []
postfix_expr = input().split()
for token in postfix_expr:
    if is_number(token):
        # Fill in code here for token being a number
        Stack.append(float(token))
    else:
        # Fill in code here for token not being a number
        if token == '+':
            Stack[len(Stack)-2] = Stack[len(Stack)-2] + Stack[len(Stack)-1]
            del Stack[len(Stack)-1]
        elif token=="x":
            Stack[len(Stack)-2] = Stack[len(Stack)-2] *  Stack[len(Stack)-1]
            del Stack[len(Stack)-1]
        elif token=="/":
            Stack[len(Stack)-2] = Stack[len(Stack)-2] /  Stack[len(Stack)-1]
            del Stack[len(Stack)-1]
        elif token=="-":
            Stack[len(Stack)-2] = Stack[len(Stack)-2] -  Stack[len(Stack)-1]
            del Stack[len(Stack)-1]
        elif token=="%":
            Stack[len(Stack)-2] = Stack[len(Stack)-2] %  Stack[len(Stack)-1]
            del Stack[len(Stack)-1]
        elif token=="^":
            Stack[len(Stack)-2] = Stack[len(Stack)-2] **  Stack[len(Stack)-1]
            del Stack[len(Stack)-1]
            
        

        
print('%.1f' % Stack[0])


        
