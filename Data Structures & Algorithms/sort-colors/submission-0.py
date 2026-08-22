class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n -> counts pointer
        # i -> array pointer
        # interate through to count the colors. Then play them back into the sorted array
        # overwriting the previous values. 
        counts = [0,0,0]

        for color in nums:
            counts[color] += 1

        # increment over the counts position
        i = 0
        colors = len(counts)
        for color in range(colors):
            for _ in range(counts[color]):
                nums[i] = color
                i += 1





            


        