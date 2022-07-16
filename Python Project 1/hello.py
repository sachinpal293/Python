def Data_read():
    x = open("student.dat")
    name = input("Enter user name : ")
    count = 0
    for line in x:
        if line.startswith(name.lower()):
            data = line
            print(data,end="")
            count += 1

    if (count == 0):
        print("Sorry! User name is not founded")
if __name__ == '__main__':
    Data_read()