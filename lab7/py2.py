import pygame
import os

pygame.init()

screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption('Music Player')

font = pygame.font.Font(None, 26)

music_dir = 'music_for_pygame'
music_files = [f for f in os.listdir(music_dir) if f.endswith(('.mp3'))]
current_track = 0

pygame.mixer.init(frequency = 44100, size = -16, channels = 2, buffer = 4096)
pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))

def play_next_track():
    global current_track
    current_track = (current_track + 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))
    pygame.mixer.music.play()
def play_previous_track():
    global current_track
    current_track = (current_track - 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))
    pygame.mixer.music.play()

# Main
running = True
paused = False
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
            elif event.key == pygame.K_LEFT:
                play_next_track()
            elif event.key == pygame.K_RIGHT:
                play_previous_track()

    sample_text = font.render('Currently playing:', True, (0, 0, 0))
    music_name = font.render(music_files[current_track], True, (0, 0, 0))
    status_text = font.render('|>' if paused else '||', True, (0, 0, 0))

    screen.blit(sample_text, (20, 20))
    screen.blit(music_name, (20, 20 + sample_text.get_height() + 15))
    screen.blit(status_text, (20, 50 + sample_text.get_height() + 20))

    pygame.display.flip()
pygame.quit()