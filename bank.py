class Bank:
    def __init__(self):
        self.accountStatus = 5000
    
    def withdraw(self, amount):
        self.accountStatus -= amount
    
    def add(self, amount):
        self.accountStatus += amount

    def display_account_status(self):
        print(self.accountStatus)

users = [Bank() for _ in range(5)]

# print(users)

while True:
    activity = input("Co chcesz zrobić? (withdraw, add, show lub exit):")

    if activity.lower() == "withdraw":
        whichUser = int(input("Którym użytkownikiem jesteś (0 - 4) lub exit: "))
        amount = int(input("Jaka kwota?: "))
        users[whichUser].withdraw(amount)

    elif activity.lower() == "add":
        whichUser = int(input("Którym użytkownikiem jesteś (0 - 4) lub exit: "))
        amount = int(input("Jaka kwota?: "))
        users[whichUser].add(amount)

    elif activity.lower() == "show":
        whichUser = int(input("Którym użytkownikiem jesteś (0 - 4) lub exit: "))
        print(users[whichUser].display_account_status())

    else:
        break

