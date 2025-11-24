# =============================================================================
# Python 集合数据类型详解：函数大全与类型转换
# =============================================================================

# =============================================================================
# 1. List（列表） - 有序、可变
# =============================================================================

# 创建列表
my_list = [1, 2, 3, 4, 5]
print("原始列表:", my_list)

# 增
my_list.append(6)           # [1, 2, 3, 4, 5, 6]
my_list.insert(1, 1.5)      # [1, 1.5, 2, 3, 4, 5, 6]
my_list.extend([7, 8])      # [1, 1.5, 2, 3, 4, 5, 6, 7, 8]
print("添加元素后:", my_list)

# 删
my_list.remove(1.5)         # 删除第一个匹配项
popped = my_list.pop()      # 删除并返回最后一个元素
popped_index = my_list.pop(0) # 删除并返回指定索引元素
del my_list[1]              # 删除索引1的元素
print("删除元素后:", my_list)

my_list.clear()             # 清空列表
print("清空后:", my_list)

# 重新初始化
my_list = [1, 2, 3, 2, 4, 5]

# 查
index = my_list.index(3)    # 返回第一个3的索引
count = my_list.count(2)    # 统计2出现的次数
length = len(my_list)       # 列表长度
print(f"索引:{index}, 计数:{count}, 长度:{length}")

# 改
my_list[0] = 10             # 修改索引0的元素
my_list.sort()              # 排序（升序）
print("排序后:", my_list)
my_list.sort(reverse=True)  # 降序排序
my_list.reverse()           # 反转列表
print("反转后:", my_list)

# 其他
new_list = my_list.copy()   # 浅拷贝
sliced = my_list[1:4]       # 切片
print("切片:", sliced)

# =============================================================================
# 2. Tuple（元组） - 有序、不可变
# =============================================================================

my_tuple = (1, 2, 3, 2, 4)
print("\n原始元组:", my_tuple)

# 查
index = my_tuple.index(2)   # 第一个2的索引
count = my_tuple.count(2)   # 统计2出现的次数
length = len(my_tuple)      # 元组长度
element = my_tuple[1]       # 访问元素
print(f"索引:{index}, 计数:{count}, 长度:{length}, 元素:{element}")

# 切片
sliced = my_tuple[1:4]      # (2, 3, 2)
print("切片:", sliced)

# 元组解包
a, b, c, d, e = my_tuple
a, *rest, e = my_tuple      # a=1, rest=[2,3,2], e=4
print(f"解包: a={a}, rest={rest}, e={e}")

# =============================================================================
# 3. Dictionary（字典） - 键值对、无序、可变
# =============================================================================

my_dict = {'a': 1, 'b': 2, 'c': 3}
print("\n原始字典:", my_dict)

# 增/改
my_dict['d'] = 4            # 添加新键值对
my_dict.update({'e': 5, 'f': 6}) # 批量更新
my_dict.setdefault('g', 7)  # 键不存在时设置默认值
print("添加后:", my_dict)

# 删
value = my_dict.pop('a')    # 删除键'a'并返回值
key, value = my_dict.popitem() # 删除最后一对键值
del my_dict['b']            # 删除指定键
print("删除后:", my_dict)

my_dict.clear()             # 清空字典
print("清空后:", my_dict)

# 重新初始化
my_dict = {'a': 1, 'b': 2, 'c': 3}

# 查
value = my_dict.get('c')    # 获取值，键不存在返回None
value_default = my_dict.get('x', 0) # 键不存在返回默认值0
keys = list(my_dict.keys())       # 所有键
values = list(my_dict.values())   # 所有值
items = list(my_dict.items())     # 所有键值对
print(f"查找: c={value}, x={value_default}")
print(f"键:{keys}, 值:{values}, 键值对:{items}")

# =============================================================================
# 4. Set（集合） - 无序、不重复、可变
# =============================================================================

my_set = {1, 2, 3, 4, 5}
other_set = {4, 5, 6, 7}
print("\n原始集合:", my_set)

# 增
my_set.add(6)               # 添加元素
my_set.update([7, 8, 9])    # 批量添加
print("添加后:", my_set)

# 删
my_set.remove(1)            # 删除元素，不存在报错
my_set.discard(10)          # 删除元素，不存在不报错
popped = my_set.pop()       # 随机删除并返回一个元素
print("删除后:", my_set)

# 集合运算
union = my_set | other_set        # 并集
intersection = my_set & other_set # 交集
difference = my_set - other_set   # 差集
symmetric_diff = my_set ^ other_set # 对称差集
print(f"并集:{union}, 交集:{intersection}, 差集:{difference}, 对称差集:{symmetric_diff}")

# =============================================================================
# 5. String（字符串） - 有序、不可变
# =============================================================================

my_string = " Hello, World! "
print(f"\n原始字符串: '{my_string}'")

# 大小写转换
lower = my_string.lower()       # " hello, world! "
upper = my_string.upper()       # " HELLO, WORLD! "
title = my_string.title()       # " Hello, World! "
print(f"小写:'{lower}', 大写:'{upper}', 标题:'{title}'")

# 查找替换
index = my_string.find('World') # 查找子串位置
count = my_string.count('l')    # 统计字符出现次数
new_string = my_string.replace('World', 'Python') # 替换
print(f"索引:{index}, 计数:{count}, 替换后:'{new_string}'")

# 分割连接
words = my_string.split(',')    # [' Hello', ' World! ']
joined = ','.join(['a', 'b', 'c']) # "a,b,c"
print(f"分割:{words}, 连接:{joined}")

# 去除空白
stripped = my_string.strip()    # "Hello, World!"
left_stripped = my_string.lstrip() # "Hello, World! "
right_stripped = my_string.rstrip() # " Hello, World!"
print(f"去空白:'{stripped}', 左去空白:'{left_stripped}', 右去空白:'{right_stripped}'")

# =============================================================================
# 6. 类型转换大全
# =============================================================================

print("\n" + "="*50)
print("类型转换示例")
print("="*50)

# List → 其他类型
my_list = [1, 2, 3, 2, 4]
list_to_tuple = tuple(my_list)       # (1, 2, 3, 2, 4)
list_to_set = set(my_list)           # {1, 2, 3, 4} 去重
pairs_list = [('a', 1), ('b', 2)]
list_to_dict = dict(pairs_list)      # {'a': 1, 'b': 2}
str_list = ['a', 'b', 'c']
list_to_str = ''.join(str_list)      # "abc"
print(f"列表转元组: {list_to_tuple}")
print(f"列表转集合: {list_to_set}")
print(f"列表转字典: {list_to_dict}")
print(f"列表转字符串: {list_to_str}")

# Tuple → 其他类型
my_tuple = (1, 2, 3, 2, 4)
tuple_to_list = list(my_tuple)        # [1, 2, 3, 2, 4]
tuple_to_set = set(my_tuple)          # {1, 2, 3, 4}
pairs_tuple = (('a', 1), ('b', 2))
tuple_to_dict = dict(pairs_tuple)     # {'a': 1, 'b': 2}
str_tuple = ('a', 'b', 'c')
tuple_to_str = ''.join(str_tuple)     # "abc"
print(f"元组转列表: {tuple_to_list}")
print(f"元组转集合: {tuple_to_set}")
print(f"元组转字典: {tuple_to_dict}")
print(f"元组转字符串: {tuple_to_str}")

# Set → 其他类型
my_set = {1, 2, 3, 4}
set_to_list = list(my_set)          # [1, 2, 3, 4]（顺序可能不同）
set_to_tuple = tuple(my_set)        # (1, 2, 3, 4)（顺序可能不同）
str_set = {'a', 'b', 'c'}
set_to_str = ''.join(str_set)       # "abc"（顺序可能不同）
print(f"集合转列表: {set_to_list}")
print(f"集合转元组: {set_to_tuple}")
print(f"集合转字符串: {set_to_str}")

# Dictionary → 其他类型
my_dict = {'a': 1, 'b': 2, 'c': 3}
dict_to_keys_list = list(my_dict.keys())    # ['a', 'b', 'c']
dict_to_values_list = list(my_dict.values()) # [1, 2, 3]
dict_to_items_list = list(my_dict.items())  # [('a', 1), ('b', 2), ('c', 3)]
dict_to_keys_tuple = tuple(my_dict.keys())  # ('a', 'b', 'c')
dict_to_keys_set = set(my_dict.keys())      # {'a', 'b', 'c'}
print(f"字典键转列表: {dict_to_keys_list}")
print(f"字典值转列表: {dict_to_values_list}")
print(f"字典键值对转列表: {dict_to_items_list}")
print(f"字典键转元组: {dict_to_keys_tuple}")
print(f"字典键转集合: {dict_to_keys_set}")

# String → 其他类型
my_string = "hello world"
str_to_list = list(my_string)         # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
str_to_tuple = tuple(my_string)       # ('h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd')
str_to_set = set(my_string)           # {'h', 'e', 'l', 'o', ' ', 'w', 'r', 'd'}（去重）
str_to_word_list = my_string.split()  # ['hello', 'world']
print(f"字符串转列表: {str_to_list}")
print(f"字符串转元组: {str_to_tuple}")
print(f"字符串转集合: {str_to_set}")
print(f"字符串分割: {str_to_word_list}")

# =============================================================================
# 7. 复杂转换示例
# =============================================================================

print("\n" + "="*50)
print("复杂转换示例")
print("="*50)

# 列表的列表 → 字典的列表
list_of_lists = [['name', 'age'], ['Alice', 25], ['Bob', 30]]
keys = list_of_lists[0]
dict_list = [dict(zip(keys, values)) for values in list_of_lists[1:]]
print(f"列表的列表转字典列表: {dict_list}")

# 字典列表 → 单一字典
dict_list = [{'a': 1}, {'b': 2}, {'c': 3}]
combined_dict = {}
for d in dict_list:
    combined_dict.update(d)
print(f"字典列表合并: {combined_dict}")

# 数据清洗转换
mixed_data = ["1", "2.5", "3", "4.7", "abc"]
def safe_convert(data):
    result = []
    for item in data:
        try:
            result.append(int(item))
        except ValueError:
            try:
                result.append(float(item))
            except ValueError:
                result.append(item)
    return result

cleaned_data = safe_convert(mixed_data)
print(f"数据清洗: {cleaned_data}")

# =============================================================================
# 8. 实用技巧
# =============================================================================

print("\n" + "="*50)
print("实用技巧")
print("="*50)

# 快速去重（保持顺序）
my_list = [3, 1, 2, 1, 4, 3]
unique_ordered = list(dict.fromkeys(my_list))
print(f"去重保持顺序: {unique_ordered}")

# 扁平化嵌套列表
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in nested_list for item in sublist]
print(f"扁平化列表: {flat_list}")

# 字典键值反转
my_dict = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = {v: k for k, v in my_dict.items()}
print(f"字典键值反转: {reversed_dict}")

# 使用translate进行字符处理
text = "Hello, World!"
trans_table = str.maketrans('lo', 'LO', ' ')
result = text.translate(trans_table)
print(f"字符替换删除: {result}")

print("\n所有示例执行完成！")