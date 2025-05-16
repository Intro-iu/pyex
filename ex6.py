import turtle
# 1. 编写一个 python 代码来设置背景颜色和图片，并使用 turtle 模块画一个圆圈
t = turtle.Turtle()
t.circle(50)
s = turtle.Screen()
s.bgcolor("white")
s.bgpic("1.jpg")
turtle.done()

# 2. 写一个 python 代码来设置背景颜色和图片，然后画一个正方形并填充颜色使用乌龟模块
t = turtle.Turtle()
t.fillcolor("red")
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()
s = turtle.Screen()
s.bgcolor("white")
turtle.done()

# 3. 编写 python 程序画一对交心圆表示交集韦恩图
t = turtle.Turtle()
t.color("red")
t.circle(50)
t.penup()
t.goto(80, 0)
t.pendown()
t.color("green")
t.circle(50)
s = turtle.Screen()
s.bgcolor("white")
turtle.done()