class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        # Step 1: Sort the array
        nums.sort()

        # Step 2: Define binary search range
        low, high = 1, nums[-1]  # Minimum and maximum possible maxBalls
        result = high

        while low <= high:
            mid = (low + high) // 2

            # Step 3: Feasibility check
            if self.canDistribute(nums, maxOperations, mid):
                result = mid  # Update result with feasible maxBalls
                high = mid - 1  # Try smaller maximum
            else:
                low = mid + 1  # Try larger maximum

        return result

    def canDistribute(self, nums: list[int], maxOperations: int, maxBalls: int) -> bool:
        operations = 0

        # Step 4: Traverse sorted array in reverse (largest to smallest)
        for num in reversed(nums):
            if num <= maxBalls:
                break  # No operations needed for smaller bags

            # Calculate required splits for larger bags
            operations += (num - 1) // maxBalls

            if operations > maxOperations:
                return False  # Exceeds allowed operations

        return True