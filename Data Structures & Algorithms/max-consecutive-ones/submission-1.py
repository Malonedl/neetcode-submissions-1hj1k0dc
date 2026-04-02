class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consec = 0
        max_consec = 0
        i = 0

        for num in nums:
            if num == 1:
                consec += 1
                if consec > max_consec:
                    max_consec = consec
            else:
                consec = 0
        
        return max_consec 
                