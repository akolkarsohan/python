numbers = [1, 2, 3]

def file_ops():
    myfile = open("numbers.txt", "w")
    for item in numbers:
        myfile.write(str(item) + "\n")

    myfile = open("numbers.txt", "r")
    contents = myfile.read()
    myfile.close()
    print (contents)

file_ops()
