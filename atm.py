class Atm:
    
    def __init__(self):
        self.pin=''
        self.balance=0
        self.menu()
        
    def menu(self):
        user_input = input("""
        select the menu
        1. press 1 to create pin
        2. press 2 to change pin
        3. press 3 to check balance
        4. press 4 to withdrawl
        5. exit
        """)
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdrawl()
        else:
            exit()
    
    def create_pin(self):
        user_pin=input("enter new pin")
        self.balance=input('enter balance')
        self.pin=user_pin
        print("pin created sccessfully")
        self.menu()
        
    def change_pin(self):
        old_pin=input("enter you pin")
        if(old_pin==self.pin):
            new_pin=input('enter new pin')
            self.pin=new_pin
            print('pin changed successfully')
        else:
            print("enterd pin is wrong")
        
        self.menu()
    
    def check_balance(self):
        user_pin=input("enter your pin")
        if(user_pin==self.pin):
            print('balance', self.balance)
        else:
            print('pin is wrong')
        self.menu()
        
    def withdrawl(self):
        user_pin=input("enter pin ")
        if(user_pin==self.pin):
            amount=int(input("enter amount to withdrawl"))
            if(amount<self.balance):
                self.balance=self.balance - amount
                print('amount left : ',self.balance)
            else:
                print("chal gareeb")
        else:
            print("pin is wrong")
        self.menu()

obj = Atm()
        
