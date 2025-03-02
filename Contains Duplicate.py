"""
Given an integer array nums,
return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

class containsDuplicate(object):
    def solution1(self, nums):
        """
        Start with a simple for loop
        I also wondered if I should try sorting the list first.
        """
        exist = []
        for num in nums:
            if num in exist:
                return True
            else:
                exist.append(num)
        return False
    def solution2(self, nums):
        """
        So let's try sorting. After sorting. We can just check  if the next number is the same as the current number in
        the for loop.
        Time complexity will be: O(n log n)
        """
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
    def solution3(self, nums):
        """
        Sorting isn't good enough. Let's go back to the 1st solution and rework what we can do.
        We can try changing the original list into a set, to reduce memory space.
        If the list is converted to the set, any duplicates will be removed,
        thus reducing the size of the data structure.
        The main idea is to try from one data structure to another. We don't care about making the code fast and
        small yet (the algorithm).
        This is like a hash set approach. Time complexity will be O(n).
        """
        exist = set()
        for num in nums:
            if num in exist:
                return True
            else:
                exist.add(num)
        return False
    def solution4(self, nums):
        """
        Ok previous solution works, but didn't really change much.
        We can actually just compare the two sizes of the list and set. Thus implementing an algorithm.
        """
        original_size = len(nums)
        reduce = set(nums)
        new_size = len(reduce)
        if new_size < original_size:
            return True
        else:
            return False
    def solution5(self, nums):
        """
        Previous Solution, but with just one line of code.
        Leetcode reported it is worse in terms of runtime and memory though...
        I seached around, and other users actually have similar code somehow beating 100%
        Both time complexity and space complexity is O(N)
        """
        return len(set(nums)) < len(nums)
    def solution6(self, nums):
        """
        Same as previous Solution, but just changing the operator.
        Again, obviously no improvements.
        Both this and previous solution is already one of the best way to algorithmically operate on this data structure.
        So maybe we can try looking for another data structure to work with.
        """
        return len(set(nums)) != len(nums)

    def solution7(self, nums):
        """
        Sigh, let's try a hash map.
        And it is indeed much better in time complexity and memory space.
        """
        seen = {}
        for num in nums:
            if num in seen:
                return True
            else:
                seen[num] = None
        return False

if __name__ == "__main__":
    solution = containsDuplicate()
    print(solution.solution1(nums=[1,2,3,1]))
    print(solution.solution1(nums=[1,2,3,4]))
    print(solution.solution1(nums=[1,1,1,3,3,4,3,2,4,2]))
    print("--------------------------------------------")
    print(solution.solution2(nums=[1, 2, 3, 1]))
    print(solution.solution2(nums=[1, 2, 3, 4]))
    print(solution.solution2(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
    print("--------------------------------------------")
    print(solution.solution3(nums=[1, 2, 3, 1]))
    print(solution.solution3(nums=[1, 2, 3, 4]))
    print(solution.solution3(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
    print("--------------------------------------------")
    print(solution.solution4(nums=[1, 2, 3, 1]))
    print(solution.solution4(nums=[1, 2, 3, 4]))
    print(solution.solution4(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
    print("--------------------------------------------")
    print(solution.solution5(nums=[1, 2, 3, 1]))
    print(solution.solution5(nums=[1, 2, 3, 4]))
    print(solution.solution5(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
    print("--------------------------------------------")
    print(solution.solution6(nums=[1, 2, 3, 1]))
    print(solution.solution6(nums=[1, 2, 3, 4]))
    print(solution.solution6(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
    print("--------------------------------------------")
    print(solution.solution7(nums=[1, 2, 3, 1]))
    print(solution.solution7(nums=[1, 2, 3, 4]))
    print(solution.solution7(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
    print("--------------------------------------------")