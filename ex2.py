# 1. 编写一个 lambda()函数，完成求取输入数据的两倍
double = lambda x: x * 2
a = int(input("请输入一个数字："))
print("这个数字的两倍是：", double(a))
print("-" * 20)

# 2. 编写一个 lambda()函数，实现两个输入数据的求和
add = lambda x, y: x + y
a = int(input("请输入第一个数字："))
b = int(input("请输入第二个数字："))
print("两个数字的和是：", add(a, b))
print("-" * 20)

# 3. 编写一个 filter() 函数，从给定的列表中过滤出奇数形成新的列表
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("奇数列表：", odd_numbers)
print("-" * 20)

# 4. 编写一个 map() 函数，将给定的列表中的每个元素都乘以 2
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print("乘以 2 的列表：", doubled_numbers)
print("-" * 20)

# 5. 编写一个函数对列表中所有元素求和
numbers = [1, 2, 3, 4, 5]
sum_number = lambda x: (
    0 if len(x) == 0 else
    x[0] + sum_number(x[1:])
)
print("列表中所有元素的和是：", sum_number(numbers))
print("-" * 20)