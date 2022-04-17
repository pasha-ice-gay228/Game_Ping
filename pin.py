from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self , player_image , player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 450 :
            self.rect.y += self.speed
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 450:
            self.rect.y += self.speed
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
    
clock = time.Clock()
FPS = 60
game = True
finish = False
player1 = Player1('Rocket.png', 25, 250, 5)
player2 = Player2('Rocket.png', 625, 250, 5)
hach = GameSprite('хачЬ.png', 325, 250, 10)


window = display.set_mode((700,500))
display.set_caption('Пинг-Понг')
background = transform.scale(image.load('травка.jpg'),(700,500))


speed_x = 4
speed_y = 4

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background,(0, 0))
    player1.reset()
    player1.update()
    player2.update()
    player2.reset()
    
    hach.rect.x += speed_x
    hach.rect.y += speed_y
    if hach.rect.y > 450:
        speed_y *= -1
    hach.reset()
    hach.update()
   
    display.update()
    clock.tick(FPS)