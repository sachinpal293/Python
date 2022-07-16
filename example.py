import card
def Enroll_course(code, Cname, amount, duration):
    print("Please enter your name and your credit or debit card details:")
    Name = input("Name: ")
    value = card.Card()
    if(value==True):
        Detail = [Name, code, Cname, amount, duration]
        with open("student.txt", 'a', encoding='utf-8') as f:
            f.write(f"{Name.lower()} : {Detail}")
            f.write("\n")
            print("Thank You!")
            print('Your course have been enrolled !')
            choice = input("\nDo you want to enrol in another course (Y/N)? ")

    else:
        print("Your transaction is unsuccesfull !\n\n")
