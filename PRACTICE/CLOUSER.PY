# Create a closure that remembers a username.
# def username(name):

#     def remember():
#         print(name)
#     return remember
# user1 = username("Vedantr")
# user2 = username("Rahul")

# user1()
# user2()


# Create a bank balance closure.Functions:deposit,withdraw,check balance
def bank_balance(amount):
    def deposit():
        print(amount)
        return deposit
    def withdraw():
        print(amount)
        return withdraw
    def check_balance():
        print(amount)
        return check_balance
user = bank_balance(1000)
user.deposit()
user.withdraw()
user.check_balance()