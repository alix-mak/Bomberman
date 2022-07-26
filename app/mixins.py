import pygame

from engine import Engine


class EngineMixin:
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.engine = Engine()


class MovingMixin:
    def move_collision_out(self, x_speed, y_speed):
        is_on_bomb = self.is_on_bomb if hasattr(self, "is_on_bomb") else False
        is_on_rock = self.is_on_rock if hasattr(self, "is_on_rock") else False
        if (pygame.sprite.spritecollideany(
                self, self.engine.groups["rocks"]
        ) and not is_on_rock) or pygame.sprite.spritecollideany(
            self, self.engine.groups["walls"]
        ) or pygame.sprite.spritecollideany(
            self, self.engine.groups["bombs"]
        ) and not is_on_bomb:
            self.rect.move_ip(-x_speed, -y_speed)
