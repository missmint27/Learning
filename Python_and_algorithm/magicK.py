#魔法权值
'''lis = raw_input().split() #获取n,k
n=int(lis[0])
K=int(lis[1])
i = 0
st1 = [] #存放输入字符串列表
strlen = 0 #统计所有字符串长度

while(i<n):  #从用户输入获取各个字符串，放入mystring[]
    ms = raw_input()
    strlen += len(ms)
    str1.append(ms)
    i+=1
mybei[]中存放所有可能的i。
如果字符串循环左移 i 次后得到的字符串仍和原字符串全等，
则要求i是该字符串长度的因数'''
n=3 
K=2
lists = ['AB','RAAB','RA']
strlen = 0
for item in lists:
	strlen+=len(item)
#递归全排列
import copy
import operator
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

def magicK(n,K,str1,str2):
	tempK = 0
	for i in range(1,len(str1)+1):
		str3 = str2[i:]+str2[:i]
		#print(str1,str2,str3)
		if operator.eq(str1,str3):
			tempK+=1
	#print(tempK,"\n")
	if tempK == K:
		return True

stack = []
allstr = []
paixu(lists,stack)
countK=0
for anystr in allstr:
	#print("anystr:",anystr)
	if magicK(n,K,"".join(lists),"".join(anystr)):
		countK +=1
print(countK)


