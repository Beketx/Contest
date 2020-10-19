# Contest
Leetcode, Hackerrank, Codeforce

Chapter 1
Время выражается как O(n)
Скорость алгоритмов не измеряется в секундах
Время выполнения алгоритма описывается ростом кол. операций
Бинарный пойск быстрее просого
О большое считает в худшем случае

Binary search O(logn)
100/2 50/2 25/2 13/2 7/2 4/2 2/2 1 -> 7 steps
log(2)100 = 7

----------------------------------
19/2020
Chapter 2
Массив, Списки связ, Сортировка выбором
Массив чтение - O(1), вставка - О(n)
Список чтение - О(n), вставка - О(1)

Массив произвольный(рядом с друг другом находятся элементы)
Список последовательнвц(Не обязательно рядом)

Массив быстрое чтение
Список быстрое вставка и удаление

Сортировка выбором О(n^2)
def findSmallest(arr):
	smallest = arr[0]
	smallest_index = 0
	for i in range(1, len(arr)):
		if arr[i]<smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index


def selectionSort(arr):
	newArr = []
	for i in range(len(arr)):
		smallest = findSmallest(arr)
		newArr.append(arr.pop(smallest))
	return newArr

print selectionSort([5,3,6,2,10])