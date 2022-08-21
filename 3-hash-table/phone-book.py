# create a phone book with hash table structure


class HashTable:
    def __init__(self, hash_table_size=4096):
        self.phone_book = [None] * hash_table_size

    def get_index(self, name):
        result = 0
        for i in name:
            result += ord(i)
        return result % len(self.phone_book)

    def get_valid_index(self, name):
        idx = self.get_index(name)
        while True:
            if self.phone_book[idx] is None:
                return idx
            if self.phone_book[idx][0] == name:
                return idx
            idx += 1
            if idx == len(self.phone_book):
                idx = 0

    def insert(self, name, number):
        idx = self.get_valid_index(name)
        self.phone_book[idx] = (name, number)
        print("Created! {}'s number are stored in {}".format(name, idx))

    def find(self, name):
        idx = self.get_valid_index(name)
        print("{}'s phone number is {}".format(name, self.phone_book[idx][1]))

    def update(self, name, new_number):
        idx = self.get_valid_index(name)
        lst = list(self.phone_book[idx])
        lst[1] = new_number
        self.phone_book[idx] = tuple(lst)
        print("Updated {}'s phone number to {}".format(name, new_number))

    def list_name(self):
        print([x[0] for x in self.phone_book if x is not None])


my_phone_directory = HashTable(512)
print(len(my_phone_directory.phone_book))
my_phone_directory.insert("selina", "0999999999")
my_phone_directory.insert("jack", "0799999999")
my_phone_directory.insert("david", "0699999999")
my_phone_directory.insert("jason", "0899999999")
my_phone_directory.insert("konan", "0299999999")
my_phone_directory.insert("vidad", "0669999999")
my_phone_directory.find("david")
my_phone_directory.update("david", "0367892541")
my_phone_directory.list_name()

print(hash("david") % 512)
