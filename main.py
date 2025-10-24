while True:

    one= input("Enter the first number: ")
    two= input("Enter the second number: ")
    op= input("Enter the operation between them: ").lower()
    try:
            one= float(one)
            two= float(two)

            if op =="sum" or op =="+" or op=="add" or op=="addition" or op=="plus":
                print("The result is: ", one + two)
            elif op =="difference" or op =="-" or op=="subtract" or op=="subtraction" or op=="minus":
                print("The result is: ", one - two)
            elif op =="product" or op =="x" or op=="*" or op=="multiply" or op=="multiplication" or op=="into" or op=="times":
                print("The result is: ", one * two)
            elif op =="quotient" or op =="//" :
                print("The result is: ", one // two)
            elif op =="remainder" or op=="%":
                print("The result is: ", one % two)
            elif op =="/" or op=="divide" or op=="division" or op=="by":
                print("The result is: ", one / two)
            elif op=="avg" or op=="average":
                print("The result is: ", ((one + two)/2))
            elif op=="power" or op=="exponent" or op=="**" or op=="exponentiation":
                print("The result is: ", one ** two)
            elif op=="round" or op=="round off" or op=="nearest integer":
                print("The result is: ", round(one), "and ", round(two) )
            else :
                print("Invalid operation")
    except ValueError:
        print("Please enter proper numbers.")
    except ZeroDivisionError:
        print("Division by zero is invalid.")
    ptc = input("Do you wish to continue? [Y for YES; else for NO]: ").lower()
    if ptc == "y":
        continue
    else:
        print("Exiting calculator...")
        break
