class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # appeared = set()
        # for i in nums:
        #     if i not in appeared:
        #         appeared.add(i)
        #     else:
        #         return True

        # return False

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False