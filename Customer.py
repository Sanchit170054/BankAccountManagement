from Project3_Bank_Account_Manager.checking import checking


class Customer:
    name = input("Please enter your name: ")
    print("Welcome {},".format(name))

    while True:

        print("Press 1 to check current account status, 2 to check savings account, 3 to Business account, or 0 to quit")
        userInput = int(input("enter your input "))

        if userInput == 1 or userInput == 2 or userInput == 3:
            accountNumber = input("Please enter your Account Number ")

            print("Account Balance updated successfully..!")
            x = checking(accountNumber, 0)

            while True:
                print("Press 1 to add  more money, 2 to withdraw money or 0 to quit ")
                inputValue = int(input("enter your input "))

                if inputValue == 1:
                    depositMoney = int(input("Please enter your money "))
                    x.acceptMoney(depositMoney)
                elif inputValue == 2:
                    withdrawMoney = int(input("Please enter your money "))
                    x.witdrawAmount(withdrawMoney)
                elif inputValue == 0:
                    print("Thanks for visiting here..!")
                    break
                else:
                    print("Please provide valid input..!")

        elif userInput == 0:
            print("Thanks for the visiting here.....")
            break
        else:
            print("Please enter the valid input..!")
