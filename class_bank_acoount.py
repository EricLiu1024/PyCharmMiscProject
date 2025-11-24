class Account():
    def __init__(self,balance,account_holder):
        self.balance = balance
        self.account_holder = account_holder
class SavingsAccount(Account):
    def __init__(self,balance,account_holder,interest_rate):
        self.interest_rate = interest_rate
        Account.__init__(self,balance,account_holder)
    def calculate_interest(self):
        return self.interest_rate * self.balance
def main():
    a = SavingsAccount(5000,'David Lee',0.025)
    print(a.calculate_interest())
main()

#Implement an instance method calculate_interest() in SavingsAccount that calculates and returns the interest based on the balance and interest_rate.
#Create an instance of SavingsAccount for "David Lee" with an initial balance of 5000 and an interest_rate of 0.025 (representing 2.5%).
#Call the calculate_interest() method on this instance and print the returned interest amount to verify the calculation.