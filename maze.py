from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x,player_y,speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Grandson(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5: self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height-70: self.rect.y += self.speed
        if keys[K_LEFT] and self.rect.x > 5: self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width-70: self.rect.x += self.speed

class GrandsonCyborg(GameSprite):
    side = 'left'
    def update(self):
        if self.rect.x <= win_width-250:
            self.side = 'right'
        if self.rect.x >= win_width-80:
            self.side = 'left'

        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self,color_1,color_2,color_3,wall_x, wall_y,wall_width,wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.wall_width = wall_width
        self.wall_height = wall_height

        self.image = Surface([self.wall_width, self.wall_height])
        self.image.fill((color_1 ,color_2,color_3))

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def wall_draw(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
        draw.rect(window,(self.color_1, self.color_2, self.color_3),(self.rect.x, self.rect.y, self.wall_width,self.wall_height))

win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))
display.set_caption('гамирка лабиринт')

background = transform.scale(image.load('background.jpg'), (win_width,win_height))

pacman = Grandson('hero.png', 5,430,4)
cyborg = GrandsonCyborg('cyborg.png',win_width-80,280,2)
treasure = GameSprite('treasure.png', win_width-120, win_height-80,0)
w1 = Wall(0,0,0, 100,20 , 450,10)
w2 = Wall(0,0,0, 100,480, 350,10)
w3 = Wall(0,0,0, 100,20 , 10,370)
w4 = Wall(0,0,0, 200,110, 10,370)
w5 = Wall(0,0,0, 300,20 , 10,370)
w6 = Wall(0,0,0, 440,100, 10,380)
w7 = Wall(0,0,0, 390,100, 50,10)
w8 = Wall(0,0,0, 390,280, 50,10)
w9 = Wall(0,0,0, 310,190, 50,10)
w10 = Wall(0,0,0, 310,380, 50,10)
w11= Wall(0,0,0, 550,20, 10,250)
game = True
finish = False
FPS = 60
clock = time.Clock()

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

font.init()
font = font.SysFont('Arial', 70)
win = font.render('ТЫ ПОБЕДИЛ!', True, (255,215,0))
lose = font.render('ТЫ ПРОИГРАЛ!', True, (180,215,0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0,0))
        pacman.reset()
        cyborg.reset()
        treasure.reset()
        w1.wall_draw()
        w2.wall_draw()
        w3.wall_draw()
        w4.wall_draw()
        w5.wall_draw()
        w6.wall_draw()
        w7.wall_draw()
        w8.wall_draw()
        w9.wall_draw()
        w10.wall_draw()
        w11.wall_draw()

        if (sprite.collide_rect(pacman,cyborg) or
        sprite.collide_rect(pacman, w1) or
        sprite.collide_rect(pacman, w2) or
        sprite.collide_rect(pacman, w3) or
        sprite.collide_rect(pacman, w4) or
        sprite.collide_rect(pacman, w5) or
        sprite.collide_rect(pacman, w6) or
        sprite.collide_rect(pacman, w7) or
        sprite.collide_rect(pacman, w8) or
        sprite.collide_rect(pacman, w9) or
        sprite.collide_rect(pacman, w10) or
        sprite.collide_rect(pacman, w11)):
            finish = True
            window.blit(lose, (170,200))
            kick.play()

        if sprite.collide_rect(pacman,treasure):
            finish = True
            window.blit(win, (180,200))
            money.play()

        cyborg.update()
        pacman.update()

        display.update()
        clock.tick(FPS)