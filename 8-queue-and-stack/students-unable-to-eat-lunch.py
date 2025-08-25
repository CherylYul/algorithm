"""
Leet code 1700: Number of Students Unable to Eat Lunch
Techniques: Queue, Counting
Complexity: O(n) where n is the number of students
Space Complexity: O(n) for queue simulation, O(1) for counting approach
"""

from collections import deque


class Solution(object):
    # Counting
    def countStudents(self, students, sandwiches):
        count = [0] * 2
        for stu in students:
            count[stu] += 1
        i = 0
        while i < len(sandwiches) and count[sandwiches[i]] > 0:
            count[sandwiches[i]] -= 1
            i += 1
        return count[0] + count[1]

    # Queue Simulation
    def countStudents(self, students, sandwiches):
        students = deque(students)
        i = 0
        while students:
            pop_nums = len(students)
            while pop_nums and students[0] != sandwiches[i]:
                students.append(students.popleft())
                pop_nums -= 1
            if pop_nums == 0:
                return len(students)
            students.popleft()
            i += 1
        return 0
