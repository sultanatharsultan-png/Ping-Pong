#Create your own shooter

from pygame import *
class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width,height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Racket(Gamesprite):
    def update_right(self):
        keys = key.get_pressed()
        if keys [K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_left(self):
        keys = key.get_pressed()
        if keys [K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

win_height = 500
win_width = 600
window = display.set_mode((win_width, win_height))
window.fill((200, 255, 255))
raket_right = Racket('racket.png', 520, 200, 4, 50, 150)
raket_left = Racket('racket.png', 30, 200, 4, 50, 150)
bola = Gamesprite('tenis_ball.png', 200, 200, 4, 50, 50)
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE!', True, (180, 0, 0))
speed_x = 3
speed_y = 5
clock = time.Clock()
game = True
finish = False
speed_bola_x = 3
speed_bola_y = 3
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill((200, 255, 255))
        raket_right.update_right()
        raket_left.update_left()
        raket_right.show()
        raket_left.show()
        if bola.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
        if bola.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
        if bola.rect.y > win_height-50 or bola.rect.y < 0:
            speed_bola_y *= -1
        if sprite.collide_rect(raket_right, bola) or sprite.collide_rect(raket_left, bola):
            speed_bola_x *= -1
        bola.rect.x += speed_bola_x
        bola.rect.y += speed_bola_y
        bola.show()
    display.update()
    clock.tick(60)                  