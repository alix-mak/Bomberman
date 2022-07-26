import pygame

from sprites import Player, Wall
from event import AddEnemy
from engine import Engine
from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    DEFAULT_OBJ_SIZE,
    FRAMES_PER_SECOND,
    BACKGROUND_COLOR
)


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

engine = Engine(screen=screen, clock=clock)

player = Player()

Wall.generate_walls((SCREEN_WIDTH, SCREEN_HEIGHT),
                    (DEFAULT_OBJ_SIZE, DEFAULT_OBJ_SIZE))

add_enemy = AddEnemy(2000)
engine.add_event(add_enemy)

engine.running = True

pygame.mixer.music.load("sounds/BossMain.wav")
pygame.mixer.music.play(loops=-1)

while engine.running:
    engine.events_handling()

    # Update all groups
    engine.groups_update()
    if not engine.running:
        break

    engine.screen.fill(BACKGROUND_COLOR)

    # Draw all sprites
    engine.draw_all_sprites()

    engine.draw_interface()

    pygame.display.flip()
    engine.clock.tick(FRAMES_PER_SECOND)

print("GAME OVER")
pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()
