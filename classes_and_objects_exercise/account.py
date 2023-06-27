class Account:

    def __init__(self, user_id: int, name: str, balance: int = 0):
        self.id = user_id
        self.name = name
        self.balance = balance

    def credit(self, amount: int) -> int:
        self.balance += amount

        return self.balance

    def debit(self, amount: int) -> int or str:
        if amount <= self.balance:
            self.balance -= amount

            return self.balance

        return "Amount exceeded balance"

    def info(self) -> str:

        return f"User {self.name} with account {self.id} has {self.balance} balance"


# account = Account(5411256, "Peter")
# print(account.debit(500))
# print(account.credit(1000))
# print(account.debit(500))
# print(account.info())