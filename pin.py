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
        if keys[K_DOWN] and self.rect.y < 500 - 80:
            self.rect.y -= self.speed
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_W] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_S] and self.rect.y < 500 - 80:
            self.rect.y -= self.speed
    

game = True
finish = False
player1 = Player1('Rocket')


window = display.set_mode((700,500))
display.set_caption('Пинг-Понг')
background = transform.scale(image.load('травка.jpg'),(700,500))




while game:

    window.blit(background,(0, 0))
    display.update()