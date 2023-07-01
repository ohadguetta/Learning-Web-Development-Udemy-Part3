#Create a banking app, with withdraw and deposit, write the transaction to a file



class Account:
    balance = 100.0
    name = 'Ohad'

    def log_transaction(self,transaction,amount):
        messsage = str(transaction+' was executed with '+str(amount)+' amount. '+'total balance is: '+str(self.balance))
        try:
            with open('transactions.txt','a') as file:
                file.write(messsage)
                file.write('\n')
        except Exception:
            with open('transactions.txt','w') as file:
                file.write(messsage)
                file.write('\n')

            
    def withdraw(self,amount):
        if amount > 0:
            if self.balance < amount:
                temp_bal = self.balance
                self.balance = 0
                self.log_transaction('Withdraw',amount)
                return temp_bal
            else:            
                self.balance = self.balance - amount;
                self.log_transaction('Withdraw',amount)
                return self.balance
        else:
            return ValueError
    def deposit(self,amount):
        if amount > 0:
            self.balance = self.balance + amount
            self.log_transaction('Deposit',amount)
            return self.balance
        else:
            return ValueError
    
    @property
    def get_balance(self):
        return self.balance
    
    def set_balance(self,new_balance):
        self.balance = new_balance
        return self.balance
    
    @property
    def get_name(self):
        return self.name
    
    def set_name(self,new_name):
        self.name = new_name
        return self.name


user = Account()
while True:
    operation = input('What is the desired operation? (D)eposit,(W)ithdraw,(B)alance to see balance, or (E)xit.')
    if operation.lower() == 'd':
        amount = int(input('How much to deposit: '))
        user.deposit(amount)
    elif operation.lower() == 'w':
        amount = int(input('How much to withdraw: '))
        user.withdraw(amount)
    elif operation.lower() == 'b':
        print(user.get_balance)
    elif operation.lower() == 'e':
        print('Bye!')
        break
