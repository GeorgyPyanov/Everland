import os
import sys
import random
import pygame


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, all_sprites, time):
        super().__init__(all_sprites)
        self.frames = []
        self.time = time
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.n = 0

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.n += 1
        if self.n == self.time:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
            self.n = 0


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Particle(pygame.sprite.Sprite):
    def __init__(self, pos, dx, dy, all_sprites, GRAVITY, screen_rect, image_name):
        super().__init__(all_sprites)
        fire = [[load_image(i) for i in image_name]]
        for scale in (20, 25, 30):
            fire.append(pygame.transform.scale(random.choice(fire[0]), (scale + 15, scale)))
        self.screen_rect = screen_rect
        self.image = random.choice(fire[1:])
        self.rect = self.image.get_rect()
        self.velocity = [dx, dy]
        self.rect.x, self.rect.y = pos
        self.gravity = GRAVITY

    def update(self):
        self.velocity[1] += self.gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if not self.rect.colliderect(self.screen_rect):
            self.kill()


class Particle_2:
    def __init__(self, x, y, x_vel, y_vel, radius, color, gravity=None):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.radius = radius
        self.color = color
        self.gravity = gravity

    def render(self, screen):
        self.x += self.x_vel
        self.y += self.y_vel
        if self.gravity:
            self.y_vel += self.gravity
        self.radius -= 0.1
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


class Sprite_Mouse_Location(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(0, 0, 1, 1)


class Mouse(pygame.sprite.Sprite):
    image = load_image("kristall.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Mouse.image
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

    def update(self, x, y):
        if pygame.mouse.get_focused():
            self.rect.x = x - 10
            self.rect.y = y - 10
