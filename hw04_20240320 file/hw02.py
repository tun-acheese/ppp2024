#반복문을 이용해 삼각형 그리기
import turtle

t=turtle.Turtle()

for i in range(3):
    t.forward(100)
    t.left(120)

imput()

#반복문을 이용해 별 그리기
for i in range(1,6):
    print(" " * (5 - i) + "*" * (2*i-1))
