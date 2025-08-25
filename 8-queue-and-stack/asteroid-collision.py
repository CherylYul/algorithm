"""
Leet code 735: Asteroid Collision
Techniques: Stack
Complexity: O(n) where n is the length of asteroids
Space Complexity: O(n) for the stack used to store asteroids"""


class Solution(object):
    def asteroidCollision(self, asteroids):
        s = []
        for num in asteroids:
            destroy = False
            while s and s[-1] > 0 and num < 0:
                if abs(num) == s[-1]:
                    destroy = True
                    s.pop()
                    break
                elif abs(num) < s[-1]:
                    destroy = True
                    break
                else:
                    s.pop()
            if not destroy:
                s.append(num)
        return s
