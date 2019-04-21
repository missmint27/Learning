'''
https://www.nowcoder.com/questionTerminal/43488319efef4edabada3ca481068762
【编码题】字符串S由小写字母构成，长度为n。定义一种操作，
每次都可以挑选字符串中任意的两个相邻字母进行交换。
询问在至多交换m次之后，字符串中最多有多少个连续的位置上的字母相同？

输入：第一行为一个字符串S与一个非负整数m。(1 <= |S| <= 1000, 1 <= m <= 1000000)
输出：一个非负整数，表示操作之后，连续最长的相同字母数量。
abcbaa 2
2


dp[i][j]表示字符a第i个位置到第j个位置的字符要全部相邻，至少要用需要多少次交换
1. i==j时，表示一个字符，不用交换，dp(i,j)为0；
2. i+1==j时，表示两个字符，位置相差arr[j]-arr[i]；
3.其他情况，dp[i][j] = dp[i+1][j-1] + arr[j]-arr[i] - (j - i)

动态规划。
以a字符为例，令dp[i][j]表示将从第i个a字符（包含）到第j个a字符（包含）之间的
所有a字符移动到一起的交换次数，我们可以知道将所有的字符往中间移动的代价是最小的，
同时，假设从第i+1个a字符到第j-1个a字符之间的所有字符a都已经移动到一起了，无论它们的位置如何，
则只需把i位置和j位置的a字符往中间移动，即可得到把第i个a字符（包含）到第j个a字符（包含）之间的
所有a字符移动到一起的最小操作次数，
且该步骤的操作次数一定为第j个a字符的下标减去第i个a字符的下标加一再减第i+1个a字符到第j-1个a字符之间的所有字符a的数量。
动态转移方程为
dp[i][j] = dp[i + 1][j] + (index[j] – indexAfterMove[j – 1] – 1) + (indexAfterMove[i + 1]  – index[i] – 1)
= dp[i + 1][j] + (index[j] – index[i]) – (indexAfterMove[j – 1] – indexAfterMove[i + 1])  – 2
= dp[i + 1][j] + (index[j] – index[i]) – len(i + 1, j – 1)  – 1
'''
import string
line1 = input().split()
S = list(map(str,line1[0]))
m = int(line1[1])#
chardic = dict.fromkeys(string.ascii_lowercase, 0)
Sdic = {}
for i in range(len(S)):
	if S[i] not in Sdic:
		Sdic[S[i]] = [i]
	else:
		Sdic[S[i]].append(i)
#print(Sdic)

result = 0
for char in Sdic:
	indexlist = Sdic[char]
	dp = [[0]*len(indexlist) for i in range(len(indexlist))]
	for i in range(len(indexlist)-1):
		dp[i][i + 1] =  indexlist[i + 1] - 1 - indexlist[i]
	for num in range(2,len(indexlist)+1):
		for i in range(len(indexlist)-num+1):
			dp[i][i + num - 1] = dp[i + 1][i + num - 2]  + indexlist[i  + num - 1] - indexlist[i] + 1 - num
			if dp[i][i + num - 1] <= m:
				#print("k ",indexlist[i], " ",indexlist[i  + num - 1]," ",num," ",dp[i][i + num - 1])
				result = max(result, num)

print(result)



