def Card():
    Card_no = input("Enter your Card no : ")
    length = len(Card_no)
    cout = 0
    if(length<10 or length>10 or length==''):
        cout+=1
        print("The Credit or Debit card number must be 10 digits ")
        print("Re-enter it : ")
        if(cout>0):
            Card()
    else:
        date = input("Enter expiry Month : ")
        dlen = len(date)
        year = input("Enter expiry Year : ")
        ylen = len(year)
        if(dlen<2 or dlen>2 or dlen==""):
            print("Please Enter Correct month !")
        elif(ylen<2 or ylen>2 or ylen==""):
            print("Please Enter Correct Year !")
        else:
            return True


if __name__ == '__main__':
     Card()

