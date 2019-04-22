'''
手串上的任意一种颜色（不包含无色），在任意连续的m个串珠里至多出现一次（注意这里手串是一个环形）。
手串上的颜色一共有c种。现在按顺时针序告诉你n个串珠的手串上，每个串珠用所包含的颜色分别有哪些。
请你判断该手串上有多少种颜色不符合要求。即询问有多少种颜色在任意连续m个串珠中出现了至少两次。

第一行输入n，m，c三个数，用空格隔开。(1 <= n <= 10000, 1 <= m <= 1000, 1 <= c <= 50) 
接下来n行每行的第一个数num_i(0 <= num_i <= c)表示第i颗珠子有多少种颜色。
接下来依次读入num_i个数字，
每个数字x表示第i颗柱子上包含第x种颜色(1 <= x <= c)
5 2 3
3 1 2 3
0
2 2 3
1 2
1 3
'''

import sys
#珠子个数 珠子间距 颜色种类 
n,m,c = map(int,input().split())
#color={颜色：位置(因为是环，所以要添加头尾相接部分)}
color = {}
for i in range(0,n):
	zhu=list(map(int, input().split()[1:]))
	for j in zhu:
		if j not in color:
			color[j] = [i]
		else:
			color[j].append(i)
		if i<m:
			color[j].append(i+n)
#print(color)
count = 0
for i in color:
	val = color[i]
	val.sort()
	for i in range(1,len(val)):
		#两颗有该颜色的珠子间距小于m
		if val[i]-val[i-1]<m:
			count+=1
			break
print(count)
	

