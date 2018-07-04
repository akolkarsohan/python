def convertor(C):
    if C < -273.15:
        print ("Such a low temperature of physical matter is not possible, please check your value")
    else:
        return ((C * 9)/5 + 32)

user_input=float(input("Enter Celsius value: "))
print (user_input)

print (convertor(user_input))

