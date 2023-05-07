class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:

        @cache
        def dp(l, r, count = 0):
            if l > r: return 0
            #Initial count for the letter at boxes[l]
            count += 1
            ptr = l + 1
            while ptr <= r and boxes[l] == boxes[ptr]:
                ptr += 1
                count += 1
            points = (count ** 2) + dp(ptr, r)
            for i in range(ptr + 1, r + 1):
                if boxes[l] == boxes[i]:
                    points = max(points, dp(i, r, count) + dp(ptr, i - 1))
            return points

        return dp(0, len(boxes) - 1)
            
