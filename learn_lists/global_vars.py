# bal = 0

# def main():
#     print('Balance:', bal)
#     deposit(100)
#     withdraw(50)

#     print('Updated Balance:', bal)

# def deposit(n):
#     global bal
#     bal += n

# def withdraw(n):
#     global bal
#     bal -= n

# if __name__ == '__main__':
#     main()


class Account:
    def __init__(self):
        self._bal = 0

    @property
    def balance(self):
        return self._bal

    def deposit(self, n):
        self._bal += n

    def withdraw(self, n):
        self._bal -= n


def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)


if __name__ == "__main__":
    main()
