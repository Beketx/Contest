def searchElement(A, x):
	low = 0
	high = len(A)-1
	
	while low<=high:
		mid = (low+high)//2
		next = mid + 1
		prev = mid -1

		if A[mid]==x:
			return mid

		if A[mid] <= A[high]:
			if A[mid] < x <= A[high]:
				left = mid + 1
			else:
				high = mid - 1

		else:
			if A[low] <= x < A[mid]:
				high = mid -1
			else:
				low = mid + 1
	return -1


if __name__ == '__main__':

	A = [9, 10, 2, 5, 6, 8]
	key = 5

	index = searchElement(A, key)

	if index != -1:
		print("Element found at index", index)
	else:
		print("Element found not in the list")