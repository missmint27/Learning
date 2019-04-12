#各种排序算法我的实现
#11111111111.冒泡排序
#从前往后一对儿一对儿比对，顺序不对交换
def bubbleSort(array):
	for i in range(0,len(array)-1):
		#尾部先排好 内层循环:遍历未排序好的部分
		for j in range(0,len(array)-1-i):
			if array[j]<=array[j+1]:
				continue
			else:
				temp = array[j+1]
				array[j+1] = array[j]
				array[j] = temp

	return print("bubbleSort:",array)
#22222222222222.选择排序
#每一趟假设未排序的第一个最小，然后在它后面的数组中找到更小的，交换
def selectionSort(array):
	for i in range(0,len(array)-1):
		minIndex = i
		#头部先排好 内层循环：遍历未排序好的部分
		for j in range(i+1,len(array)):
			if array[j]<array[minIndex]:
				minIndex = j
		temp = array[i]
		array[i] = array[minIndex]
		array[minIndex] = array[i]
	return print("selectionSort:",array)

#333333333333333.插入排序
#对于未排序部分，通过从后往前扫描已排序，找到相应位置并插入
def insertionSort(array):
	for i in range(1,len(array)):
		#头部先排好 内层循环：控制将拿到的元素放到前面有序序列中正确位置的过程
		for j in range(i,0,-1):
			if array[j]<array[j-1]:
				array[j],array[j-1] = array[j-1],array[j]
	return print("insertionSort:",array)

#44444444444444444.希尔排序（缩小增量排序）
#把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；
#随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。
def shellSort(array):
	#设定初始增量 //取整数 向下取整
	gap = len(array)//2
	while gap>=1:
		#从最靠后一组开始比对
		for i in range(gap,len(array)):
			k = i
			#当前面的数字不超出数组index时
			while (k-gap)>=0:
				#比对当前位置与减少gap位置的大小并交换
				if array[k-gap]>array[k]:
					array[k],array[k-gap] = array[k-gap],array[k]
					k -= gap #只与同等增量的相同位置数字比对
				else:
					break
		#当最后一组比对完成之后 gap//2
		gap //=2
	return print("shellSort:",array)

#55555555555555555.归并排序（分治法）递归
#len/2比对 其中再分成两部分比对 。。。最小为2个数字比对 排序
'''
递归求解方法：
1. 一定是先找到最小问题规模时的求解方法
2. 然后考虑随着问题规模增大时的求解方法
3. 找到求解的递归函数式后（各种规模或因子），设计递归程序即可
'''
def mergeSort(array):
	#最小规模 len为1
	if len(array)<=1:
		return array
	m = len(array)//2
	# 分别对左右两个列表进行处理，分别返回两个排序好的列表
	l = mergeSort(array[:m])
	r = mergeSort(array[m:])
	# 对排序好的两个列表合并，产生一个新的排序好的列表
	return merge(l,r)
"""合并两个已排序好的列表，产生一个新的已排序好的列表"""
def merge(l,r):
	result = []
	i = 0
	j = 0
	# 对两个列表中的元素 两两对比。
    # 将最小的元素，放到result中，并对当前列表下标加1
	while i < len(l) and j < len(r):
		if l[i]<=r[j]:
			result.append(l[i])
			i+=1
		else:
			result.append(r[j])
			j+=1
	result+=l[i:]
	result+=r[j:]
	return result

#6666666666666666.快速排序  递归
#通过一趟排序将待排记录分隔成独立的两部分，其中一部分记录的关键字均比另一部分的关键字小
#则可分别对这两部分记录继续进行排序，以达到整个序列有序。
#1.
def quickSort(array):
	if len(array)>1:
		qsort(array,0,len(array)-1)
def qsort(array,start,end):
	key = array[start]
	l = start
	r = end
	while l < r:
		while l < r and array[r]>=key:
			r-=1
		if l == r:
			break
		else:
			array[l],array[r] = array[r],array[l]
		while l < r and array[l]<=key:
			l+=1
		if l == r:
			break
		else:
			array[l],array[r] = array[r],array[l]
	#l==r
	if l-1>start:
		qsort(array,start,l-1)
	if r+1<end:
		qsort(array,r+1,end)

#2.
def quicksort(array):
    if len(array) <= 1:
        return array
    # 左子数组
    less = []
    # 右子数组
    greater = []
    # 基准数
    key = array.pop()
    # 对原数组进行划分
    for x in array:
        if x < key:
            less.append(x)
        else:
            greater.append(x)
    # 递归调用
    return quicksort(less) + [key] + quicksort(greater)

#7777777777777.堆排序
	
if __name__ == '__main__':
	array = [6,8,4,3,9,2,10,-1,5]
	#bubbleSort(array)

	#selectionSort(array)

	#insertionSort(array)

	#shellSort(array)

	#result = mergeSort(array)
	#print("mergeSort:",result)

	#quickSort(array)
	#print("quickSort:",array) #的原数组进行原地排序

	#result = quicksort(array)
	#print("quicksort2:",result)

















