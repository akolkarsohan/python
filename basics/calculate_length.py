def calculate_len(input_str):
    if type(input_str) == int:
        print ("Intergers don't have lengths")
    elif type(input_str) == float:
        print("Floats don't have lengths")
    else:
        return len(input_str)

input_str=input("Enter input string: ")

print (calculate_len(input_str))
   
