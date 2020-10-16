def guessNumber(self, n: int) -> int:
	low = 0
	high = n

	while low<=high:
		mid = (high+low)//2
		find = guess(mid)
		if find == 0:
			return mid

		elif find == -1:
			high = mid - 1
		else:
			low = mid + 1