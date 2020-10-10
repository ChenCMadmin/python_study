'''
python中的字典规定则是 一对一 列如：my_dict = {'name':'班长'}这里的name 对应的就是'班长' 这个值 不能够对应别的.
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值 key => value对 用冒号 : 分割
每个键值对之间用逗号 , 分割
整个字典包括在花括号 {} 中 ,格式如下所示：
字典的格式:
	d = {key1 : value1, key2 : value2, ... }
'''
my_dict = {'name':'班长', 'id':100, 'sex':'f', 'address':'地球亚洲中国北京'}

# 根据键 - -->访问值
print(my_dict['name'])

# 需要注意:若访问不存在的键，则会报错，列如下方语句
# print(my_dict['neme'])

print(my_dict.get('neme',))   #使用get方法,如果没有当前的key,则返回None
print(my_dict.get('neme','没有该键值'))   #可以设置一个默认值,如果没有当前的key值时, 则返回默认参数

'''
# 使用字典保存
# 格式: 字典名 = {键值1: 实值1, 键值2: 实值2, .....}
# 键值1: 实值1 统称为 键值对  key value 也称之为元素
# 键值数据类型的选择: 必须是不可变的
# 键值 的名字不能重复(才能完成1对1 通过一个key 获取key 的value)
# 字典的key 一般都是使用字符串
# 字典的value 没有规定 (可以重复
'''



