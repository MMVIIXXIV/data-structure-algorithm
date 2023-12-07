def is_number (string):
    try :
        float(string)
        return True
    except ValueError:
        return False
    
Stack = []
postFix = input().split()

for x in postFix:
    
    if is_number(x):
        Stack.append(float(x)) # if it is a number fill it into stack first
        print(Stack)

    #hello sir, the coplot is off, as you can see, when i hover it , its showing activate. 
    else : # if not number , then it come after number
        if x == "+":
            Stack [ len (Stack)-2] = Stack [ len (Stack)-2] + Stack [len (Stack)-1]
            print("+ called")
            del Stack [len(Stack)-1]
        elif x=="-":
            Stack [ len (Stack)-2] = Stack [ len (Stack)-2] - Stack [len (Stack)-1]
            print("- called")
            del Stack [len(Stack)-1]
        elif x=="*":
            Stack [ len (Stack)-2] = Stack [ len (Stack)-2] * Stack [len (Stack)-1]
            print("x called")
            del Stack [len(Stack)-1]
        elif x=="/":
            Stack [ len (Stack)-2] = Stack [ len (Stack)-2] / Stack [len (Stack)-1]
            print("/ called")
            del Stack [len(Stack)-1]
        elif x=="%":
            Stack [ len (Stack)-2] = Stack [ len (Stack)-2] % Stack [len (Stack)-1]
            print("% called")
            del Stack [len(Stack)-1]
        elif x=="^":
            Stack [ len (Stack)-2] = Stack [ len (Stack)-2] ** Stack [len (Stack)-1]
            print("^ called")
            del Stack [len(Stack)-1]

print('%.1f'% Stack[0])

#input 14 2 /
#output 7.0


'''Best Case:
In the best case, the postfix expression contains only a single operation (e.g., "5 3 +"). 
The code iterates through the expression once, performs the operation, and returns the result. The time complexity is O(N), where N is the number of tokens in the expression.

Average Case:
In the average case, the postfix expression contains multiple operations and operands.
 The code iterates through the expression once, evaluating each operation and operand. The time complexity is O(N), where N is the number of tokens in the expression.

Worst Case:
In the worst case, the postfix expression is complex and contains a large number of operations and operands.
 The code iterates through the expression once, evaluating each operation and operand. The time complexity is still O(N), where N is the number of tokens in the expression.

The time complexity of the code is linear, and it depends on the number of tokens in the postfix expression. 
It does not depend on the specific operations or operands used in the expression. The code processes the expression from left to right, and each token is processed once.
 Therefore, the overall time complexity is O(N), making it an efficient way to evaluate postfix expressions.'''