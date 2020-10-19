def CountOccurence(A,n):
	low = 0
	high = len(A) - 1
	cnt = 0
	while low<=high:
		mid = (low+high)//2

		if A[mid]==n:
			cnt+=1
			A.pop(n)
		elif A[mid]>n:
			high=mid-1
		elif A[mid]<n:
			low=mid+1
	return cnt
Arr = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
num = 5
print(CountOccurence(Arr,num))

# def CountOccurenceTwo(A,n):
# 	low = 0
# 	high = len(A) - 1
# 	while low<=high:
# 		mid = (low+high)//2

# 		if A[mid]==n:
# 			A.pop(n)
# 			return True
# 		elif A[mid]>n:
# 			high=mid-1
# 		elif A[mid]<n:
# 			low=mid+1
# 	return False

# cnt=0
# A = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
# n = 5
# result = CountOccurenceTwo(A,n)
# if result!=-1:
# 	cnt+=1
# 	