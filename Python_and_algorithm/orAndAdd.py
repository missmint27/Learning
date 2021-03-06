'''或与加
给定 x, k ，求满足 x + y = x | y （x&y=0）的第 k 小的正整数 y 。 
| 是二进制的或(or)运算，例如 3 | 5 = 7。
比如当 x=5，k=1时返回 2，因为5+1=6 不等于 5|1=5，而 5+2=7 等于 5 | 2 = 7
x + y = x | y 为x&y=0 既是x为1时y一定不可以是1
x在二进制取1的位上，y不能做出改变，只能取0
'''

def orAndAdd(x,k):
#目标是把k的各位依次填在x中是0的位上
#bit用来移动到x中零的位置，然后把k的最低位放在x的零位上, 
#k左移，将下一位变成最低位,bitNum一直左移，知道x中的下一个为0的位上。
	bit = 1
	ans = 0
	while k:
		#x中当前bit为0的话,把k的最低位放在这儿
	    if x & 1 == 0:  
	    	#k&1是将k的最低位取出来, bit*(k&1)的结果就是得到bit位和当前k的最低位一样的一个数
	    	#而其它位都是0
	        ans += bit*(k&1) 
	        print("x",bin(x))
	        print("ans",bin(ans)) 
	        #而ans原来的bit为肯定为0，ans+(bit*(k&1)) 就将k的最低位放在x的这个零上了。
	        k >>= 1
	    x >>= 1
	    print(bin(x),"  ",bin(k))
	    #bit的1一直左移到x中第k个零的位置
	    bit <<= 1
	    print("bit",bin(bit))
	print(ans)

orAndAdd(5,1)