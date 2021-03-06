'''
函数定义的简单规则：

函数代码块以 def 关键词开头，后接函数标识符名称和小括号 ()。
函数内容以冒号开始，并且必须要缩进。
Python 定义函数使用 def 关键字，一般格式如下:

def 函数名（）:
	函数体

'''

def function() :
    print('函数')

# 调用函数很简单，通过 函数名() 即可完成调用

function()      #调用函数

'''
注意:
每次调用某个函数时，该函数体都会从头开始执行
当这个函数中的代码执行完毕后，意味着调用结束
函数的定义一定要在函数调用之前.否则会找不到函数
'''

