from pygame import*


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, Width,Height):
        super().__init__()#We create super class
        self.image = transform.scale(image.load(player_image), (50, 50))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.width = Width
        self.height = Height

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite): 
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.x < 650:
            self.rect.x += self.speed
       
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 450:
            self.rect.y += self.speed

font.init()
Width = 700
Height = 500
Screen = display.set_mode((Width, Height))
Screen.fill((124,57,2))
#Fonts
font1 = font.Font(None, 72)
lose_text_LEFT = font1.render("Left lose", True, (255,0,255))
lose_text_RIGHT = font1.render("Left lose", True, (255,0, 255))

game = True
finish = False

platform_left = Player("platform.png", 10, 250, 10, 35, 110) 
platform_right = Player("platform.png", 690, 250, 10, 35, 110 )

ball = GameSprite('ball.png', 350, 255, 10, 50, 50)
clock = time.Clock()
#Classes

speed_x = 3
speed_y = 3
while game:
    for i in event_get():
        if i.type == QUIT:
            game = False

    if finish != True:
        Screen.fill((255,255,255))
        platform_left.update_l()
        platform_right.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(platform_left, ball) or sprite.collide_rect(platform_right, ball):
            speed_y *= -1 
            speed_x *= -1
        if ball.rect.y <= 0 or ball.rect.y >450:
            speed_y *= -1

        if ball.rect.x <= 0:
            finish = True
            Screen.blit(lose_text_LEFT,(300, 250))
        if ball.rect.x >= 700:
            finish = True
            Screen.blit(lose_text_RIGHT,(300,250))
        platform_left.reset()
        platform_right.reset()
#Display update

    pygame.display.update()
    clock.tick(60)