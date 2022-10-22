while(True):
    a = int(input(10*"=="+"\nInput number 'a'\n"))
    b = int(input("Input number 'b'\n"))
    symbol = str(input("Choose operation(+,-,*,/): "))
    together = (str(a)+symbol+str(b)+" = ")
    if(symbol == "+"):
        print(together+str(a+b))
    elif(symbol == "-"):
        print(together+str(a-b))
    elif(symbol == "*"):
        print(together+str(a*b))
    elif(symbol == "/"):
        if(b != 0):
            print(together+str(a/b))
        else:
            print("ERROR - Cannot divide by zero")
    else:
        print("ERROR - Wrong symbol")