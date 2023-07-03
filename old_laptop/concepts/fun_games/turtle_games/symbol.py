import turtle
from turtle import *

scn = Screen()
scn.setup(width=1200, height=680)
t = turtle() # 'module' object is not callable
scn.bgcolor('gray')
t.speed(0)
colors = ['white', 'black']

for i in range(200):
    t.pencolor(colors[i])
    t.rt(i)
    t.circle(100, i)
    t.fb(i)
    t.rt(180)
    t.fb(i)

#scn.mainloop()
