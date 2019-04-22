'''
    现有一个M*N的表格，请统计表格中每行最小数值之和。要求最小数的都在不同列中，
    既假设第一行第一列数是最小数，那即使第二行第一列的数在第二行中不去计算。
    example: 
    存在如下表格：
    1 2 3
    2 4 5
    则：
    第一行最小数是1，第二行最小数是4，和为5。表格数据输入形式自定，使用python语言编写。
'''

def finMin(array):
	columnAndRow=[]
	MinTotal = 0
	for i in range(0,len(array)):
		for j in range(0,len(array[i])):
			if j not in columnAndRow:
				minNum = min(array[i])
				minNumIndex = array[i].index(minNum)
				columnAndRow.append(minNumIndex)
				MinTotal+=minNum			
				break
			else:
				maxNum = max(array[i])
				array[i][j] = maxNum
				minNum = min(array[i])
				minNumIndex = array[i].index(minNum)
				columnAndRow.append(minNumIndex)
				MinTotal+=minNum
				break
	print(MinTotal)
finMin([[1,2,3],[2,4,5]])



'''import random
def table(list):
    #记录所选列编号集合
    columnNumSet = set()
    #记录总值
    TotalNum = 0
    for row in list:
        #记录当前列号
        columnNum = 0
        #记录下标集合
        temp=random.choice([row[x] for x in range(len(row)) if x not in columnNumSet])
        print("random:",row,temp)
        #随机选一个数字，然后看下标是否在columnNumSet中,不在的话才可以继续比较大小（并找到最小的）
        for num in range(0,len(row)):
            if not num in columnNumSet:
                if row[num] <= temp:
                    temp = row[num]
                    columnNum = num
        TotalNum += row[columnNum]
        columnNumSet.add(columnNum)
    print(TotalNum)
TotalNum = table(((1,2,3),(2,4,5)))
'''
