from random import choice

"""
Expected constant time: O(1) for delete, lookup and insert
Space need: O(n log(M))
- n items with log(M) bits per item
- log(M) bits to store the hash function
- n buckets
"""


class HashTable:
    # function h maps universe U to range(n)
    # store in n buckets, each has linked list
    def __init__(self, h, n):
        self.h = h
        self.buckets = [[] for _ in range(n)]

    def insert(self, x):
        self.buckets[self.h(x)].append(x)

    def delete(self, x):
        bucket = self.buckets[self.h(x)]
        for i in range(len(bucket)):
            if bucket[i] == x:
                return bucket.pop(i)
        return None

    def find(self, x):
        bucket = self.buckets[self.h(x)]
        for i in range(len(bucket)):
            if bucket[i] == x:
                return bucket[i]
        return None

    def __repr__(self):
        return "Hash table {}".format(self.buckets)

    def __str__(self):
        return self.__repr__()


"""
Some of hash function:
1. last digit and first digit: return the first and last number of the input
2. generate a uniformly random hash function from range(m) to range(n)
3. generate universal hash function: apply r = (a * x + b) % p
"""


def last_digit(x, n=10):
    return x % n


def first_digit(x, n=10):
    if x == 0:
        return 0
    while x > 0:
        last = x % n
        x = (x / n).__trunc__()
    return last


# error because cannot track position:
# def generate_uniformly_random(x, n=10):
#     return choice(range(n))
def generate_uniformly_random(m, n=10):
    fn_table = [None for _ in range(m)]
    for x in range(m):
        fn_table[x] = choice(range(n))

    def randomFn(x):
        return fn_table[x]

    return randomFn


def generate_universal_hash_fn(a, b, p, n=10):
    def f(x):
        r = (a * x + b) % p
        return r % n

    return f


def bad_hash_family():
    return choice([first_digit, last_digit])


def good_hash_family(p):
    a = choice(range(1, p))
    b = choice(range(p))
    return generate_universal_hash_fn(a, b, p)


def best_hash_family(m, n):
    return generate_uniformly_random(m, n)


# compare collision probabilities
def collision_probabilities(hash_family_fn, m, trials=100):
    data = []
    for x in range(m):
        for y in range(x + 1, m):
            countxy = 0
            for t in range(trials):
                h = hash_family_fn()
                if h(x) == h(y):
                    countxy += 1
            data.append(countxy / trials)
    return data


"""
Using last digit & first digit fn we can find and delete the value easily, but
using generate uniform random, we cannot arrange larger size, say we need hash
all 128^40 hashtags m = 128^40, that's alot! It better to use universal hash fn
"""

HT = HashTable(last_digit, 10)
HT.insert(2631)
HT.insert(263822435)
HT.insert(19)
print(HT.find(2631))
print(HT.find(2630))
print(HT.delete(782))
print(HT.delete(19))
print(HT.__str__())


# range m is 1000 so hash function cannot larger than that
random_fn = generate_uniformly_random(1000, 10)
HT = HashTable(random_fn, 10)
HT.insert(123)
HT.insert(76)
print(HT.find(123))
print(HT.find(263))
print(HT.__str__())
