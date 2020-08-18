# def shuffle(nums, n):
# 	x = len(nums)
# 	result = list()
# 	if x % n == 0:	
# 		for i in range(n):
# 			result.append(nums[i])
# 			result.append(nums[n])
# 			n+=1
# 	print(result)
# 	return result
# nums = [1,2,3,4,5,6]	
# shuffle(nums, 3)




# def shuffle(nums, n):
# 	lst = list()
# 	for i in range(n):
# 		lst+=[nums[i]]
# 		lst+=[nums[i+n]]
# 	print(lst)

# shuffle(nums, 3)


def shuffle(nums, n):
	res = []
	for i, j in zip(nums[:n], nums[n:]):
		res += [i,j]
	return res


nums = [1,3,5,2,4,6]

print(shuffle(nums, 3))