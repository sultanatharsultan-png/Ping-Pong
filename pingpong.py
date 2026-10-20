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
speed_x = 3
speed_y = 5
clock = time.Clock()
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill((200, 255, 255))
        raket_right.update_right()
        raket_left.update_left()
        bola.rect.x += speed_x
        bola.rect.y += speed_y
        raket_right.show()
        raket_left.show()
        bola.show()
    display.update()
    clock.tick(60)