def findRotations(A):

	high = len(A)-1
	low = 0
	#as we always making low++ and high= mid - 1, we make while loop
	while low<=high:
		#first case when first element is the lowest
		if A[low]<=A[high]:
			return low

		mid = (low+high)/2
		next = mid + 1
		prev = mid - 1

		if A[prev] >= A[mid] and A[mid]<=A[next]:
			return mid

		elif A[high]>=A[mid]:
			high = mid-1

		elif A[low]<=A[mid]:
			low = mid+1

	return -1

if __name__ == '__main__':

	A = [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
	print("This list is rotated", findRotations(A), "times")