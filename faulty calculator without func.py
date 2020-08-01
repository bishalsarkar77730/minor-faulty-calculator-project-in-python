# project faulty calculator in python minor...
print("enter your operator in operator section +,-,*,/ ")
val1 = int(input("Enter first number = "))
operator=input("enter operator = ")
val2 = int(input("Enter second number = "))
if operator == "+":
    if val1 == 56 and val2 == 9:
        print("77")
    else:
        print("Sum is:",val1 + val2)
elif operator == "-":
    print("Substract is:",val1-val2)
elif operator == "*":
    if val1 == 45 and val2 == 3:
        print("555")
    else:
        print("Multiply is :",val1*val2)
elif operator == "/":
    if val1 ==56 and val2 == 6:
        print("4")
    else:
        print("Divide is:",float(val1/val2))