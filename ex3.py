# 1 & 2. 编写一段 python 代码来演示异常终止, 演示 try，except 和 finally 语句
a = 5
b = 0
try:
    result = a / b
    print("结果是：", result)
except ZeroDivisionError:
    print("除数不能为零！")
finally:
    print("程序结束")

# 3. 编写一个 python 程序打开并将“hello world”写入一个文件
file_path = "hello_world.txt"
with open(file_path, 'w') as file:
    file.write("hello world")

# 4. 编写一个 python 程序，为现有文件编写内容“hi python programming”
file_path = "hello_world.txt"
with open(file_path, 'a') as file:
    file.write("hi python programming")