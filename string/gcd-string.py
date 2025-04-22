"""
The task requires finding the largest string x that divides both
input strings str1 and str2. Here, "divides" means that the original string
can be formed by repeatedly concatenating x.
- Brute-Force Substring Check: inefficient
- Euclidean Algorithm: a > b => gcd(a, b) = gcd(b, a % b), repeat until b = 0
Ex: 65 vs 25 => 25 vs 15 => 15 vs 10 => 10 vs 5 => 5 vs 0
"""


class Solution(object):
    def gcdOfStrings2(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""

        a, b = len(str1), len(str2)
        while b > 0:
            a, b = b, a % b

        return str1[:a]

    def gcdOfStrings1(self, str1, str2):
        if len(str1) >= len(str2):
            long_str_length, long_str = len(str1), str1
            short_str_length, short_str = len(str2), str2
        else:
            long_str_length, long_str = len(str2), str2
            short_str_length, short_str = len(str1), str1

        l = short_str_length // 2
        list_of_divisor = [
            {
                "string": short_str[0],
                "common_divisor": 1,
                "short_coef": short_str_length,
                "long_coef": long_str_length,
            }
        ]

        for i in range(2, l + 1):
            if short_str_length % i == 0 and long_str_length % i == 0:
                list_of_divisor.append(
                    {
                        "string": short_str[:i],
                        "common_divisor": i,
                        "short_coef": short_str_length / i,
                        "long_coef": long_str_length / i,
                    }
                )
        print(list_of_divisor)
        if long_str_length % short_str_length == 0:
            if short_str * (long_str_length / short_str_length) == long_str:
                return short_str

        for obj in list_of_divisor[::-1]:
            if (
                obj["string"] * obj["short_coef"] == short_str
                and obj["string"] * obj["long_coef"] == long_str
            ):
                return obj["string"]

        return ""
