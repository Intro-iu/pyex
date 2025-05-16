# 1.编写一段程序完成两个输入数字的相加
a = int(input("请输入第一个数字："))
b = int(input("请输入第二个数字："))
print("两个数字的和为：", a + b)

print("-" * 20)

# 2.编写一段程序输入的数字是正数还是负数
num = float(input("请输入一个数字："))
if num > 0:
    print("这个数字是正数")
elif num < 0:
    print("这个数字是负数")
else:
    print("这个数字是零")

print("-" * 20)

# 3. 编写程序寻找三个数字中的最大值
a = float(input("请输入第一个数字："))
b = float(input("请输入第二个数字："))
c = float(input("请输入第三个数字："))
max_num = max(a, b, c)