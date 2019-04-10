#Python实现一个类
#应用于list实现stack

'''
类：模板，描述一类对象的行为和形态。是对现实世界中一些事物的封装
类定义完之后就产生了类对象
类对象的两种操作：
1.引用：调通过类对象用类中的属性或者方法
2.实例化：产生类对象的实例
方法：与某个对象进行绑定的函数
实例对象：类的实例化 例如：s=stackByList() 为初始化一个“stack” s，s就具有了类里面的属性和方法
'''
class stackByList(object):
	"""
	此处是类的属性=变量
	variableName = xx;   为全局变量,可以在类外通过对象名访问
	__variableName = xx;   为局部变量
	
	在类中定义的方法至少会有一个参数，一般以名为'self'的变量作为该参数，而且需要作为第一个参数
	self:类的实例  self.equals(stackByList)
	s.pop() == stackByList.pop(s)

	构造方法__init__(self,....):
	在生成对象时调用，可以用来进行一些初始化操作，不需要显示去调用，系统会默认去执行
	析构方法__del__(self):
	在释放对象时调用，支持重载，可以在里面进行一些释放资源的操作，不需要显示调用。
	"""
	def __init__(self):
		#super(ClassName, self).__init__()
		self.stack = []

	def push(self,item):
		self.stack.append(item)
		return self.stack

	def pop(self):	
		return print(self.stack.pop())

	def peek(self):
		return print(self.stack[len(self.stack)-1])

	def show(self):
		return print(self.stack)

	def size(self):
		return print(len(self.stack))

	def is_empty(self):
		return print(self.stack == [])


'''
当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；
当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
'''
if __name__ =='__main__':
	s=stackByList()
	s.show()
	s.push(2)
	s.push(3)
	s.push(4)
	s.show()
	s.peek()
	s.pop()
	s.size()
	s.pop()
	s.is_empty()
	s.pop()
	s.show()

		