#создай игру "Лабиринт"!
from pygame import *
win_x = 700
win_y = 500
window = display.set_mode((win_x,win_y))
background = transform.scale(image.load('cat-drift.gif'),(win_x,win_y))
clock = time.Clock()
game = True
display.set_caption('Мазэ')

#мьюзик
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
kick = mixer.Sound('kick.ogg')
zoloto = mixer.Sound('money.ogg')

#Персонажи
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 435:
            self.rect.y += self.speed
        if keys_pressed[K_d] and self.rect.x < 636:
            self.rect.x += self.speed
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        if self.rect.x <= 490:
            self.direction = 'right'
        elif self.rect.x >= 645:
            self.direction = 'left'

igrok = Player('hero.png',5,390,5)
kibork_ybiyca = Enemy('cyborg.png',590,300,2)
ciganskoe_zoloto = GameSprite('treasure.png',590,400,666)

#Стена
class Wall(sprite.Sprite):
    def __init__(self,color,wallx,wally,wallwidht,wallheight):
        super().__init__()
        self.color = color
        self.width = wallwidht
        self.height = wallheight
        self.image = Surface((self.width,self.height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = wallx
        self.rect.y = wally
    def draw_wall(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
wall1 = Wall((0,255,0),100,30,500,10)
wall2 = Wall((0,255,0),100,30,10,340)
wall_condition_zero = Wall((0,255,0),100,470,500,10)
wall4 = Wall((0,255,0),200,150,10,320)
wall5 = Wall((0,255,0),300,150,320,10)
wall6 = Wall((0,255,0),480,270,10,200)

finish = False
font.init()
font1 = font.SysFont('verdana',70)
win = font1.render('You WIN!',True,(0,255,0))
lose = font1.render('You LOSER!!!!',True,(255,0,0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    
    window.blit(background,(0,0))  
    if not finish:
        '''if sprite.collide_rect(igrok, wall1) or sprite.collide_rect(igrok, wall2) or sprite.collide_rect(igrok, wall_condition_zero) or sprite.collide_rect(igrok, wall4) or sprite.collide_rect(igrok, wall5) or sprite.collide_rect(igrok, wall6) or sprite.collide_rect(igrok, kibork_ybiyca): #ss
            kick.play()
        if sprite.collide_rect(igrok, ciganskoe_zoloto): #ss
            zoloto.play()'''

        kibork_ybiyca.reset()
        igrok.reset()
        wall1.draw_wall()
        wall2.draw_wall()
        wall_condition_zero.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        ciganskoe_zoloto.reset()
        kibork_ybiyca.update()
        igrok.update()
    if sprite.collide_rect(igrok, ciganskoe_zoloto): #ss
        finish = True
        window.blit(win,(200,230))
            
    if sprite.collide_rect(igrok, wall1) or sprite.collide_rect(igrok, wall2) or sprite.collide_rect(igrok, wall_condition_zero) or sprite.collide_rect(igrok, wall4) or sprite.collide_rect(igrok, wall5) or sprite.collide_rect(igrok, wall6) or sprite.collide_rect(igrok, kibork_ybiyca): #ss
        finish = True
        window.blit(lose,(130,230))
            
    display.update()
    clock.tick(60)