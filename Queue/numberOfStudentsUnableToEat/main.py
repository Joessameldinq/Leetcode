from collections import deque
class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        q1 = deque(students)
        q2 = deque()
        n = len(students)
        for i in range(n):
            if students[i] == sandwiches[i]:
                q1.popleft()
                sandwiches.pop()
            else:
                q2.append(q1.popleft()) 
        