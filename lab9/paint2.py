import pygame  
import math  

# Определение констант для различных типов фигур
SQUARE = 'SQUARE'
CIRCLE = 'CIRCLE'
RIGHT_TRIANGLE = 'RIGHT_TRIANGLE'
EQUILATERAL_TRIANGLE = 'EQUILATERAL_TRIANGLE'
RHOMBUS = 'RHOMBUS'

# Установка размеров экрана и панелей инструментов
dis_width = 640
dis_height = 480
icon_top_bar_height = 50
icon_right_bar_width = 50

# Определение основных цветов
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (200, 200, 200)

# Инициализация начальных значений для текущего цвета и формы
current_color = black
current_shape = SQUARE
elements_to_draw = []  # Список для хранения элементов, которые будут нарисованы

pygame.init()  # Инициализация Pygame
screen = pygame.display.set_mode((dis_width, dis_height))  # Создание экрана для отображения
clock = pygame.time.Clock()  # Создание таймера для контроля фреймрейта

def draw_ui():
    # Рисуем фон для панели инструментов и панели выбора цвета
    pygame.draw.rect(screen, gray, (0, 0, dis_width, icon_top_bar_height))
    pygame.draw.rect(screen, gray, (dis_width - icon_right_bar_width, 0, icon_right_bar_width, dis_height))
    
    # Отрисовка иконок для инструментов и цветов
    icons = [
        (10, SQUARE), (60, CIRCLE), (110, RIGHT_TRIANGLE), 
        (160, EQUILATERAL_TRIANGLE), (210, RHOMBUS)
    ]
    colors = [(dis_width - 40, 50, blue), (dis_width - 40, 90, red)]
    
    # Рисуем иконки для выбора формы
    for x, shape in icons:
        if shape == SQUARE:
            pygame.draw.rect(screen, black, (x, 10, 30, 30), 2)  # Квадрат
        elif shape == CIRCLE:
            pygame.draw.circle(screen, black, (x + 15, 25), 15, 2)  # Круг
        elif shape == RIGHT_TRIANGLE:
            pygame.draw.polygon(screen, black, [(x + 15, 40), (x + 45, 40), (x + 15, 10)], 2)  # Прямоугольный треугольник
        elif shape == EQUILATERAL_TRIANGLE:
            h = (math.sqrt(3)/2) * 50
            pygame.draw.polygon(screen, black, [(x, 40), (x + 15, 10), (x + 30, 40)], 2)  # Равносторонний треугольник
        elif shape == RHOMBUS:
            pygame.draw.polygon(screen, black, [(x + 15, 10), (x + 30, 25), (x + 15, 40), (x, 25)], 2)  # Ромб
    
    # Рисуем иконки для выбора цвета
    for x, y, color in colors:
        pygame.draw.rect(screen, color, (x, y, 30, 30))

def draw_elements():
    # Отрисовка выбранных элементов на экране
    for element in elements_to_draw:
        if element['shape'] == SQUARE:
            pygame.draw.rect(screen, element['color'], (element['x'], element['y'], 50, 50))  # Рисуем квадрат
        elif element['shape'] == CIRCLE:
            pygame.draw.circle(screen, element['color'], (element['x'], element['y']), 25)  # Рисуем круг
        elif element['shape'] == RIGHT_TRIANGLE:
            pygame.draw.polygon(screen, element['color'], [(element['x'], element['y']), (element['x'], element['y'] + 50), (element['x'] + 50, element['y'] + 50)])  # Рисуем прямоугольный треугольник
        elif element['shape'] == EQUILATERAL_TRIANGLE:
            h = (math.sqrt(3)/2) * 50
            pygame.draw.polygon(screen, element['color'], [(element['x'], element['y'] + h), (element['x'] + 25, element['y']), (element['x'] + 50, element['y'] + h)])  # Рисуем равносторонний треугольник
        elif element['shape'] == RHOMBUS:
            pygame.draw.polygon(screen, element['color'], [(element['x'] + 25, element['y']), (element['x'] + 50, element['y'] + 25), (element['x'] + 25, element['y'] + 50), (element['x'], element['y'] + 25)])  # Рисуем ромб

def handle_mouse_click(pos):
    # Обработка кликов мыши для выбора формы или цвета
    global current_shape, current_color
    if pos[1] <= icon_top_bar_height:  # Выбор фигуры
        if pos[0] < 50:
            current_shape = SQUARE
        elif 50 < pos[0] <= 100:
            current_shape = CIRCLE
        elif 100 < pos[0] <= 150:
            current_shape = RIGHT_TRIANGLE
        elif 150 < pos[0] <= 200:
            current_shape = EQUILATERAL_TRIANGLE
        elif 200 < pos[0] <= 250:
            current_shape = RHOMBUS
    elif dis_width - icon_right_bar_width <= pos[0]:  # Выбор цвета
        if 50 <= pos[1] <= 80:
            current_color = blue
        elif 90 <= pos[1] <= 120:
            current_color = red
    else:
        # Добавление элемента для рисования
        elements_to_draw.append({'shape': current_shape, 'x': pos[0] - 25, 'y': pos[1] - 25, 'color': current_color})

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Выход из программы
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handle_mouse_click(event.pos)  # Обработка клика мыши
    
    screen.fill(white)  # Очистка экрана
    draw_ui()  # Рисуем пользовательский интерфейс
    draw_elements()  # Рисуем элементы
    pygame.display.flip()  # Обновление экрана
    clock.tick(60)  # Контроль частоты обновления экрана

pygame.quit()  # Закрытие Pygame
