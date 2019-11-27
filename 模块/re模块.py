# coding= utf-8
import re
"""
查找模块
match(pattern,string,flags=0)
功能：尝试从字符串string的启始位置匹配一个pattern模式，如果不是启始位置匹配成功的话就返回
None,
参数
pattern 匹配的正则表达式
string要匹配的字符串
flags标志位，用于控制正则表达式的匹配方式（是否大小写，等）
re.L本地化识别匹配
re.I 匹配大小写不敏感
re.M多行匹配形象^和$
re.S 使用.匹配包括换行符在内的所有字符
re.U根据unicode字符解析字符，影响\w\W\b\B
re.X通过给与我们功能灵活的格式以便更好的理解正则表达式
"""
print(re.match("www", "www.124.com"))
"""
search
原型：(pattern,string,flags=0)
功能：扫描整个字符串，并返回第一个成功的匹配
findall（）
功能：扫描整个字符串，并返回结果的列表

"""
# 切分字符串
str = "tony is good      man，tony is"
print(re.split(r" +", str))
#类似findall，但是返回一个迭代器，可以通过next迭代
print(next(re.finditer("tony", str)))#或
for i in re.finditer("tony", str):
    print(i)
# 字符的修改和替换,（pattern，repl, string, count= 0代表全部, flags = 0）
# 2个区别：sub返回一个被替换的字符串，subn返回一个tuple，
# tuple第一个元素为被替换的字符串，第二个元素为发生的多少次替换
print(re.sub("(tony)", "long", str))
print(re.subn("(long)", "tony", str))
#分组
#除了简单的判断是否匹配之外，正则患有提取子串的功能，用（）表示的就是要提取的分组
m = re.search(r"(?P<quhao>\d{3})-(\d{8})","010-56781234")
print(m)
#使用组序号获取匹配的字符串，0表示原数据,组的排序，重从外到内，从左到右
print(m.group(0))
print(m.group(1))
# 查看各组匹配的数据,组成一个tuple
print(m.groups())
# 编译（使用正则表达式时，re模块会做2个事情，1件是编译正则表达式，如果错误，报错，另一个用编译后的
# 的正则去匹配字符串）
re_phone = re.compile(r"(?P<quhao>\d{3})-(\d{8})")
# re_phone.match()

"""
正则表达式  和centos一样
[a-zA-Z0-9]字符和数字
\D 非0-9
\d 0-9
\W  非|w
\w  任意字母/下划线/数字/汉字
\s  任意空白符（空白符/换页/回等）
\S  非|s
锚字符
^行首
$行尾
边界字符
\A 匹配字符串开始，和^区别是\A只匹配整个字符的开肉，即使不再re.M模式下也不会匹配其他的行首
\Z匹配字符串开始，和$区别是\A只匹配整个字符的开肉，即使不再re.M模式下也不会匹配其他的行尾
\B匹配非单词边界
\b匹配一个单词的边界，指单词和空格的位置查找

"""

