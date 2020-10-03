import turtle
import time
import random
def go_up():
    print("w pressed")
    head.setheading(90)
def go_down():
    print("s pressed")
    head.setheading(270)
def go_left():
    print("d pressed")
    head.setheading(360)
def go_right():
    print("a pressed")
    head.setheading(540)    
s=turtle.Screen()  #画布
tails=[]           #设置一个数组存放尾巴

s.tracer(0)            #手动刷新屏幕

head=turtle.Turtle()   #蛇头
apple=turtle.Turtle()  #苹果
Goldenapple=turtle.Turtle()

obstacles=[]
                    
s.update()
head.shape("square")
head.color("green")
head.penup()           #提起笔移动，不绘制图形
apple.shape("circle")
apple.color("red")
apple.penup()
apple.goto(100,100)
Goldenapple.shape("circle")
Goldenapple.color("yellow")
Goldenapple.penup()
Goldenapple.goto(100,100)

s.onkeypress(go_up,"w")
s.onkeypress(go_down,"s")
s.onkeypress(go_left,"d")
s.onkeypress(go_right,"a")
s.listen()
h_x=0
h_y=0
is_tauch=False
last_tails_len = 0
zaw=False

o_x=random.randint(-300,300)
o_y=random.randint(-300,300)
for i in range(15):
    obstacle=turtle.Turtle()
    obstacle.shape("square")
    obstacle.color("black")
    obstacle.penup()
    obstacle.goto(o_x-i*20,o_y)
    obstacles.append(obstacle)


while True:
    trans_flag=random.randint(0,500)
    if trans_flag == 10:
        x= random.randint(-300,300)
        y= random.randint(-300,300)
        trans_type = random.randint(0,1)
        for i in range(15):
            if trans_type == 0:
               obstacles[i].goto(x-i*20,y)
            if trans_type == 1:
                obstacles[i].goto(x,y-i*20)

        
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
        tails.append(tail) #tail存入tails数组
        
    if head.distance(Goldenapple)<=20:
        new_x=random.randint(-300,300)
        new_y=random.randint(-300,300)
        Goldenapple.goto(new_x,new_y)
        tail=turtle.Turtle()
        tail.shape("circle")
        tail.color("green")
        tail.penup()
        tails.append(tail)
        tail2=turtle.Turtle()
        tail2.shape("circle")
        tail2.color("green")
        tail2.penup()
        tails.append(tail2) 
        tail3=turtle.Turtle()
        tail3.shape("circle")
        tail3.color("green")
        tail3.penup()
        tails.append(tail3)
        tail4=turtle.Turtle()
        tail4.shape("circle")
        tail4.color("green")
        tail4.penup()
        tails.append(tail4)
        tail5=turtle.Turtle()
        tail5.shape("circle")
        tail5.color("green")
        tail5.penup()
        tails.append(tail5)
        tail6=turtle.Turtle()
        tail6.shape("circle")
        tail6.color("green")
        tail6.penup()
        tails.append(tail6)
        tail7=turtle.Turtle()
        tail7.shape("circle")
        tail7.color("green")
        tail7.penup()
        tails.append(tail7)
        tail8=turtle.Turtle()
        tail8.shape("circle")
        tail8.color("green")
        tail8.penup()
        tails.append(tail8)
        tail9=turtle.Turtle()
        tail9.shape("circle")
        tail9.color("green")
        tail9.penup()
        tails.append(tail9)
        tail0=turtle.Turtle()
        tail0.shape("circle")
        tail0.color("green")
        tail0.penup()
        tails.append(tail0)
        
    if len(tails) > 2:    
        for i in range(2,len(tails)-2):
            if head.distance(tails[i])<=15:
                is_tauch = True
                print("game over!\n")
                break;
            
    if len(tails) > 0:    
        for i in range(0,len(obstacles)):
            if head.distance(obstacles[i])<=15:
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

