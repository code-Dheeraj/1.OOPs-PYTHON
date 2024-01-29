class atm:
    
    def __init__(self):
        self.pin=''
        self.balance=0
        self.menu()
    
    def menu(self):
        user_input=input("""
        enter the number
        1. create pin
        2. change pin
        3. check balance
        4. withdraw
        5. exit
        """)
        
        if user_input == '1':
            self.createPin()
        elif user_input == '2':
            self.changePin()
        elif user_input =='3':
            self.check_balance()
        elif user_input =='4':
            self.withdraw()
        else:
            exit()
        
    def createPin(self):
        newPin=int(input("enter you pin "))
        self.pin=newPin
        initialBalance=int(input("enter your initial balance "))
        self.balance=initialBalance
        print("Pin created successfully")
        self.menu()
        
    def changePin(self):
        user_pin=int(input("enter your atm pin "))
        if(user_pin==self.pin):
            user_pin=int(input("enter your new pin "))
            self.pin=user_pin
            print("your pin has changed successfully")
        else:
            print("your pin is wrong...")
        self.menu()
    
    def check_balance(self):
        user_pin=int(input("enter you atm pin "))
        if(user_pin==self.pin):
            print("your balance ",self.balance)
        else:
            print("your pin is wrong...")
        self.menu()
    
    def withdraw(self):
        user_pin=int(input("enter you atm pin "))
        if(user_pin==self.pin):
            withdraw_amount=int(input("enter amount to withdraw "))
            if(withdraw_amount<self.balance):
                left_balance=self.balance-withdraw_amount
                print("your current balance is :",left_balance)
            else:
                print("insufficient funds ")
        else:
            print("your pin is wrong...")
        self.menu()

obj = atm()
