#字符串的基本处理
#切片
a = ' b 2, _lki,l'
b = a.split(',')
print(b)
#大写
print(a.upper())
#去掉空格及特殊符号
#去掉左侧的空格
print(a.strip())
print(a.lstrip(' b '))
print(a.rstrip(',l'))
#查找一个字符
print(a.index('b'))
print(a.find('b'))
#比较一个字符，用in not in 或者用cmp，在python3需要重新查找dir
b = 'lkl'
print(b in a)
#变成大小写lower是变成小写
print(a.upper())
print(a.upper().lower())
#翻转字符串
print(a[::-1])
#进行排序
print(sorted(a))
#正则表达式
'''验证工具 http://egexr.com/
.  点表示除换行符\n外所有的字符
\  转义字符，使后一个字符转义
{..} 表示前一个字符的个数和格式或者区间段，贪婪匹配先匹配最多的
\d  表示所有的数字
\D  除数字外的字符
\s  表示所有的空格\t\r\n\f\v
\S  除空格和换行符
\w  表示A-Za-z0-9_
\W  除\w的字符
*   匹配前一个字符0或者无限次
+   匹配前一个字符1或者无限次
？  匹配前一个字符0次或者1次
{m} 匹配前一个字符m次
^   匹配字符串的开头，在多行匹配每行的开头
$   匹配字符串的末尾，在多行匹配每行的末尾
\A  仅匹配字符串开头
\Z  仅匹配字符串末尾
\b  匹配\w与\W之间
\B  \b的取反
|   组合几个模式组合或者
()  表示组合，若里面为数字时表示在组合中匹配的步骤
[]  表示指定的字符
练习网站：Regex Golf
'''
