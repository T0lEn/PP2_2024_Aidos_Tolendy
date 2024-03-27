import pygame
import datetime

pygame.init()

screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption('Mickey Clock')

mickey = pygame.image.load('main-clock.png')
left_arm = pygame.image.load('left-hand.png')
right_arm = pygame.image.load('right-hand.png')

mickey_scaled = pygame.transform.scale(mickey, (1050, 750))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = datetime.datetime.now()

    seconds_angle = -(current_time.second / 60) * 360
    minutes_angle = -((current_time.minute + 60) / 60) * 360

    rotated_left_arm = pygame.transform.rotate(left_arm, seconds_angle)
    rotated_right_arm = pygame.transform.rotate(right_arm, minutes_angle)

    screen.fill((255, 255, 255))
    screen.blit(mickey_scaled, (-25, -30))
    screen.blit(rotated_left_arm, ((1000 - rotated_left_arm.get_width()) // 2, (700 - rotated_left_arm.get_height()) // 2))
    screen.blit(rotated_right_arm, ((1000 - rotated_right_arm.get_width()) // 2, (700 - rotated_right_arm.get_height()) // 2))

    pygame.display.flip()
pygame.quit()