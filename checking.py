from Project3_Bank_Account_Manager.Account import Account

actualMoney = 0


class checking(Account):

    def __init__(self, accountNumber, openingMoney):
        super().__init__(accountNumber, openingMoney)

        print("Account Number :# {} \nAccount Balance is: Rs {} ".format(self.accNumber, self.deposit))


class savings(Account):

    def __init__(self, accountNumber, openingMoney):
        super().__init__(accountNumber, openingMoney)

        print("Saving Account Number :# {} \nAccount Balance is: {}".format(self.accNumber, self.deposit))


class Business(Account):
    def __init__(self, accountNumber, openingMoney):
        super().__init__(accountNumber, openingMoney)

        print("Business Account Number :# {} \nAccount Balance is: {}".format(self.accNumber, self.deposit))
