import sys
from random import choice, randint
import pygame
import Map as Map
from Tools import Background, Mouse, Sprite_Mouse_Location, Particle, Particle_2, load_image, Atom


def end():
    pygame.init()
    pygame.display.set_caption('Конец')
    all_sprites = pygame.sprite.Group()
    mouse_but = pygame.sprite.Group()
    clock = pygame.time.Clock()
    BackGround = Background('data/bashnya_1.jpg', [0, 0])
    pygame_icon = pygame.image.load('data/avatar.jpeg')
    pygame.display.set_icon(pygame_icon)
    pygame.mixer.music.load("sounds/serdcebienie.mp3")
    pygame.mixer.music.play(-1)
    pygame.mouse.set_visible(False)
    mouse = Mouse(mouse_but)
    particles = []
    mouse_sprite = Sprite_Mouse_Location()
    colors = [(255, 0, 0), (220, 20, 60), (128, 0, 0)]
    list_pictures = ['fire.png', 'fire_2.png', 'fire_3.png']
    screen = pygame.display.set_mode((1024, 522))
    screen_rect = (0, 0, 1024, 522)
    particles1 = []
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("big_love_2.png")
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 350
    sprite.rect.y = 100
    all_sprites.add(sprite)
    n = -1
    x11 = 350
    y11 = 100
    na = 1
    g = 0
    bars0 = pygame.sprite.Group()
    bars1 = pygame.sprite.Group()
    a = ['Почувствуй, как оно бьется..', 'Вспомни всё!']
    w00, h00 = 460, 430
    bars1.add(Atom((w00, h00), a[0]))
    bars = pygame.sprite.Sprite()
    bars.image = load_image("bars.png")
    bars.rect = bars.image.get_rect()
    bars.rect.x = 0
    bars.rect.y = 350
    bars0.add(bars)
    perg = pygame.sprite.Sprite()
    perg.image = load_image("perg.png")
    perg.rect = bars.image.get_rect()
    perg.rect.x = 300
    perg.rect.y = 400
    bars0.add(perg)
    r = 0
    op = 0
    running = True

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

    def DrawPictures1():
        for i in particles1:
            i.render(screen)
            if i.radius <= 0:
                particles1.remove(i)

    while running:
        n += 1
        if n % 50 == 0:
            x11 += 10
            y11 += 10
        elif n % 50 == 25:
            x11 -= 10
            y11 -= 10
        sprite.rect.x = x11
        sprite.rect.y = y11
        screen.fill((0, 0, 0))
        events = pygame.event.get()
        for event in events:
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                mouse_but.update(pos[0], pos[1])
            if event.type == pygame.MOUSEBUTTONDOWN:
                create_particles(pygame.mouse.get_pos(), list_pictures)
                if a:
                    if len(a) != 1 and not op:
                        del a[0]
                        for i in bars1:
                            bars1.remove(i)
                        bars1.add(Atom((w00, h00), a[0]))
                    else:
                        r = 1
                if na == -7:
                    f = open("files/levels.txt", 'w')
                    f.seek(0)
                    f.write('1111')
                    f.close()
                    pygame.quit()
                    Map.main()
                    sys.exit()
        if pygame.sprite.collide_rect(sprite, mouse_sprite) and na > 0 and op:
            na += 1
        if pygame.sprite.collide_rect(sprite, mouse_sprite) and na < 0:
            g += 1
        mouse_sprite.rect.x = pos[0]
        mouse_sprite.rect.y = pos[1]
        for x in range(randint(15, 25)):
            particle = Particle_2(pos[0], pos[1], randint(0, 20) / 10,
                                  randint(-3, -1), randint(2, 5 + na // 10 + g // 10), choice(colors))
            particles.append(particle)
            for i in range(20):
                particle = Particle_2(randint(0, 1000), randint(0, 500), randint(0, 20) / 10,
                                      randint(-3, -1), randint(2, 5), choice(colors))
            particles1.append(particle)
        if r:
            bars.rect.x -= 2
        if bars.rect.x < -300 and na >= 0:
            op = 1
            w00, h00 = 210, 430
            perg.rect.x = 50
            perg.rect.y = 400
            for i in bars1:
                bars1.remove(i)
            bars1.add(Atom((w00, h00), '...'))
            na = 0
        if na == 500:
            na = 0
        if g == 500:
            g = 0
            if na != -7:
                na -= 1
        if na == 0:
            BackGround = Background('data/bashnya.jpg', [0, 0])
            pygame.mixer.music.load("sounds/bashnya_on.mp3")
            pygame.mixer.music.play(-1)
            na = -1
            sprite.image = load_image("big_love_3.png")
            colors = [(222, 184, 135), (255, 248, 220)]
            for i in bars1:
                bars1.remove(i)
            bars1.add(Atom((w00, h00), 'Ум', 30))
        if na == -2:
            BackGround = Background('data/snow_forest_2.jpg', [0, 0])
            colors = [(252, 15, 192), (224, 176, 255), (255, 142, 0)]
            pygame.mixer.music.load('sounds/snow_forest_20.mp3')
            pygame.mixer.music.play(-1)
            na = -3
            sprite.image = load_image("big_love_4.png")
            for i in bars1:
                bars1.remove(i)
            bars1.add(Atom((w00, h00), 'Чуткость', 30))
        if na == -4:
            BackGround = Background('data/dom.jpg', [0, 0])
            colors = [(255, 0, 148), (253, 108, 43), (255, 0, 0)]
            pygame.mixer.music.load("sounds/library.mp3")
            pygame.mixer.music.play(-1)
            na = -5
            sprite.image = load_image("big_love_5.png")
            for i in bars1:
                bars1.remove(i)
            bars1.add(Atom((w00, h00), 'Храбрость', 30))
        if na == -6:
            na = -7
            sprite.image = load_image("big_love_6.png")
            colors = [(255, 0, 0), (220, 20, 60), (128, 0, 0)]
            pygame.mixer.music.load("sounds/final.mp3")
            pygame.mixer.music.play(-1)
        if na <= 0 and na != -7:
            screen.blit(BackGround.image, BackGround.rect)
        if na == -7:
            screen.fill((238, 130, 238))
            for i in bars1:
                bars1.remove(i)
            for i in bars0:
                bars0.remove(i)
        all_sprites.update()
        all_sprites.draw(screen)
        mouse_but.draw(screen)
        DrawPictures()
        DrawPictures1()
        if r != 1000:
            bars0.draw(screen)
            bars1.draw(screen)
        pygame.display.update()
        clock.tick(50)

