import pygame  
from random import randrange, choice  

res = 800  # Размер игрового поля.
size = 50  # Размер одного блока (ячейки) игры.
x, y = randrange(0, res, size), randrange(0, res, size)  # Начальное положение змейки на игровом поле.
apple = randrange(0, res, size), randrange(0, res, size)  # Начальное положение яблока.
foods = [{'pos': (randrange(0, res, size), randrange(0, res, size)), 'time': pygame.time.get_ticks(), 'color': choice(['red', 'gold'])} for _ in range(3)]  # Список еды с их позициями, временем появления и цветом.
dirs = {'W': True, 'S': True, 'A': True, 'D': True}  # Допустимые направления движения змейки.
length = 1  # Начальная длина змейки.
snake = [(x, y)]  # Список сегментов змейки.
score = 0  # Начальный счет.
dx, dy = 0, 0  # Начальное направление движения змейки.
fps = 8  # Начальная скорость игры (количество кадров в секунду).

pygame.init()  # Инициализация библиотеки pygame.
sc = pygame.display.set_mode([res, res])  # Создание окна для игры.
clock = pygame.time.Clock()  # Создание таймера для контроля времени.
font_score = pygame.font.SysFont('Arial', 26, bold=True)  # Шрифт для отображения счета.
font_end = pygame.font.SysFont('Arial', 66, bold=True)  # Шрифт для отображения сообщения о конце игры.

def spawn_food():
    # Функция для создания новой еды в случайном месте.
    color = choice(['red', 'gold'])  # Выбор цвета еды.
    return {'pos': (randrange(0, res, size), randrange(0, res, size)), 'time': pygame.time.get_ticks(), 'color': color}

while True:
    sc.fill(pygame.Color('black'))  # Закрашивание экрана в черный цвет.
    # Отрисовка змейки.
    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, size - 2, size - 2))) for i, j in snake]
    
    # Обновление и отрисовка еды.
    current_time = pygame.time.get_ticks()
    foods = [food for food in foods if current_time - food['time'] <= 5000]  # Еда исчезает через 5 секунд.
    for food in foods:
        pygame.draw.rect(sc, pygame.Color(food['color']), (*food['pos'], size, size))
    if len(foods) < 3:  # Поддержание на поле трех единиц еды.
        foods.append(spawn_food())

    # Отображение счета.
    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    sc.blit(render_score, (5, 5))
    
    # Движение змейки.
    x += dx * size
    y += dy * size
    snake.append((x, y))
    snake = snake[-length:]

    # Поедание еды змейкой.
    for food in foods:
        if snake[-1] == food['pos']:
            if food['color'] == 'red':
                score += 1
            elif food['color'] == 'gold':  # За золотую еду дают больше очков.
                score += 3
            length += 1
            fps += 1  # Увеличение скорости игры.
            foods.remove(food)
            foods.append(spawn_food())

    # Условия окончания игры (столкновение с краем экрана или с собственным телом).
    if x < 0 or x > res - size or y < 0 or y > res - size or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
            sc.blit(render_end, (res // 2 - 200, res // 3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    pygame.display.flip()  # Обновление содержимого всего экрана.
    clock.tick(fps)  # Контроль скорости обновления экрана.

    # Управление змейкой.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}
