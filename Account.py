class Account:
    def __init__(self, accNumber, depositMoney):
        self.accNumber = accNumber
        self.deposit = int(depositMoney)

    def acceptMoney(self, amount):
        self.deposit = self.deposit + amount
        print("Updated Balance: {}".format(self.deposit))

    def witdrawAmount(self, withdraw_Amount):
        if self.deposit >= withdraw_Amount:
            self.deposit = self.deposit - withdraw_Amount
            print("Remaining Balance: {}".format(self.deposit))

        else:
            print("Your balance is low..!!!")

