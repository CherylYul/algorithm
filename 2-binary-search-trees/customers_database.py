# Developing a fast in-memory data structure to manage customers e-wallet
# operations needed include insert new customers information,
# find customers information,
# update their balance if any changes,
# list all customers information
from helpful_function import calculate_height, calculate_size, display_tree


class Ewallet:
    def __init__(self, account_number, username, balance=0):
        self.account_number = account_number
        self.username = username
        self.balance = balance

    def transfer_to(self, amount, Others):
        self.balance -= amount
        Others.balance += amount
        return "You transfer {} to {}, please confirm!".format(amount, Others.username)

    def deposits(self, amount):
        initial_amount = self.balance
        self.balance += amount
        return "Your balance increase from {} to {}".format(
            initial_amount, self.balance
        )

    def withdraw(self, amount):
        initial_amount = self.balance
        self.balance -= amount
        return "Your balance decrease from {} to {}".format(
            initial_amount, self.balance
        )

    def __repr__(self):
        return "Your account information: account numbers {}, username {}, balance {}".format(
            self.account_number, self.username, self.balance
        )

    def __str__(self):
        return self.__repr__()


cheryl = Ewallet("27495572", "ycheryl", 3819)
howard = Ewallet("78313649", "howardtang", 8972)
andrew = Ewallet("10387362", "andrewnguyen", 4267)
dilys = Ewallet("10357362", "dilysdong", 2267)
william = Ewallet("57830930", "williamle", 11909)
andy = Ewallet("97830930", "andyoptix", 21909)

print(cheryl)
print(cheryl.deposits(200))
print(cheryl.withdraw(50))
print(cheryl.transfer_to(9, william))
print(william)


class DatabaseTree:
    def __init__(self, username, balance=0):
        self.username = username
        self.left = None
        self.right = None
        self.balance = balance
        self.parent = None


def insert(database, ewallet):
    if database is None:
        database = DatabaseTree(ewallet.username, ewallet.balance)
    elif ewallet.username < database.username:
        database.left = insert(database.left, ewallet)
        database.left.parent = database
    elif ewallet.username > database.username:
        database.right = insert(database.right, ewallet)
        database.right.parent = database
    return database


def find(database, username):
    if database is None:
        return None
    if database.username == username:
        return database
    if username < database.username:
        return find(database.left, username)
    if username > database.username:
        return find(database.right, username)


def update(database, username, balance):
    target = find(database, username)
    if target is not None:
        target.balance = balance


def list_all(database):
    if database is None:
        return []
    return (
        list_all(database.left)
        + [(database.username, database.balance)]
        + list_all(database.right)
    )


def data_to_balanced_tree(data, lo=0, hi=None, parent=None):
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None
    mid = (lo + hi) // 2
    username, balance = data[mid]
    root = DatabaseTree(username, balance)
    root.parent = parent
    root.left = data_to_balanced_tree(data, lo, mid - 1, parent)
    root.right = data_to_balanced_tree(data, mid + 1, hi, parent)
    return root


class UserDatabase:
    def __init__(self):
        self.root = None

    def __setitem__(self, ewallet):
        item = find(self.root, ewallet.username)
        if not item:
            self.root = insert(self.root, ewallet)
            self.root = data_to_balanced_tree(list_all(self.root))
        else:
            update(self.root, ewallet.username, ewallet.balance)

    def __getitem__(self, ewallet):
        item = find(self.root, ewallet.username)
        return item.value if item else None

    def __iter__(self):
        return (print(x) for x in list_all(self.root))

    def __len__(self):
        return calculate_size(self.root)

    def __display__(self):
        return display_tree(self.root)

    def __repr__(self):
        return ("customer information: {}".format(x) for x in list_all(self.root))


customer_data = UserDatabase()
customer_data.__setitem__(cheryl)
customer_data.__setitem__(howard)
customer_data.__setitem__(dilys)
customer_data.__setitem__(william)
customer_data.__setitem__(andrew)
