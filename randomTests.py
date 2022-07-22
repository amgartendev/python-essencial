class Account:
    counter = 0

    def __init__(self, owner, balance, limit):
        self.__counter = Account.counter
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit
        Account.counter += 1

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, new_owner):
        self.__owner = new_owner

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        self.__balance = new_balance

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, new_limit):
        self.__limit = new_limit

    def show_infos(self):
        return f'{self.__owner} has the balance of {self.__balance} and a limit of {self.__limit}'

    def transfer(self, amount, recipient):
        self.__balance -= amount
        recipient.__balance += amount


acc1 = Account('João', 2000, 3000)
acc2 = Account('Roberto', 5000, 7000)

print(acc1.owner)
print(acc1.balance)
print(acc1.limit)

print(acc1.show_infos())

acc1.owner = 'Carlos'
acc1.balance = 1000
acc1.limit = 2000

print(acc1.owner)
print(acc1.balance)
print(acc1.limit)

print(acc1.show_infos())

print('=' * 15)

print(acc1.__dict__)
print(acc2.__dict__)

acc1.transfer(500, acc2)
print('-' * 15)

print(acc1.__dict__)
print(acc2.__dict__)
