class Solution:
    def calPoints(self, operations: List[str]) -> int:
        nums = []
        for i in operations:
            if i == 'D':
                nums.append(int(nums[-1]*2))
                
            
            elif i == '+':
                tmp1 = nums[-1]
                tmp1 += nums[-2]
                nums.append(tmp1)

            elif i == 'C':
                nums.pop(-1)
            
            else:
                nums.append(int(i))
        
        return sum(nums)
            

        