#alt+shift+down
from turtle import*
pencolor('blue')
pensize(3)
speed('slowest')
for i in range(9):
    fd(120)
    lt(40)
    write(i, font=('calibri',25))
hideturtle()
mainloop()