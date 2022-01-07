"""
1、如果需要使用变量保存以下字符串，我们该如何书写代码
鲁迅说:"我没有说过这句话"
"""
_str = '鲁迅说:"我没有说过这句话"'
print(_str)


"""
2、做一个简单的用户信息管理系统：
提示用户依次输入姓名，年龄和爱好
并且在输入完成之后，一次性将用户输入的数据展示出来
"""
u_name = input("请输入姓名：")
u_age = input("请输入年龄：")
u_hobby = input("请输入爱好：")
print("你的姓名是{}，年龄是{}，爱好是{}".format(u_name, u_age, u_hobby))

"""
3、现有字符串如下，请使用切片提取出ceg
words = "abcdefghi"
"""
words = "abcdefghi"
print(words[2:7:2])

"""
4、有一个列表，判断列表中的每一个元素是否以s或e结尾，如果是，则将其放入一个新的列表中，最后输出这个新的列表
list = ["red", "apples", "orange", "pink", "bananas", "blue", "black", "white"]
"""
_list = ["red", "apples", "orange", "pink", "bananas", "blue", "black", "white"]
new_list = []
for i in _list:
    if i.endswith("s") or i.endswith("e"):
        new_list.append(i)
print(new_list)

"""
5、给定一个列表，首先删除以s开头的元素，删除后，修改第一个元素为"joke"，并且把最后一个元素复制一份，放在joke的后边
list = ["spring", "look", "strange", "curious", "black", "hope"]
"""
_list = ["spring", "look", "strange", "curious", "black", "hope"]
for i in _list:
    if i.startswith("s"):
        _list.remove(i)
print(_list)
_list[0] = "joke"   # 修改第一个元素
_list.insert(1, _list[-1])
print(_list)

"""
6、有如下两行代码：
tuple1 = (2)
tuple2 = (2,)
请问tuple1与tuple2有什么不同
"""
tuple1 = (2)
tuple2 = (2,)
print(type(tuple1), type(tuple2))


"""
7、现有：type1 = ("tom","kaisa","alisi","xiaoming","songshu")
我想获得“alisi”这个内容，你能否想到三种方法来做？
"""
type1 = ("tom", "kaisa", "alisi", "xiaoming", "songshu")
print(type1[2])
print(type1[2:3])
for i in type1:
    if i == "alisi":
        print(i)

"""
8、有如下元组：
typle1 = ("tom","kaisa","alisi","xiaoming","songshu")
求出他的长度
"""
type1 = ("tom", "kaisa", "alisi", "xiaoming", "songshu")
print(len(type1))
