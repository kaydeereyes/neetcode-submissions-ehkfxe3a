class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = 0

        numCount = dict()
        for num in set(nums):
            numCount[num] = nums.count(num)
        numCount = sorted(numCount.items(), key=lambda item: item[1], reverse=True)

        return [count[0] for count in numCount[:k]]