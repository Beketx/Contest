# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         length = len(nums)
#         sum = [None]*len(nums)
#         for k in range(length):
#             sum[k]=0
#             for j in range(length):
#                 if nums[k]>nums[j]:
#                     sum[k]+=1
#         return sum


class Solution:
	def smallerNumbersThanCurrent(self, nums: List[int] -> List[int]):
		result = []
		tempNums=nums.copy()
		nums.sort()
		for k in tempNums:
			result.append(nums.index(k))
		return result