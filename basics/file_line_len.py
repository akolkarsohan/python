def calculate_len(filename):
    myfile = open(filename)
    contents = myfile.read()
    myfile.close()
    lines = contents.splitlines()
    print (lines)
    for item in lines:
        print (len(item))

user_input=raw_input("Enter filename: ")
calculate_len(user_input)
