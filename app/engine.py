import pygame

from collections import defaultdict

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

from config import SCREEN_WIDTH


def singleton(class_):
    _instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in _instances:
            _instances[class_] = class_(*args, **kwargs)
        return _instances[class_]
    return get_instance


@singleton
class Engine:
    def __init__(self, screen, clock):
        self.running = True
        self.screen = screen
        self.clock = clock

        self.score = 0

        self.groups = defaultdict(pygame.sprite.Group)
        self.all_sprites = pygame.sprite.Group()
        self.events = dict()

    def add_event(self, event):
        self.events[event.event_no] = event

    def events_handling(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False

            # Did user click quit button?
            elif event.type == QUIT:
                self.running = False

            elif event.type in self.events:
                self.events[event.type].action()

    def add_to_group(self, sprite, group):
        self.groups[group].add(sprite)
        self.all_sprites.add(sprite)

    def groups_update(self):
        groups = list(self.groups.values())
        for group in groups:
            group.update()

    def draw_all_sprites(self):
        for sprite in self.all_sprites:
            self.screen.blit(sprite.surf, sprite.rect)

    def draw_interface(self):
        font = pygame.font.SysFont("comicsans", 15, True)
        text = font.render("Score: " + str(self.score), True, (255, 0, 0))
        self.screen.blit(text, (10, 10))

        player = self.groups["player"].sprites()[0]
        text_health = font.render("Health: " + str(player.get_health()),
                                  True, (0, 255, 0))
        text_speed = font.render("Speed: " + str(player.get_speed()),
                                 True, (0, 255, 0))

        self.screen.blit(text_health,
                         (SCREEN_WIDTH - text_health.get_width() - 10, 10))
        self.screen.blit(text_speed,
                         (SCREEN_WIDTH - text_speed.get_width() - 10, 30))
