def paixu(lists,stack):
	print(lists)
	if not lists:
		return stack   # 到树的最后，输出结果
	else:   # 没有到树的叶子节点的时候，使用递归继续往下找。
		for i in range(len(lists)):
			stack.append(lists[i])
			del lists[i]
			paixu(lists,stack)
			lists.insert(i,stack.pop())
			print("lists",lists)

lists = ['AB','RAAB','RA']
stack = []
result = paixu(lists,stack)
print(result)