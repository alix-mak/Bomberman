import pygame


pygame.mixer.init()

SCREEN_WIDTH = 650
SCREEN_HEIGHT = 650
FRAMES_PER_SECOND = 60
BACKGROUND_COLOR = (0, 0, 0)

DEFAULT_OBJ_SIZE = 50
DEFAULT_PLAYER_HP = 100
DEFAULT_PLAYER_SPEED = 5

BOMB_TIMER = 90
PLANT_BOMB_COOLDOWN = 60
BOMB_EXPLODE_RANGE = 5
FIRE_LIFETIME = 10
COLLISION_SOUND = pygame.mixer.Sound("sounds/collision.ogg")
EXPLOSION_SOUND = pygame.mixer.Sound("sounds/explode.wav")
PLANT_BOMB_SOUND = pygame.mixer.Sound("sounds/plant.flac")
GAME_OVER_SOUND = pygame.mixer.Sound("sounds/game-over.wav")
