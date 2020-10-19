def intersectionOFTwoArrayII(A,B):

	def binary_search(C,target):
		low = 0
		high = len(A) - 1

		while low<=high:
			mid = (low+high)//2

			if A[mid]==target:
				A.pop(target)
				return True
			elif A[mid]>target:
				high=mid-1
			elif A[mid]<target:
				low=mid+1
		return False

	if len(A)>len(B):
		A,B=B,A

	A.sort()
	res = []
	for num in B:
		found = binary_search(A,num)
		if found!=-1:
			res.append(A[found])
			A.pop(found)
	return res

A = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
n = [3,2,5]

print(intersectionOFTwoArrayII(A,n))

