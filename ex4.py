# 1
# 创建列表以列表 list1 = ["life", "is", "short"] 和 list2 = ["You", "need", "python"]，
# 并完成以下任务:
# 输出 list1 中的第一个元素 life 及其索引（下标）。
# 在 list1 后面增加一个”!”

list1 = ["life", "is", "short"]
list2 = ["You", "need", "python"]
print(list1[0], 0)
list1.append("!")
print(list1)

# 2. 编写程序,将列表 s=[9,7,8,3,2,1,5,6]中的偶数变成它的平方,奇数保持不变
s = [9,7,8,3,2,1,5,6]
s = [x ** 2 if x % 2 == 0 else x for x in s]
print(s)

# 3. 编写一个长度至少为 5 的字典，其中姓名为键，性别为值；请编写一个程序,删除性别为男的员工信息
female = {"Alex", "Anna", "Carol", "Jassie", "Lily"}
male = {"George", "John", "Lee", "Victor"}
d1 = {x: "female" for x in female}
d2 = {x: "male" for x in male}
d = d1|d2
print(d)

d = {k: v for k, v in d.items() if v != "male"}
print(d)

# 4. 创建 2 个集合 A = {1,2,3,4,5},B = {1,2,6,7,9},分别计算两个集合的交集并集、补集和差集
A = {1,2,3,4,5}
B = {1,2,6,7,9}
print("A: ", A)
print("B: ", B)
print("交集: ", A & B)
print("并集: ", A | B)
print("补集: ", A ^ B)
print("差集: ", A - B)