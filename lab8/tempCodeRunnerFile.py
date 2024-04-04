import pygame

SQUARE = 'SQUARE'
CIRCLE = 'CIRCLE'
TRIANGLE = 'TRIANGLE'

dis_width = 640
dis_height = 480
main_screen_size = (dis_width, dis_height)
elements_to_draw = []

icon_top_bar_height = 50
icon_top_bar_width = 50
icon_rectangle_start_x = 0
icon_rectangle_end_x = 50
icon_circle_start_x = 50
icon_circle_end_x = 100

icon_red_color_start_y = 50
icon_red_color_end_y = 100
icon_blue_color_start_y = 100
icon_blue_color_end_y = 150
icon_color_shape_width = 40
icon_color_shape_height = 30
icon_orange_color_start_y = 150
icon_orange_color_end_y = 200

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
orange = (255, 165, 0)

top_tab_color = (100, 100, 100)
right_tab_color = (80, 80, 80)


def draw_all_shapes(screen):
  for element in elements_to_draw:
    if element['shape'] == SQUARE:
      pygame.draw.rect(screen, element['color'],
                       [element['x'], element['y'], 50, 50])
    elif element['shape'] == CIRCLE:
      pygame.draw.circle(screen, element['color'],
                         (element['x'], element['y']), element['radius'])
    elif element['shape'] == TRIANGLE:
      # pygame.draw.polygon(screen, element['color'],(element['x'], element['y']), element['radius'])
      pass


def add_element_rectangle(x, y, color):
  elements_to_draw.append({'shape': SQUARE, 'x': x, 'y': y, 'color': color})


def add_element_circle(x, y, color, radius):
  elements_to_draw.append({
      'shape': CIRCLE,
      'x': x,
      'y': y,
      'color': color,
      'radius': radius
  })


def add_element_triangle(x, y, color):
  vertices = [(x, y), (x - 25, y + 50), (x + 25, y + 50)]
  elements_to_draw.append[{'shape': TRIANGLE, 'vertices': vertices, 'color': color}]


def draw_main_icons(screen):
  # tabs
  pygame.draw.rect(screen, top_tab_color, (0, 0, dis_width, 40))
  pygame.draw.rect(screen, right_tab_color,
                   (dis_width - 80, 0, 80, dis_height))
  pygame.draw.rect(screen, white, (icon_rectangle_start_x + 5, 5, 40, 30))
  pygame.draw.rect(screen, white, (icon_circle_start_x + 5, 5, 40, 30))
  pygame.draw.circle(screen, (128, 0, 128), (icon_circle_start_x + 25, 20), 10)
  # colors
  pygame.draw.rect(screen, red,
                   (dis_width - 70, icon_red_color_start_y, icon_color_shape_width, icon_color_shape_height))
  pygame.draw.rect(screen, blue,
                   (dis_width - 70, icon_blue_color_start_y, icon_color_shape_width, icon_color_shape_height))
  pygame.draw.rect(screen, orange, (dis_width - 70, icon_orange_color_start_y, icon_color_shape_width, icon_color_shape_height))


def main():
  pygame.init()
  screen = pygame.display.set_mode(main_screen_size)
  clock = pygame.time.Clock()

  x = 0
  y = 0
  mode = 'blue'
  points = []
  is_rectangle_drawer = False
  is_circle_drawer = False

  color = black

  position = (0, 0)

  while True:
    pressed = pygame.key.get_pressed()
    alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
    ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w and ctrl_held:
          return
        if event.key == pygame.K_F4 and alt_held:
          return
        if event.key == pygame.K_ESCAPE:
          return

      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          if position[0] <= icon_rectangle_end_x and position[
              0] > 0 and position[1] < icon_top_bar_height:
            is_rectangle_drawer = not is_rectangle_drawer
            is_circle_drawer = False
            print('is_rectangle_drawer = True')
          elif position[0] <= icon_circle_end_x and position[
              0] > icon_circle_start_x and position[1] < icon_top_bar_height:
            is_circle_drawer = not is_circle_drawer
            is_rectangle_drawer = False
            print('is_circle_drawer = True')
          elif position[0] >= dis_width - 70 and position[0] < dis_width - 70 + icon_color_shape_width and position[1] > icon_red_color_start_y and position[1] < icon_red_color_end_y:
            color = red
            print('color = color')
          elif is_rectangle_drawer:
            add_element_rectangle(position[0], position[1], color)
          elif is_circle_drawer:
            add_element_circle(position[0], position[1], color, 20)
          elif element['shape'] == TRIANGLE:
            pygame.draw.polygon(screen, element['color'], element['vertices'])

      if event.type == pygame.MOUSEMOTION:
        position = event.pos
        print(position)
        #points = points + [position]
        #points = points[-256:]

    screen.fill((255, 255, 255))

    draw_all_shapes(screen)
    draw_main_icons(screen)

    # draw all points
    i = 0
    while i < len(points) - 1:
      drawLineBetween(screen, i, points[i], points[i + 1], 15, mode)
      i += 1

    pygame.display.flip()

    clock.tick(60)


def drawLineBetween(screen, index, start, end, width, color_mode):
  c1 = max(0, min(255, 2 * index - 256))
  c2 = max(0, min(255, 2 * index))

  if color_mode == 'blue':
    color = (c1, c1, c2)
  elif color_mode == 'red':
    color = (c2, c1, c1)
  elif color_mode == 'green':
    color = (c1, c2, c1)

  dx = start[0] - end[0]
  dy = start[1] - end[1]
  iterations = max(abs(dx), abs(dy))

  for i in range(iterations):
    progress = 1.0 * i / iterations
    aprogress = 1 - progress
    x = int(aprogress * start[0] + progress * end[0])
    y = int(aprogress * start[1] + progress * end[1])
    pygame.draw.circle(screen, color, (x, y), width)


main()
