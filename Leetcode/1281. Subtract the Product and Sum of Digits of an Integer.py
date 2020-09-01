# class Solution:
#     def subtractProductAndSum(self, n: int) -> int:
#         x = 0
#         suma = 0
#         umna = 1
#         while n/10!=0:
#             x = n%10
#             suma+=x
#             umna*=x
#             n=n//10
#         result = umna - suma
#         return result
	
def subtractProductAndSum(n):
	A = map(int, str(n))
	X = reduce(operator.mul, A)-sum(A)
	return X

print(subtractProductAndSum(234))