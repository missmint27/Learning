import copy
def paixu(lists,stack):
	global allstr
	if not lists:
		allstr.append(copy.deepcopy(stack))
		#print(stack)   # 到树的最后，输出结果
	else:   # 没有到树的叶子节点的时候，使用递归继续往下找。
		for i in range(len(lists)):
			stack.append(lists[i])
			del lists[i]
			paixu(lists,stack)
			lists.insert(i,stack.pop())

lists = ['AB','RAAB','RA']
stack = []
allstr = []
paixu(lists,stack)
print(allstr)


'''COUNT=0  
def perm(n,begin,end):  
    global COUNT  
    if begin>=end:  
        print(n)  
        COUNT +=1  
    else:  
        i=begin  
        for num in range(begin,end):  
            n[num],n[i]=n[i],n[num]  
            perm(n,begin+1,end)  
            n[num],n[i]=n[i],n[num]  

n=['AB','RAAB','RA']  
perm(n,0,len(n))  
print(COUNT) 
''' 
