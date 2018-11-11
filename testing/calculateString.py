def calcString(f):
    if type(f) == str:
        return len(f)

    elif type(f) == int:
        return "Sorry integers don't have legth."

    elif type(f) == float:
        return "Sorry floats don't have legth. "

    else:
        return "the input don't have length"



#f = input("please input the string to calculate: ")
print(calcString(True))
