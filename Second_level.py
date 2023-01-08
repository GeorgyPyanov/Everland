from random import choice, randint
import pygame
from Tools import Background, Particle, Mouse, Sprite_Mouse_Location, Particle_2, Piano

pygame.init()
pygame.display.set_caption('Ледяной лес')
font = pygame.font.SysFont('data/shrift.ttf', 50)
all_sprites = pygame.sprite.Group()
mouse_but = pygame.sprite.Group()
piano = pygame.sprite.Group()
noty = ['sounds/do.mp3', 'sounds/re.mp3', 'sounds/mi.mp3', 'sounds/fa.mp3',
        'sounds/sol.mp3', 'sounds/ly.mp3', 'sounds/si.mp3', 'sounds/do_2.mp3']
noty_s = []
for i in range(8):
    nota = Piano(300 + 58 * i, 435, noty[i])
    piano.add(nota)
    noty_s.append(nota)
screen = pygame.display.set_mode((1024, 522))
screen_rect = (0, 0, 1024, 522)
clock = pygame.time.Clock()
pygame.key.set_repeat(200, 25)
BackGround = Background('data/snow_forest.jpg', [0, 0])
pygame_icon = pygame.image.load('data/avatar.jpeg')
pygame.display.set_icon(pygame_icon)
pygame.mixer.music.load("sounds/snowstorm.mp3")
pygame.mixer.music.play(-1)
pygame.mouse.set_visible(False)
mouse = Mouse(mouse_but)
particles = []
mouse_sprite = Sprite_Mouse_Location()
colors = [(100, 149, 237), (25, 25, 112), (218, 112, 214)]
list_pictures = ['snowflakes_1.png', 'snowflakes_2.png', 'snowflakes_3.png']


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


while True:
    screen.fill((225, 225, 225))
    events = pygame.event.get()
    screen.blit(BackGround.image, BackGround.rect)
    for event in events:
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEMOTION:
            mouse_but.update(pos[0], pos[1])
        if event.type == pygame.MOUSEBUTTONDOWN:
            create_particles(pygame.mouse.get_pos(), list_pictures)
            if event.button == 1:
                for i in piano:
                    if pygame.sprite.collide_rect(i, mouse_sprite):
                        i.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                n = 0
                for i in piano:
                    if n == 0:
                        i.update()
                    n += 1
            if event.key == pygame.K_x:
                n = 0
                for i in piano:
                    if n == 1:
                        i.update()
                    n += 1
            if event.key == pygame.K_c:
                n = 0
                for i in piano:
                    if n == 2:
                        i.update()
                    n += 1
            if event.key == pygame.K_v:
                n = 0
                for i in piano:
                    if n == 3:
                        i.update()
                    n += 1
            if event.key == pygame.K_b:
                n = 0
                for i in piano:
                    if n == 4:
                        i.update()
                    n += 1
            if event.key == pygame.K_n:
                n = 0
                for i in piano:
                    if n == 5:
                        i.update()
                    n += 1
            if event.key == pygame.K_m:
                n = 0
                for i in piano:
                    if n == 6:
                        i.update()
                    n += 1
            if event.key == pygame.K_l:
                n = 0
                for i in piano:
                    if n == 7:
                        i.update()
                    n += 1
    mouse_sprite.rect.x = pos[0]
    mouse_sprite.rect.y = pos[1]
    for x in range(randint(15, 25)):
        particle = Particle_2(pos[0], pos[1], randint(0, 20) / 10,
                              randint(-3, -1), randint(2, 5), choice(colors))
        particles.append(particle)
    piano.draw(screen)
    if pygame.mouse.get_focused():
        mouse_but.draw(screen)
        DrawPictures()
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(30)
