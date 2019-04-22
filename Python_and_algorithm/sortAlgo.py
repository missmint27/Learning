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
    less = []# 左子数组    
    greater = []# 右子数组
    key = array.pop()# 基准数
    # 对原数组进行划分
    for x in array:
        if x < key:
            less.append(x)
        else:
            greater.append(x)
    # 递归调用
    return quicksort(less) + [key] + quicksort(greater)

#7777777777777.堆排序 (完全二叉树的结构) 使用Python里面的双向队列deque
#大根堆：每个节点都比自己的孩子大   小根堆：每个节点都比自己的孩子小
#使用大根堆并且升序排列的思想为：首先排列为大根堆，第一个元素最大，和最后一个交换（确定了最大的）
#剩下的元素再次塑造大根堆，第一个元素又是最大，再放到倒数第二个位置
#ki<=k2i and ki<=k2i+1       and 1<=i<=n//2   
#ki>=k2i and ki>=k2i+1  
       
def heapSort(L): 
	len_L = len(L)-1
	first_sort_count = len_L//2
	#把队列调整为大根堆
	#first_sort_count-i是有孩子的节点
	for i in range(first_sort_count):
		heap_adjust(L,first_sort_count-i,len_L)
	#把栈顶元素与堆末尾元素交换，并且将剩下元素调整为大根堆
	for i in range(len_L-1):
		L = swap_param(L, 1, len_L - i)
		heap_adjust(L, 1, len_L - i - 1)
	return [L[i] for i in range(1, len(L))]
#调整大根堆，其实就是按照从右往左，从下到上的顺序，把每颗小树调整为一个大根堆
#把每个子树的根节点和较大的子节点进行值交换。而且如果在左子树 依然是根节点的情况下继续进行调整。
def heap_adjust(L,start,end):
	temp = L[start]
	i = start
	j = 2 * i
	while j <= end:
		if (j < end) and (L[j] < L[j + 1]):
			j += 1
		if temp < L[j]:
			L[i] = L[j]
			i = j
			j = 2 * i
		else:
			break
	L[i] = temp
def swap_param(L,i,j):
	L[i],L[j] = L[j], L[i]
	return L


#888888888.计数排序：只能排序非负整数  不是基于比较的排序算法
'''
找出待排序的数组中最大和最小的元素；
统计数组中每个值为i的元素出现的次数，存入数组C的第i项；
对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）；
反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1。
'''
def countingSort(array):
	k = max(array)
	n = len(array)  # 计算a序列的长度
	o = [0 for i in range(n)]  # 设置输出序列并初始化为0
	c = [0 for i in range(k + 1)]  # 设置计数序列并初始化为0，
	for i in array:
		c[i] += 1        #统计每一个元素出现的次数
	for i in range(1, len(c)):
		c[i] += c[i-1]   #计算要放的位置：统计每一个元素等于或者小于它的元素个数, 从第一个(不是第0个开始)
	for i in array:      #遍历每数组A中每一个数, 放在相应的数组B中的位置
		o[c[i] - 1] = i  #C[A[i]]表示等于或者小于元素的个数, 在B数组中的下标应该-1
		c[i] -= 1        #C中的计数-1
	print(o)

#999999.桶排序：
#把数组a划分为n个大小相同子区间（桶），每个子区间各自排序，最后合并。
#桶排序要求数据的分布必须均匀，不然可能会失效。
#计数排序是桶排序的一种特殊情况，可以把计数排序当成每个桶里只有一个元素的情况
'''
设置一个定量的数组当作空桶；
遍历输入数据，并且把数据一个一个放到对应的桶里去；
对每个不是空的桶进行排序；
从不是空的桶里把排好序的数据拼接起来
'''
def bucketSort(array):
	o = []
	buckets = [0] * (max(array)-min(array)+1) #初始化桶
	for i in array:
		buckets[i-min(array)] += 1  # 遍历数组a，在桶的相应位置累加值
	for i in range(len(buckets)):
		if buckets[i] != 0:
			o += [i + min(array)] * buckets[i]
	print(o)

	
if __name__ == '__main__':
	#array = [6,8,4,3,9,2,10,-1,5]
	#bubbleSort(array)

	#selectionSort(array)

	#insertionSort(array)

	#shellSort(array)

	'''
	result = mergeSort(array)
	print("mergeSort:",result)
	'''
	'''
	quickSort(array)
	print("quickSort:",array) #的原数组进行原地排序
	'''
	'''
	result = quicksort(array)
	print("quicksort2:",result)
	'''
	'''from collections import deque
	L = deque([50, 16, 30, 10, 60,  90,  2, 80, 70])
	L.appendleft(0)
	print(heapSort(L))
	'''
	array = [6,8,4,3,9,2,10,2,3,4,2,2,3,6,5]
	#countingSort(array)
	bucketSort(array)

















