#for i in range(5):
 # print(i)

#for i in range(10):
#  print(i)

#for p in range(5):
#  print(p)
  
for count in range(10):
  print(count)
  
import turtle

sak_turtle = turtle.Turtle()
sak_turtle.speed(1)

def square():
  sak_turtle.forward(100)
  sak_turtle.right(90)
  sak_turtle.forward(100)
  sak_turtle.right(90)
  sak_turtle.forward(100)
  sak_turtle.right(90)
  sak_turtle.forward(100)


for count in range(8):
  square()
