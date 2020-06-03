#AutoTraceDraw.py
import turtle as t
t.title('自动轨迹绘制')
t.setup(800,600,0,0)
t.pencolor("red")
t.pensize(5)
#数据读取
detals = []
f = open('data.txt')
for line in f:
    l = line.replace("\n",'')
    detals.append(list(map(eval,line.split(','))))
print(detals)
f.close()
#自动绘制
for i in range(len(detals)):
    t.pencolor(detals[i][3],detals[i][4],detals[i][5])
    t.fd(detals[i][0])
    if detals[i][1]:
        t.right(detals[i][2])
    else:
        t.left(detals[i][2])
t.hideturtle()
t.done()