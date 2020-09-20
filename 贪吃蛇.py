import turtle
import time
import random
def go_up():
    print("W pressed")
    head.setheading(90)
def go_down():
    print("S pressed")
    head.setheading(270)
def go_left():
    print("D pressed")
    head.setheading(360)
def go_right():
    print("A pressed")
    head.setheading(540)    
s=turtle.Screen()  #画布
tails=[]           #设置一个数组存放尾巴


s.tracer(0)            #手动刷新屏幕

head=turtle.Turtle()   #蛇头
apple=turtle.Turtle()  #苹果

s.update()
head.shape("square")
head.color("green")
head.penup()           #提起笔移动，不绘制图形
apple.shape("circle")
apple.color("red")
apple.penup()
apple.goto(100,100)

s.onkeypress(go_up,"W")
s.onkeypress(go_down,"S")
s.onkeypress(go_left,"D")
s.onkeypress(go_right,"A")
s.listen()
h_x=0
h_y=0
is_tauch=False
while True:
    if len(tails)>0:
        h_x=head.xcor()
        h_y=head.ycor()        #返回上一个坐标值（cor）
        tails[0].goto(h_x,h_y)
    for i in range(len(tails)-1,0,-1):   #获取每次尾巴长度，每次减一
        last_tail=tails[i-1]
        this_tail=tails[i]
        this_tail.goto(last_tail.xcor(),last_tail.ycor())
    head.forward(15)
    if head.distance(apple)<=20:
        new_x=random.randint(-300,300)
        new_y=random.randint(-300,300)
        apple.goto(new_x,new_y)
        tail=turtle.Turtle()
        tail.shape("circle")
        tail.color("green")
        tail.penup()
        tails.append(tail)     #tail存入tails数组
    if len(tails) > 2:    
        for i in range(2,len(tails)-2):
            if head.distance(tails[i])<=10:
                is_tauch = True
                print("game over!\n")
                break;
    if is_tauch == True:
        break;
        
    time.sleep(0.1)
    s.update()
    
s.mainloop()


    
       

import pygame,sys
from pygame.locals import *
pygame.init() #初始化pygame模块
DISPLAYSURF = pygame.display.set_mode((400,300)) #长400，宽300
pygame.display.set_caption('GAME OVER')
BLACK = (0,0,0)
GREEN = (0,255,0)
BLUE = (0,0,128)
 
fontObj = pygame.font.Font('freesansbold.ttf',32)
textSurfaceObj = fontObj.render('GAME OVER',True,GREEN,BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center=(200,150)
 
while True:
	DISPLAYSURF.fill(BLACK)
	DISPLAYSURF.blit(textSurfaceObj,textRectObj)
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()

