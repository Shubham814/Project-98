def swapData():
    print("Enter 2 files path to swap their data.")

    # getting file path from user
    file1 = str(input("Enter 1st file path: "))
    file2 = str(input("Enter 2nd file path: "))

    # reading data from files and storing them in variables
    with open(file1,'r') as a:
        data_1 = a.read()
    with open(file2,'r') as b:
        data_2 = b.read()

    # swapping data in files
    with open(file1,'w') as a:
        a.write(data_2)
    with open(file2,'w') as a:
        a.write(data_1)

swapData()

