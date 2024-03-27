import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Moving red ball')

x = 250
y = 250
pixels = 20

running = True
while running:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y > 30:
                y -= pixels
            elif event.key == pygame.K_DOWN and y < 500 - 30:
                y += pixels
            elif event.key == pygame.K_LEFT and x > 30:
                x -= pixels
            elif event.key == pygame.K_RIGHT and x < 500 - 30:
                x += pixels
    pygame.display.update()
pygame.quit()