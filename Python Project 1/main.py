import hello
import card
course_list = {1: {'Name':'JAVA','Cost':20,'Total_Lenght':'10 hours'},
                   2:{'Name':'RUBY', 'Cost':30,'Total_Lenght':'15 hours'},
                   3:{'Name':'DATABASE','Cost':120,'Total_Lenght':'10 hours'},
                   4:{'Name':'JAVA ADVANCE' ,'Cost':60,'Total_Lenght':'20 hours'},
                   }




def Listofcourse():
    print("The Available courses are: ")
    print("1 - Java\n2 - Ruby\n3 - Database\n4 - Java advance")

    cours_selection = int(input("""Please select the course code you want to enrol or a negative number to exit:\n"""))
    cost = course_list[cours_selection]['Cost']
    Cname = course_list[cours_selection]['Name']
    duration = course_list[cours_selection]['Total_Lenght']
    if(cours_selection>0):
        print("Course Details: \n")
        print(f"Name : {Cname}")
        print(f"Cost : {cost}$")
        print(f"Duration : {duration}")

        choice = input("\nDo you want to enrol in this course (Y/N)? ")

        if(choice=='Y' or choice == 'y'):
            Enroll_course(cours_selection,Cname, cost, duration)
        else:
            print("Thank you , for Visit !")
            exit()
    else:
        exit()

def search_course():
    search_input= input("Please enter the course name you want to search or a negative number to exit: ")
    count = 0
    for i in course_list:
        if(course_list[i]['Name']==search_input.upper()):
            print("Thank You!\n")
            print("One course has been found:")
            print(f"Course ID : {i}\nName: {course_list[i]['Name']}\nCost: {course_list[i]['Cost']}\nDuration : {course_list[i]['Total_Lenght']}")
            count+=1
            break

    if(count==0):
        print("This Course is not found")

# def Transaction():
#     value = card.Card()
#     if(value==True):
#         print("The Transcation is Successfull ")
#     else:
#         print("The Transcation is unsuccessfull")


def Enroll_course(code, Cname, amount, duration):
    print("Please enter your name and your credit or debit card details:")
    Name = input("Name: ")
    value = card.Card()
    if(value==True):
        Detail = [Name, code, Cname, amount, duration]
        with open("student.dat", 'a', encoding='utf-8') as f:
            f.write(f"{Name.lower()} : {Detail}")
            f.write("\n")
        print("Thank You!")
        print('Your course have been enrolled !')
        choice = input("\nDo you want to enrol in another course (Y/N)? ")
        if (choice == 'Y' or choice == 'y'):
            Listofcourse()
        else:
            mainwindow()
    else:
        print("Your transaction is unsuccesfull !\n\n")
        mainwindow()
    print(value)



def MyLearn():
    hello.Data_read()

def mainwindow():
    print("\n")
    print("====================================================")
    print("     Welcome to TAFE Online Courses System")
    print("====================================================")
    print("<1> List the available courses")
    print("<2> Search for a course")
    print("<3> Enrol in a course")
    print("<4> List My Course")
    print("<5> Quit")
    getdata()

def getdata():
    Choice = int(input("Please select an option from the above : "))
    if(Choice==1):
        Listofcourse()
    elif(Choice==2):
        search_course()
    elif(Choice==3):
        Listofcourse()
    elif(Choice==4):
        MyLearn()
    else:
        exit("Enter for Exit.")

if __name__ == '__main__':
    try:
        while (True):
            mainwindow()
    except Exception as e:
        print(e)




