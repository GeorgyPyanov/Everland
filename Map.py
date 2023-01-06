from random import random, randint, choice
import pygame
from Tools import load_image, Particle, Particle_2, Sprite_Mouse_Location, AnimatedSprite, Mouse

pygame.init()
pygame.display.set_caption('Карта')
size = width, height = 700, 600
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
screen_rect = (0, 0, width, height)
running = True
all_sprites = pygame.sprite.Group()
mouse_but = pygame.sprite.Group()
clock = pygame.time.Clock()
snow_list = []
pygame.mixer.music.load("sounds/snow.mp3")
pygame_icon = pygame.image.load('data/avatar.jpeg')
pygame.display.set_icon(pygame_icon)
sprite = pygame.sprite.Sprite()
sprite.image = load_image("name_small.png")
sprite.rect = sprite.image.get_rect()
sprite.rect.x = -90
sprite.rect.y = -60
all_sprites.add(sprite)
particles = []
colors = [(0, 0, 255), (255, 255, 255)]
sprite_island = pygame.sprite.Sprite()
one = pygame.sprite.Sprite()
two = pygame.sprite.Sprite()
three = pygame.sprite.Sprite()
four = pygame.sprite.Sprite()
sprite_island.image = load_image("island.png")
sprite_island.rect = sprite_island.image.get_rect()
sprite_island.rect.x = -100
sprite_island.rect.y = 50
all_sprites.add(sprite_island)
one.image = load_image("one.png")
one.rect = one.image.get_rect()
one.rect.x = 150
one.rect.y = 150
mouse_sprite = Sprite_Mouse_Location()
pygame.mixer.music.load("sounds/map.mp3")
pygame.mixer.music.play(-1)
list_pictures = ['snowflakes_1.png', 'snowflakes_2.png', 'snowflakes_3.png']
effect = AnimatedSprite(load_image("fire_effect_20.png"), 9, 1, 155.5, 360, all_sprites, 2)
effect.rect.x = 0
effect.rect.y = 300
pygame.mouse.set_visible(False)
mouse = Mouse(mouse_but)


def create_particles(position, list_pictures_0):
    particle_count = 20
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle((position[0] - 10, position[1]), choice(numbers), choice(numbers), all_sprites, 0.5, screen_rect,
                 list_pictures_0)


def DrawPictures():
    for i in particles:
        i.render(screen)
        if i.radius <= 0:
            particles.remove(i)


while running:
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            create_particles(pygame.mouse.get_pos(), list_pictures)
        if event.type == pygame.MOUSEMOTION:
            mouse_but.update(pos[0], pos[1])
            if pygame.sprite.collide_rect(sprite_island, mouse_sprite):
                sprite_island.image = load_image("island_on.png")
                colors = [(1, 1, 1), (155, 155, 155)]
                list_pictures = ['fire.png', 'fire_2.png', 'fire_3.png']
            elif pygame.sprite.collide_rect(effect, mouse_sprite):
                colors = [(255, 0, 0), (255, 69, 0)]
            else:
                sprite_island.image = load_image("island.png")
                colors = [(0, 0, 255), (255, 255, 255)]
                list_pictures = ['snowflakes_1.png', 'snowflakes_2.png', 'snowflakes_3.png']
    mouse_sprite.rect.x = pos[0]
    mouse_sprite.rect.y = pos[1]
    for x in range(randint(15, 25)):
        particle = Particle_2(pos[0], pos[1], randint(0, 20) / 10,
                              randint(-3, -1), randint(2, 5), choice(colors))
        particles.append(particle)
    screen.fill((0, 0, 0))
    DrawPictures()
    all_sprites.update()
    all_sprites.draw(screen)
    if pygame.mouse.get_focused():
        mouse_but.draw(screen)
    else:
        colors = [(0, 0, 0)]
    pygame.display.flip()
    clock.tick(40)

pygame.quit()