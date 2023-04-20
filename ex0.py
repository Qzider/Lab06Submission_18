import sys 
import pygame as pg
pg.init()

class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0,r=0,g=0,b=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.r = r 
        self.g = g
        self.b = b
        
    def draw(self,screen):
        pg.draw.rect(screen,(self.r, self.g, self.b),(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0,r=0,g=0,b=0):
        Rectangle.__init__(self, x, y, w, h,r,g,b)
    
    def isMouseOn(self):
        mouse_1 , mouse_2 = pg.mouse.get_pos()
        if mouse_1 >= self.x and mouse_1 <= self.x + self.w and mouse_2 >= self.y and mouse_2 <= self.y + self.h:
            return True
        else:
            return False

run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
#firstObject = Rectangle(20,20,100,100) # สร้าง Object จากคลาส Rectangle ขึ้นมา
btn = Button(20,20,100,100,255,0,0)

while(run):
    screen.fill((255, 255, 255))
    if btn.isMouseOn():
        # btn.w = 200
        # btn.h = 300
        btn.r = 192
        btn.g = 192
        btn.b = 192
        if pg.mouse.get_pressed()[0] == 1:
            btn.r = 153
            btn.g = 0
            btn.b = 153
    else:
        # btn.w = 100
        # btn.h = 100
        btn.r = 255
        btn.g = 0
        btn.b = 0
    btn.draw(screen)
    
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False