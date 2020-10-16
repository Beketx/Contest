def firstAndLastOccurence(A,n):
	low = 0
	high = len(A)-1

	result = -1

	while low<=high:
		mid = (low+high)//2

		if A[mid]==n:
			result = mid
			high = mid - 1

		elif A[mid]>n:
			high = mid - 1

		elif A[mid]<n:
			low = mid + 1

		else:
			return 'Number %n Not exist in $A'
	return result


if __name__ == '__main__':
	A = [1,2,3,3,3,3,3,3,3,3,3,4,5,6,7,8,9,10,11,12]
	key=13
	index = firstAndLastOccurence(A, key)

	if index != -1:
		print('Last occurnce is at ',str(index))
	else:
		print('Not exist in ',A)