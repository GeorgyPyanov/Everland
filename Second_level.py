from random import choice, randint
import pygame
from Tools import Background, Particle, Mouse, Sprite_Mouse_Location, Particle_2, Piano, load_image

pygame.init()
pygame.display.set_caption('Ледяной лес')
font = pygame.font.SysFont('data/shrift.ttf', 50)
all_sprites = pygame.sprite.Group()
mouse_but = pygame.sprite.Group()
piano = pygame.sprite.Group()
lives = pygame.sprite.Group()
noty = ['sounds/do.mp3', 'sounds/re.mp3', 'sounds/mi.mp3', 'sounds/fa.mp3',
        'sounds/sol.mp3', 'sounds/ly.mp3', 'sounds/si.mp3', 'sounds/do_2.mp3']
noty_s = []
ha = 0
for i in range(8):
    nota = Piano(300 + 58 * i, 435, noty[i])
    piano.add(nota)
    noty_s.append(nota)
screen = pygame.display.set_mode((1024, 522))
screen_rect = (0, 0, 1024, 522)
clock = pygame.time.Clock()
pygame.key.set_repeat(200, 25)
BackGround = Background('data/snow_forest_1.jpg', [0, 0])
pygame_icon = pygame.image.load('data/avatar.jpeg')
pygame.display.set_icon(pygame_icon)
pygame.mixer.music.load("sounds/snowstorm.mp3")
pygame.mixer.music.play(-1)
pygame.mouse.set_visible(False)
mouse = Mouse(mouse_but)
particles = []
mouse_sprite = Sprite_Mouse_Location()
colors = [(25, 116, 210), (72, 61, 139), (18, 47, 170)]
list_pictures = ['snowflakes_1.png', 'snowflakes_2.png', 'snowflakes_3.png']
k = -1
f = open("files/piano.txt", encoding="utf8")
level = f.readline().rstrip()
f.close()
lev = 0
progress = 0
sprite = pygame.sprite.Sprite()
sprite.image = load_image("snow_qeen_1.png")
sprite.rect = sprite.image.get_rect()
sprite.rect.x = 450
sprite.rect.y = 70
all_sprites.add(sprite)
for i in range(3):
    sprite1 = pygame.sprite.Sprite()
    sprite1.image = load_image("snowflakes_4.png")
    sprite1.rect = sprite1.image.get_rect()
    sprite1.rect.x = 800 + i * 58
    sprite1.rect.y = 10
    lives.add(sprite1)
particles1 = []
h = 0
yt = 200
lose = 0
gaga = True
dance = 255


def create_particles(position, list_pictures_0):
    particle_count = 20
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle((position[0] - 10, position[1]), choice(numbers), choice(numbers), all_sprites, 0.5, screen_rect,
                 list_pictures_0)


def update_on_an():
    n = 0
    for i in piano:
        if n == k:
            i.update_an()
        else:
            i.update_on()
        n += 1


def DrawPictures():
    for i in particles:
        i.render(screen)
        if i.radius <= 0:
            particles.remove(i)


def Draw_person():
    for i in particles1:
        i.render(screen)
        if i.radius <= 0:
            particles1.remove(i)


def optimization(k0):
    n = 0
    k = k0
    for i in piano:
        if n == k:
            i.update()
        else:
            i.update_on()
        n += 1


while True:
    we = False
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
            if event.button == 1 and h == 0:
                n = 0
                for i in piano:
                    if pygame.sprite.collide_rect(i, mouse_sprite):
                        we = True
                        k = n
                        i.update()
                    else:
                        i.update_on()
                    n += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z and h == 0:
                optimization(0)
                we = True
            if event.key == pygame.K_x and h == 0:
                optimization(1)
                we = True
            if event.key == pygame.K_c and h == 0:
                optimization(2)
                we = True
            if event.key == pygame.K_v and h == 0:
                optimization(3)
                we = True
            if event.key == pygame.K_b and h == 0:
                optimization(4)
                we = True
            if event.key == pygame.K_n and h == 0:
                optimization(5)
                we = True
            if event.key == pygame.K_m and h == 0:
                optimization(6)
                we = True
            if event.key == pygame.K_l and h == 0:
                optimization(7)
                we = True
            if event.key == pygame.K_LEFT and h == 0:
                we = False
                if k > 0:
                    k -= 1
                else:
                    k = 7
                update_on_an()
            if event.key == pygame.K_RIGHT and h == 0:
                we = False
                if k != 7:
                    k += 1
                else:
                    k = 0
                update_on_an()
            if event.key == pygame.K_SPACE and h == 0:
                we = True
                n = 0
                for i in piano:
                    if n == k:
                        i.update()
                    else:
                        i.update_on()
                    n += 1
    mouse_sprite.rect.x = pos[0]
    mouse_sprite.rect.y = pos[1]
    for x in range(randint(15, 25)):
        if gaga:
            particle = Particle_2(pos[0], pos[1], randint(0, 20) / 10,
                                  randint(-3, -1), randint(2, 5), choice(colors))
            particle1 = Particle_2(480, 300, randint(-20 - h, 0 + h) / 10,
                                   randint(1 - h, 3 + h), randint(2, 5 + h // 100 * 3), choice(colors), -1)
            particle2 = Particle_2(590, 300, randint(0 - h, 20 + h) / 10,
                                   randint(1 - h, 3 + h), randint(2, 5 + h // 100 * 3), choice(colors), -1)
            particles.append(particle)
            particles1.append(particle1)
            particles1.append(particle2)
        else:
            for i in range(20):
                particle = Particle_2(randint(0, 1000), randint(0, 500), randint(0, 20) / 10,
                                      randint(-3, -1), randint(2, 5), choice(colors))
            particles1.append(particle)
    n = 0
    if int(level[lev]) != k and we and h == 0 and gaga:
        lose += 1
        if lose < 3:
            lev = 0
            h += 1
            yt = 200
            for i in lives:
                lives.remove(i)
                break
            pygame.mixer.Sound('sounds/bura.mp3').play()
            if progress != 0:
                progress -= 1
                if progress == 0:
                    ha = 0
                elif progress == 1:
                    ha = 1
        else:
            lev = 0
            h += 1
            yt = 200000000
            for i in lives:
                lives.remove(i)
                break
            pygame.mixer.music.load('sounds/bura_2.mp3')
            pygame.mixer.music.play(-1)
            progress = 0
    if 0 < h <= yt:
        h += 1
    elif h == yt + 1:
        h = 0
    if int(level[lev]) != k and h == 0 and gaga:
        for i in piano:
            if n == int(level[lev]):
                i.update_0()
            n += 1
    if int(level[lev]) == k and we and h == 0 and gaga:
        lev += 1
    if lev == len(level) and h == 0 and gaga:
        lev = 0
        progress += 1
    if progress == 0:
        if ha == 0:
            pygame.mixer.music.load('sounds/snowstorm.mp3')
            pygame.mixer.music.play(-1)
            ha += 1
        sprite.image = load_image("snow_qeen_1.png")
        colors = [(25, 116, 210), (72, 61, 139), (18, 47, 170)]
        BackGround = Background('data/snow_forest_1.jpg', [0, 0])
    if progress == 1:
        if ha == 1:
            pygame.mixer.music.load('sounds/kapel.mp3')
            pygame.mixer.music.play(-1)
            ha += 1
        BackGround = Background('data/snow_forest.jpg', [0, 0])
        colors = [(100, 149, 237), (25, 25, 112), (218, 112, 214)]
    if progress == 2:
        BackGround = Background('data/snow_forest_2.jpg', [0, 0])
        colors = [(252, 15, 192), (224, 176, 255), (255, 142, 0)]
        sprite.image = load_image("snow_qeen.png")
    if progress == 3:
        h = 0
        if ha == 2:
            pygame.mixer.music.load('sounds/snow_forest_20.mp3')
            pygame.mixer.music.play(-1)
            ha += 1
        gaga = False
        if dance != 0:
            dance -= 1
        sprite.image = load_image("snow_qeen.png", None, dance)
    piano.draw(screen)
    all_sprites.update()
    all_sprites.draw(screen)
    lives.draw(screen)
    if pygame.mouse.get_focused():
        mouse_but.draw(screen)
        DrawPictures()
    Draw_person()
    pygame.display.update()
    clock.tick(30)
