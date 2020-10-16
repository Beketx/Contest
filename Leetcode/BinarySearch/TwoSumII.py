def twoSum(A,n):
	low = 0
	high = len(A) - 1

	while low<=high:

		mid = (low+high)//2
		next = mid + 1
		prev = mid - 1
		if A[mid] + A[next] > n:
			high = mid - 1
		elif A[mid] + A[next] < n:
			low = mid + 1
		elif A[mid] + A[next] == n:
			return (mid,next)
		elif A[mid] + A[prev] == n:
			return (prev,mid)


A=[2,3,4]
print(twoSum(A,6))