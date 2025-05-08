from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        arr = list(range(1, days + 1))
        meeting_days= set()
        for meeting in meetings:
            for i in range(meeting[0], meeting[1] + 1):
                meeting_days.append(i)
        arr = [day for day in arr if day not in meeting_days]
        return arr