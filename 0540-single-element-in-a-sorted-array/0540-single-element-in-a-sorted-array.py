class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Initialize the left and right pointers
        l, r = 0, len(nums) - 1

        while l != r:
            # Set the value of mid
            mid = l + (r - l) // 2

            # If mid is odd, decrement it to make it even
            if mid % 2 == 1:
                mid -= 1

            # If the elements at mid and mid + 1 are the same,
            # then the single element must appear after the midpoint
            if nums[mid] == nums[mid + 1]:
                l = mid + 2
            # Otherwise, we must search for the single element
            # before the midpoint
            else:
                r = mid

        return nums[l]