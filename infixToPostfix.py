__author__ = 'ravindra'

"""
this function can convert infix expression to postfix expression
input = infix expression as a form of string
output=return a list of postfix expression
"""
def inToPost(str):
    precedence={"/": 2,"*" : 2,"+" : 1,"-" : 1,"%":2}
    exp=str.split()
    stack =[]
    output=[]
    for item in exp:
        if item == "+" or item == "-" or item == "*" or item == "/" or item=="%":
            if not isEmpty(stack):
                a=stack.pop()
                stack.append(a)
                if precedence[item] < precedence[a]:
                    output.append(stack.pop())
                    stack.append(item)
                else:
                    stack.append(item)
            else:
                stack.append(item)

        else:
            output.append(item)
    length=len(stack)
    while(length):
        length-=1
        output.append(stack.pop())
    return output

def isEmpty(a):
    if len(a)==0:
        return 1
    else:
        return 0

#print(output)
#print(stack)



