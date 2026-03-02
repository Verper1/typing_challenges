import decimal
import uuid

class User:
    def __init__(self, balance="265.2"):
        self.__balance = balance
        self.id = uuid.uuid4()

    def get_user_balance(self, user_id: uuid.uuid4) -> decimal.Decimal:
        if user_id == self.id:
            return decimal.Decimal(self.__balance)

    def get_user_id(self):
        return self.id


if __name__ == "__main__":
    usr1 = User("1000")
    usr2 = User()

    usr1_id = usr1.get_user_id()
    usr2_id = usr2.get_user_id()

    assert usr1.get_user_balance(user_id=usr1_id) != decimal.Decimal("265.2")
    assert usr2.get_user_balance(user_id=usr2.id) == decimal.Decimal("265.2")
