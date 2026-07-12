class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # both arrays are sorted in non decreasing so this is just the final merge step of merge sort
        # Left pointer tracks nums1 and goes for the len(m)
        # Right pointer tracks nums2 and goes for the len(n)'
        # insert pointer that tracks the location of insertion within nums1
        # If left value is <= Right point place value in insert pointers location
        # No temp values needed for copy
        # start from the right since its in decreasing so you dont overwrite the larger value

        left_ptr = m-1 #starts at 0
        right_ptr = n-1
        insert_ptr = m + n - 1
        
        while right_ptr >= 0: 
            # if left ptr is less than 0, we need to take nums2
            if left_ptr >= 0:
                left_tmp = nums1[left_ptr]
                right_tmp = nums2[right_ptr]

                if left_tmp >= right_tmp:
                    nums1[insert_ptr] = left_tmp
                    left_ptr -= 1
                else:
                    nums1[insert_ptr] = right_tmp
                    right_ptr -= 1

            else:
                right_tmp = nums2[right_ptr]
                nums1[insert_ptr] = right_tmp
                right_ptr -= 1
                
            
            insert_ptr -= 1


