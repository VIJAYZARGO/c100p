class Atm:
    def __init__(self,card_number,pin,balance_before_withdrawal,cash_to_withdraw,balance_after_withdrawal):
        self.card_number = card_number
        self.pin = pin
        self.balance_before_withdrawal = balance_before_withdrawal
        self.cash_to_withdraw = cash_to_withdraw
        self.balance_after_withdrawal = balance_after_withdrawal
        
    def insert_the_card(self):
            print("card inserted")
        
    def enter_the_pin(self):
            print("entered the pin")
        
    def Cash_To_Withdraw(self,ctw):
            print(ctw,"has been withdrawn")
        
    def Balance_After_Withdrawal(self,baw):
            print(baw,"is your available balance")

account1 = Atm("XXXX XXXX xxxx xxxx", 2908, 1050000, 30000, 1020000)

account1.insert_the_card()
account1.enter_the_pin()
account1.Cash_To_Withdraw(30000)
account1.Balance_After_Withdrawal(1020000)

