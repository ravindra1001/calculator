__author__ = 'ravindra'

"""
this function can evaluate postfix expration

input = a list in postfix
output= resutant value in string form

"""
def evaluate(exp):
    #exp=["1","2","/"]
    st=[]
    for item in exp:
        if item=="+" or item=="-" or item=="*" or item=="/" or item=="%":
            a=st.pop()
            b=st.pop()
            result=0
            if item == "+":
                result=float(b) + float(a)
            elif item == "-":
                result=float(b) - float(a)
            elif item == "*":
                result=float(b) * float(a)
            elif item == "/":
                if a=="0":
                    return "Error"
                else:
                    result=float(b) / float(a)
            elif item == "%":
                if a=="0":
                    return "Error"
                else:
                    result=int(b) % int(a)

            st.append(str(result))
        else:
            st.append(item)
    #print(st[0])
    return st[0]

