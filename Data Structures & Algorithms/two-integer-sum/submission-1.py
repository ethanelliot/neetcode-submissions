class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        for i, num in enumerate(nums):
            nums_dict[num] = i

        for i in range(len(nums)):
            remaining = target - nums[i]

            if j := nums_dict.get(remaining, None):
                if i != j:
                    return sorted([i, j])
