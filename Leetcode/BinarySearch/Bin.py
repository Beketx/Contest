    def search(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1
        if not(nums[low]<=target<=nums[high]):
        	return -1
        
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] <= target:
            	low = mid + 1
            elif nums[mid] >= target:
            	high = mid - 1

    	return -1


	# def search(self, nums, target):
	#   if not (nums[0] <= target <= nums[-1]):
	#       return -1
	#   lo = 0
	#   hi = len(nums) - 1
	#   while(lo <= hi):
	#       mid = (lo + hi) // 2
	#       if nums[mid] == target:
	#           return mid
	#       elif nums[mid] > target:
	#           hi = mid - 1
	#       else:
	#           lo = mid + 1
	#   return -1