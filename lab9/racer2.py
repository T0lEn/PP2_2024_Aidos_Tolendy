import pygame, sys  
import random, time  
from pygame.locals import *  
import os  

pygame.init()  
FramePerSec = pygame.time.Clock()  # Создание объекта для отслеживания времени.
background = pygame.image.load("AnimatedStreet.png")  # Загрузка фонового изображения.

# Определение основных цветов.
BLACK = pygame.Color(0, 0, 0)         
WHITE = pygame.Color(255, 255, 255)   
BLUE = pygame.Color(0, 0, 255)   
RED = pygame.Color(255, 0, 0)       
GREY = pygame.Color(128, 128, 128)    

# Настройка переменных игры.
FPS = 60
SPEED = 4
WIDTH = 400
HEIGHT = 600 
SCORE = 0
COINS = 0
COINSPEED = 4

screen = pygame.display.set_mode((400, 600))  # Создание игрового экрана.
screen.fill(WHITE)  # Заполнение экрана белым цветом.
pygame.display.set_caption("IMPROVED RACE")  # Настройка заголовка окна.

# Настройка шрифтов.
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Класс вражеской машины.
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")  # Загрузка изображения врага.
        self.rect = self.image.get_rect()  # Получение прямоугольника вокруг изображения.
        self.rect.center=(random.randint(40, WIDTH-40),0)  # Начальное положение врага.

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)  # Движение врага вниз.
        if (self.rect.top > 600):  # Если враг выходит за пределы экрана.
            SCORE += 1  # Увеличение счета.
            self.rect.top = 0  # Перемещение врага вверх экрана.
            self.rect.center = (random.randint(30, 370), 0)  # Новое случайное положение врага.

# Класс игрока.
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")  # Загрузка изображения игрока.
        self.rect = self.image.get_rect()  # Получение прямоугольника вокруг изображения.
        self.rect.center = (160, 520)  # Начальное положение игрока.

    def move(self):
        pressed_keys = pygame.key.get_pressed()  # Состояние клавиш.
         
        if self.rect.left > 0:  # Проверка границы слева.
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)  # Движение влево.
        if self.rect.right < WIDTH:  # Проверка границы справа.     
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)  # Движение вправо.

# Класс монет.
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.coin_type = random.choices(["golden-coin", "silver-coin", "bronze-coin"], weights=[0.2, 0.3, 0.5])[0]  # Тип монеты.
        self.image_orig = pygame.image.load(f"{self.coin_type}.png")  # Загрузка изображения монеты.
        self.image = pygame.transform.scale(self.image_orig, (30, 30))  # Изменение размера изображения монеты.
        self.rect = self.image.get_rect()  # Получение прямоугольника вокруг изображения.
        self.rect.center = (random.randint(40, WIDTH-40), 0)  # Начальное положение монеты.
 
    def move(self):
        self.rect.move_ip(0, COINSPEED)  # Движение монеты вниз.
        if self.rect.top > HEIGHT:
            self.kill()  # Удаление монеты, если она выходит за пределы экрана.

# Создание объектов игрока и врага.
P1 = Player()
E1 = Enemy()   

# Создание групп спрайтов.
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(E1)
all_sprites.add(P1)

# Настройка таймера для увеличения скорости врагов.
INC_SPEED = pygame.USEREVENT + 1
enemy_speed_increment = 0.5
coins_for_speed_increase = 10
enemy_speed_increase_counter = 0
pygame.time.set_timer(INC_SPEED, 1000)

coins = pygame.sprite.Group()  # Группа для монет.

# Основной игровой цикл.
while True:     
    for event in pygame.event.get(): 
        if event.type == INC_SPEED:
            SPEED += 0.1  # Увеличение скорости врагов.

        if event.type == QUIT:
            pygame.quit()  # Завершение работы Pygame при закрытии окна.
            sys.exit()
    P1.update()  # Обновление позиции игрока.
    E1.move()  # Движение врага.
    screen.blit(background, (0,0))  # Отрисовка фона.
    scores = font_small.render("SCORE: " + str(SCORE), True, BLACK)  # Отображение счёта.
    screen.blit(scores, (10,10))

    # Добавление новой монеты при условии.
    if len(coins) < 1:
        if random.random() < 0.2:  
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)
    
    # Отрисовка всех спрайтов.
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    # Отображение количества монет.
    coin_text = font_small.render("Coins: " + str(COINS), True, BLACK)
    screen.blit(coin_text, (10, 40))

    # Проверка столкновений игрока с монетами.
    for coin in coins:
        if pygame.sprite.collide_rect(P1, coin):
            coin.kill()  # Удаление монеты при сборе.
            # Увеличение счетчика монет в зависимости от типа монеты.
            if coin.coin_type == "golden-coin":
                COINS += 5
            elif coin.coin_type == "silver-coin":
                COINS += 3
            elif coin.coin_type == "bronze-coin":
                COINS += 1
            pygame.mixer.Sound("8bit-coin-sound-effect.mp3").play()  # Воспроизведение звука сбора монеты.
            # Увеличение скорости врагов при достижении определенного количества монет.
            if COINS % coins_for_speed_increase == 0:
                SPEED += enemy_speed_increment
                enemy_speed_increase_counter += 1
        
    # Проверка столкновения игрока с врагами.
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound("crash.wav").play()  # Воспроизведение звука столкновения.
        time.sleep(0.5)  # Пауза перед завершением игры.
        screen.fill(RED)  # Заливка экрана красным цветом.
        screen.blit(game_over, (30,250))  # Отображение текста "Игра окончена".

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()  # Удаление всех спрайтов.
        time.sleep(2)
        pygame.quit()  # Завершение работы Pygame.
        sys.exit()    

    pygame.display.update()  # Обновление содержимого экрана.
    FramePerSec.tick(FPS)  # Контроль частоты кадров.
