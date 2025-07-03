class Solution(object):
    def binaryToNums(s):
        reverse_s = s[::-1]
        nums = 0
        for i in range(len(s)):
            nums += pow(2, i) if reverse_s[i] == "1" else 0
        return nums

    def numsToBinary(num):
        s = ""
        print(num)
        while num != 0:
            s += "0" if num % 2 == 0 else "1"
            num = num // 2
        return s[::-1]

    def addBinary(self, a, b):
        pass
