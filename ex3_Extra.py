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

class InputBox:

    def __init__(self, x, y, w, h,intt, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.intt = intt
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
    
        

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif self.intt:
                    if event.unicode.isnumeric():
                        self.text += event.unicode
                    else:
                        pass
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True,self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

COLOR_INACTIVE = pg.Color('MediumOrchid4') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('maroon3')     # ^^^
FONT = pg.font.Font(None, 32)

font = pg.font.Font('14274_Bluemoon_PixCers_v.1.1.ttf', 32) # font and fontsize
text = font.render('Firstname : ',True,(200,0,255)) # (text,is smooth?,letter color,background color)
text1 = font.render('Lastname : ',True,(200,0,255))
text2 = font.render('Ages : ',True,(200,0,255))
text3 = font.render('SUBMIT!!',True,(0,0,0))
text6 = font.render('Nickname : ',True,(200,0,255))
text7 = font.render('University : ',True,(200,0,255))
text8 = font.render('Student ID : ',True,(200,0,255))
textRect = text.get_rect() # text size

btn = Button(350,400,100,50,150,255,200)

input_box1 = InputBox(100, 100, 140, 32,False) # สร้าง InputBox1
input_box2 = InputBox(100, 200, 140, 32,False) # สร้าง InputBox2
input_boxage = InputBox(100, 300 , 140 ,32,True) # อายุ
input_boxnn = InputBox(450, 100, 140, 32,False) # ชื่อเล่นน
input_boxuni = InputBox(450, 200, 140, 32,False) # มหาวิทยาลัย
input_boxid = InputBox(450,300,140,32,True) # student id
input_boxes = [input_box1, input_box2, input_boxage,input_boxid,input_boxnn,input_boxuni] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
run = True
state =''
while run:
    screen.fill((255, 255, 255))
    screen.blit(text,(100,66))
    screen.blit(text1,(100,166))
    screen.blit(text2,(100,266))
    screen.blit(text6,(450,66))
    screen.blit(text7,(450,166))
    screen.blit(text8,(450,266))
    btn.draw(screen)
    screen.blit(text3,(357,410))
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
        
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    if btn.isMouseOn():
        if pg.mouse.get_pressed()[0] == 1:
            btn.color = [127,127,127]
            
            if input_box1.text == '':
                state = 'bababa'
                input_box1.color = [255,0,0]
            if input_box2.text == '':
                state = 'bababa'
                input_box2.color = [255,0,0]
            if input_boxage.text == '':
                state = 'bababa'
                input_boxage.color = [255,0,0]
            if input_boxnn.text == '':
                state = 'bababa'
                input_boxnn.color = [255,0,0]
            if input_boxuni.text == '':
                state = 'bababa'
                input_boxuni.color = [255,0,0]
            if input_boxid.text == '':
                state = 'bababa'
                input_boxid.color = [255,0,0]
            if input_box1.text != '' and input_box2.text != '' and input_boxage.text != '' and input_boxnn.text != ''and input_boxuni.text != ''and input_boxid.text != '':
                state = 'ojay'
            
    if state == 'ojay':
        text4 = font.render('Hello '+ str(input_box1.text) + ' ' + str(input_box2.text)+'! You are '+str(input_boxage.text)+' years old.',True,(0,0,0))
        screen.blit(text4,(100,350))
    elif state == 'bababa':
        text5 = font.render("Box is Empty! Please term info", True, (0,0,0))
        screen.blit(text5, (100, 350))
    pg.time.delay(1)
    pg.display.update()