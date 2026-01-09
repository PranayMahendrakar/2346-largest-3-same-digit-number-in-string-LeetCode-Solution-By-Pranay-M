class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # Find largest 3-digit substring with same digits
        # Time: O(n), Space: O(1)
        result = ""
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                if num[i:i+3] > result:
                    result = num[i:i+3]
        return result