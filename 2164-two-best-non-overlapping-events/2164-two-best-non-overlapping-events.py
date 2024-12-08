class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        event = []       

        for start, end, value in events:
            event += [(start, 1, value)]
            event += [(end + 1, -1, value)]
        event = sorted(event)

        res = 0            
        max_value = 0       

        for time, load, value in event:
            if load == 1:
                res = max(res, max_value + value)
            else:
                max_value = max(max_value, value)

        return res