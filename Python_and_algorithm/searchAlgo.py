'''查找算法
静态查找：在查找过程中，只是对数据元素执行查找操作，而不对其执行其他操作。
	顺序查找/二分查找/索引查找
动态查找：在查找过程中，不仅对数据元素执行查找操作，同时还执行其他操作，如插入和删除等。
	哈希表查找/二叉树查找
'''

#1.顺序查找
#从头到尾挨个查找
#顺序查找有三种情形可能发生：最好的情况，第一项就是要查找的数据对象，只有一次比较，
#最差的情况，需要 n 次比较，全部比较完之后找不到数据。平均情况下，比较次数为 n/2 次。算法的时间复杂度是 O(n)
class sequenceSearch:
	def __init__(self,array):
		self.array = array
	def sequSearch(self,key):
		findindex = -1
		for i in range(0,len(self.array)):
			if self.array[i] == key:
				findindex = i
				break
		return i
	def maxAndIndex(self):
		pos = 0
		maxNum = self.array[0]
		for i in range(0,len(self.array)):
			if self.array[i] > maxNum:
				pos = i
				maxNum = self.array[i]
		return pos,maxNum	
	def minAndIndex(self):
		pos = 0
		minNum = self.array[0]
		for i in range(0,len(self.array)):
			if self.array[i] < minNum:
				pos = i
				minNum = self.array[i]
		return pos,minNum		

#2.二分查找（折半查找）：折半查找要求线性表必须采用顺序存储结构，而且表中元素按关键字有序排列。
#确定查找区间后，从区间的中间位置开始，如果与给定值相等，则查找成功，如果大于给定值，在左半部分继续寻找，如果小于给定值，在右半部分继续寻找。
class binarySearch:
	def __init__(self,array):
		self.array = array
	def bSearch(self,key):
		low = 0
		high = len(self.array)-1
		while low<high:
			mid = (high+low)//2
			if key > self.array[mid]:
				low = mid+1
			elif key<self.array[mid]:
				high = mid-1
			else:
				return mid 
		return -1

if __name__ == '__main__':
	array = [1,3,5,6,7,8,9,11,23,44]
	'''stable = sequenceSearch(array)
	findindex = stable.sequSearch(23)
	maxIndex,maxNum = stable.maxAndIndex()
	minIndex,minNum = stable.minAndIndex()
	print(findindex,maxIndex,maxNum,minIndex,minNum)'''

	btable = binarySearch(array)
	findindex = btable.bSearch(4)
	print(findindex)



