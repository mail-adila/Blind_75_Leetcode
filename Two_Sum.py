"""
Problem Description:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :param nums: list of elements entered by the user
        :param target: the sum of the numbers that we are looking for
        :return: list of indices that make the targert when summed
        """
        result = []
        for i in range(0, len(nums)):
            next_num = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == next_num:
                    result.extend([i, j])
        return result


def main():
    nums = []
    # Enter the list size to take that many inputs from the user
    size = int(input("Enter the number of elements in list"))
    print("Enter the list of elements - no duplicates")
    for i in range(0, size):
        nums.append(int(input()))
    target = int(input("Enter the target"))
    output = Solution()
    result = output.twoSum(nums, target)
    print(result)


main()
