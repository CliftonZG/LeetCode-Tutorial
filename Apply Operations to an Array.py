class applyOperations(object):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    """
    Depending on the specifications needed and whether the input data can be directly overwritten, each of these
    solutions might be better than the other.
    """

    def solution1(self, nums):
        """
        Brute Force method by doing exactly what the specifications needs, regardless of Time Complexity and Space Complexity
        """
        n = len(nums)
        modified_nums = []

        # Step 1: Apply operations on the array
        for index in range(0, n - 1):
            if (nums[index] == nums[index + 1]) and (nums[index] != 0):
                nums[index] *= 2
                nums[index + 1] = 0

        # Step 2: Move non-zero elements to the front
        for num in nums:
            if num != 0:
                modified_nums.append(num)

        # Step 3: Append zeros to maintain the original size
        while len(modified_nums) < n:
            modified_nums.append(0)

        return modified_nums

    def solution2(self, nums):
        """
        In the first loop, do the operation if needed as well as, count the amount of zeros in the array.
        In the second loop, create a new array that excludes all the zero.
        In the end, just concatenate a new array of non-zeros with another array of zeros
        """
        zeros = 0
        for i, num in enumerate(nums):
            if i < len(nums) - 1:
                if nums[i] == nums[i+1]:
                    nums[i] = nums[i] * 2
                    nums[i+1] = 0
            if nums[i] == 0:
                zeros += 1
        zero_array = [0] * zeros
        non_zero = []
        for num in nums:
            if num > 0:
                non_zero.append(num)
        return non_zero + zero_array

    def solution3(self, nums):
        """
        Similar to the previous solution, but using only 1 for loop.
        """
        zeros = 0
        non_zero = []
        for i, num in enumerate(nums):
            if i < len(nums) - 1:
                if nums[i] == nums[i+1]:
                    nums[i] = nums[i] * 2
                    nums[i+1] = 0
            if nums[i] == 0:
                zeros += 1
            else:
                non_zero.append(nums[i])
        zero_array = [0] * zeros

        return non_zero + zero_array

    def solution4(self, nums):
        """
        Using only 1 array and 1 while loop.
        Directly modify the nums array by just deleting all zeros, as well doing the operations.
        Then adding the zeros into the end of the nums array.

        In-place algorithms overwrite the input to save space, but sometimes this can cause problems.

        There are a couple of situations where an in-place algorithm might not be suitable:
            The algorithm needs to run in a multi-threaded environment without exclusive access to the array.
            Other threads might need to read the array as well and may not expect it to be modified.
            Even if there is only a single thread or the algorithm has exclusive access to the array while running,
            the array might need to be reused later or by another thread once the lock has been released.
        """
        zeros = 0
        size = len(nums)
        i = 0
        while i < size:
            num = nums[i]
            if num == 0:
                zeros += 1
                del nums[i]
                size -= 1
            else:
                if i < size - 1:
                    if nums[i] == nums[i + 1]:
                        nums[i] = num * 2
                        nums[i + 1] = 0
                i += 1

        return nums + ([0] * zeros)

    def solution5(self, nums):
        """
        Similar to the previous solution, but just subtract the current size from the original size instead, of tracking
        the amount of zeros.

        According to leetcode, this is worse in both time complexity and memory space than the previous solution.
        """
        original = len(nums)
        size = original
        i = 0
        while i < size:
            num = nums[i]
            if num == 0:
                del nums[i]
                size -= 1
            else:
                if i < size - 1:
                    if nums[i] == nums[i + 1]:
                        nums[i] = num * 2
                        nums[i + 1] = 0
                i += 1

        return nums + ([0] * (original-size))

if __name__ == "__main__":
    solution = applyOperations()
    print(solution.solution1(nums=[1,2,2,1,1,0]))
    print(solution.solution1(nums=[0,1]))
    print(solution.solution2(nums=[1, 2, 2, 1, 1, 0]))
    print(solution.solution2(nums=[0, 1]))
    print(solution.solution3(nums=[1, 2, 2, 1, 1, 0]))
    print(solution.solution3(nums=[0, 1]))
    print(solution.solution4(nums=[1, 2, 2, 1, 1, 0]))
    print(solution.solution4(nums=[0, 1]))