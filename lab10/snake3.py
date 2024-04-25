import pygame
import sys
import psycopg2
from random import randrange, choice
from config2 import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

# Настройки Pygame
pygame.init()
res = 800
size = 50
sc = pygame.display.set_mode([res, res])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
font_level = pygame.font.SysFont('Arial', 26, bold=True)
font_menu = pygame.font.SysFont('Arial', 30, bold=True)

# Подключение к базе данных
def connect_db():
    return psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)

def get_or_create_user(conn, username):
    cursor = conn.cursor()
    cursor.execute("SELECT id, current_level, (SELECT MAX(score) FROM user_scores WHERE user_id = users.id) FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    if result:
        return result
    else:
        cursor.execute("INSERT INTO users (username) VALUES (%s) RETURNING id, 1, 0", (username,))
        conn.commit()
        return cursor.fetchone()

def save_game(conn, user_id, score, level):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_scores (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
    conn.commit()

def main_menu():
    running = True
    username_input = ""
    while running:
        sc.fill(pygame.Color('black'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and username_input:
                    return username_input
                elif event.key == pygame.K_BACKSPACE:
                    username_input = username_input[:-1]
                else:
                    username_input += event.unicode

        block_text = font_menu.render("Enter Username and press ENTER: " + username_input, True, pygame.Color('orange'))
        sc.blit(block_text, (50, res // 2 - 50))
        pygame.display.flip()
        clock.tick(30)

def game_screen(conn, user_id, current_level, max_score):
    # Инициализация переменных игры
    x, y = randrange(0, res, size), randrange(0, res, size)
    snake = [(x, y)]
    length = 1
    score = 0 if max_score is None else max_score
    level = current_level
    dx, dy = 0, 0
    fps = 10  # скорость игры может быть адаптирована к уровню сложности
    foods = [{'pos': (randrange(0, res, size), randrange(0, res, size)), 'color': choice(['red', 'gold'])} for _ in range(3)]
    dirs = {'W': True, 'S': True, 'A': True, 'D': True}

    running = True
    while running:
        sc.fill(pygame.Color('black'))

        # Отрисовка змейки
        for i, j in snake:
            pygame.draw.rect(sc, pygame.Color('green'), (i, j, size - 2, size - 2))

        # Отрисовка еды
        for food in foods:
            pygame.draw.rect(sc, pygame.Color(food['color']), (*food['pos'], size, size))

        # Обработка событий
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
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

        # Обновление позиции змейки
        x += dx * size
        y += dy * size
        snake.append((x, y))
        snake = snake[-length:]

        # Проверка на столкновение с едой
        for food in foods[:]:
            if snake[-1] == food['pos']:
                foods.remove(food)
                foods.append({'pos': (randrange(0, res, size), randrange(0, res, size)), 'color': choice(['red', 'gold'])})
                score += 3 if food['color'] == 'gold' else 1
                length += 1
                fps += 1  # Увеличение скорости игры

        # Проверка на столкновение с границами или самим собой
        if x < 0 or x > res - size or y < 0 or y > res - size or len(snake) != len(set(snake)):
            render_end = font_end.render('GAME OVER', True, pygame.Color('orange'))
            sc.blit(render_end, (res // 2 - 200, res // 3))
            pygame.display.flip()
            pygame.time.wait(2000)  # Пауза перед закрытием
            running = False

        # Отображение счёта и уровня
        render_score = font_score.render(f'SCORE: {score}', True, pygame.Color('orange'))
        render_level = font_level.render(f'LEVEL: {level}', True, pygame.Color('orange'))
        sc.blit(render_score, (5, 5))
        sc.blit(render_level, (5, 40))

        pygame.display.flip()
        clock.tick(fps)

if __name__ == '__main__':
    conn = connect_db()
    username = main_menu()
    user_id, current_level, max_score = get_or_create_user(conn, username)
    game_screen(conn, user_id, current_level, max_score)

