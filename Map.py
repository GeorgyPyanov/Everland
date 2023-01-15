import sys
from random import randint, choice
import First_level as First_level
import Second_level as Second_level
import Third_level as Third_level
import Fourth_level as Fourth_level
import pygame
from Tools import load_image, Particle, Particle_2, Sprite_Mouse_Location, AnimatedSprite, Mouse, Background, Atom


def main():
    pygame.init()
    pygame.display.set_caption('Карта')
    size = width, height = 700, 600
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    screen_rect = (0, 0, width, height)
    running = True
    all_sprites = pygame.sprite.Group()
    mouse_but = pygame.sprite.Group()
    numbers_sprite = pygame.sprite.Group()
    numbers_sprite_2 = pygame.sprite.Group()
    bars0 = pygame.sprite.Group()
    bars1 = pygame.sprite.Group()
    a = ['Приветствую тебя, Герой!', 'Я Барс - великий волшебник страны Everland',
         'Давным-давно я даровал Сердце Волшебства людям',
         'Оно давало им Дары', 'У каждого человека был свой особенный Дар',
         'Кто-то управлял водой',
         'Кто-то искусно строил замки и дома ',
         'Но однажды Сердце было утеряно...',
         'Люди без Сердца стали алочными и жадными',
         'Они пошли войной на друг друга...',
         'Найди Сердце и помоги людям!']
    w00, h00 = 460, 430
    bars1.add(Atom((w00, h00), a[0]))
    bars = pygame.sprite.Sprite()
    bars.image = load_image("bars.png")
    bars.rect = bars.image.get_rect()
    bars.rect.x = 0
    bars.rect.y = 400
    bars0.add(bars)
    perg = pygame.sprite.Sprite()
    perg.image = load_image("perg.png")
    perg.rect = bars.image.get_rect()
    perg.rect.x = 300
    perg.rect.y = 400
    bars0.add(perg)
    BackGround = Background('data/fon_map.jpg', [0, 0])
    grop = []
    grop_2 = []
    f = open("files/levels.txt", encoding="utf8")
    level = f.readline()
    f.close()
    clock = pygame.time.Clock()
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
    fon = pygame.sprite.Sprite()
    sprite_island.image = load_image("island.png")
    sprite_island.rect = sprite_island.image.get_rect()
    sprite_island.rect.x = 20
    sprite_island.rect.y = 130
    all_sprites.add(sprite_island)
    one.image = load_image("one.png")
    one.rect = one.image.get_rect()
    one.rect.x = 520
    one.rect.y = 150
    two.image = load_image("two.png")
    two.rect = two.image.get_rect()
    two.rect.x = 320
    two.rect.y = 180
    three.image = load_image("three.png")
    three.rect = three.image.get_rect()
    three.rect.x = 420
    three.rect.y = 250
    four.image = load_image("four.png")
    four.rect = four.image.get_rect()
    four.rect.x = 120
    four.rect.y = 200
    if level[0] == '1':
        one.image = load_image("one_1.png")
        grop_2.append(one)
    else:
        grop.append(one)
    if level[1] == '1':
        two.image = load_image("two_1.png")
        grop_2.append(two)
    else:
        grop.append(two)
    if level[2] == '1':
        three.image = load_image("three_1.png")
        grop_2.append(three)
    else:
        grop.append(three)
    if level[3] == '1':
        four.image = load_image("four_1.png")
        grop_2.append(four)
    else:
        grop.append(four)
    mouse_sprite = Sprite_Mouse_Location()
    pygame.mixer.music.load("sounds/map.mp3")
    pygame.mixer.music.play(-1)
    if level == '1111':
        pygame.mixer.music.load("sounds/priz.mp3")
        pygame.mixer.music.play(-1)
    list_pictures = ['snowflakes_1.png', 'snowflakes_2.png', 'snowflakes_3.png']
    effect = AnimatedSprite(load_image("magic_2.png"), 4, 2, 170.75, 174, all_sprites, 10)
    effect.rect.x = 270
    effect.rect.y = 350
    effect2 = AnimatedSprite(load_image("fire_effect_20.png"), 4, 2, 170.75, 174, all_sprites, 2)
    effect2.rect.x = 270
    effect2.rect.y = 350
    all_sprites.remove(effect2)
    pygame.mouse.set_visible(False)
    mouse = Mouse(mouse_but)
    le = 1
    for i in grop_2:
        numbers_sprite_2.add(i)
    r = 0
    if level != '0000':
        a = []
        r = 1000

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
        spu = False
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                create_particles(pygame.mouse.get_pos(), list_pictures)
                if a:
                    if len(a) != 1:
                        del a[0]
                        for i in bars1:
                            bars1.remove(i)
                        bars1.add(Atom((w00, h00), a[0]))
                    else:
                        r = 1
                else:
                    if pygame.sprite.collide_rect(one, mouse_sprite) and level != '1111':
                        pygame.quit()
                        First_level.one1()
                        sys.exit()
                    if pygame.sprite.collide_rect(two, mouse_sprite) and level == '1000':
                        pygame.quit()
                        Second_level.two1()
                        sys.exit()
                    if pygame.sprite.collide_rect(three, mouse_sprite) and level == '1100':
                        pygame.quit()
                        Third_level.three1()
                        sys.exit()
                    if pygame.sprite.collide_rect(four, mouse_sprite) and level == '1110':
                        pygame.quit()
                        Fourth_level.four1()
                        sys.exit()
            if event.type == pygame.MOUSEMOTION:
                mouse_but.update(pos[0], pos[1])
                if pygame.sprite.collide_rect(sprite_island, mouse_sprite) and level != '1111':
                    BackGround = Background('data/fon_map_1.jpg', [0, 0])
                    all_sprites.remove(effect)
                    all_sprites.add(effect2)
                    sprite_island.image = load_image("island_on.png")
                    fon.image = load_image("fon_2.png")
                    colors = [(1, 1, 1), (155, 155, 155)]
                    list_pictures = ['fire.png', 'fire_2.png', 'fire_3.png']
                    spu = True
                    for i in grop:
                        numbers_sprite.add(i)
                    for i in grop_2:
                        numbers_sprite_2.remove(i)
                else:
                    BackGround = Background('data/fon_map.jpg', [0, 0])
                    all_sprites.remove(effect2)
                    all_sprites.add(effect)
                    sprite_island.image = load_image("island.png")
                    fon.image = load_image("fon.png")
                    colors = [(0, 0, 255), (255, 255, 255)]
                    list_pictures = ['snowflakes_1.png', 'snowflakes_2.png', 'snowflakes_3.png']
                    for i in grop:
                        numbers_sprite.remove(i)
                    for i in grop_2:
                        numbers_sprite_2.add(i)
        if r:
            bars.rect.x -= 2
        if r == 1000:
            for i in bars0:
                bars0.remove(i)
        if bars.rect.x < -300:
            r = 1000
            a = []
        if pygame.sprite.collide_rect(effect, mouse_sprite):
            colors = [(255, 0, 0), (255, 79, 0), (204, 85, 0), (255, 36, 0), (255, 127, 73)]
            if level == '1111':
                colors = [(255, 69, 0), (255, 0, 0), (255, 255, 0),
                          (0, 255, 0), (0, 255, 255), (0, 0, 128), (75, 0, 130)]
        mouse_sprite.rect.x = pos[0]
        mouse_sprite.rect.y = pos[1]
        for x in range(randint(15, 25)):
            particle = Particle_2(pos[0], pos[1], randint(0, 20) / 10,
                                  randint(-3, -1), randint(2, 5), choice(colors))
            particles.append(particle)
        screen.fill((0, 0, 0))
        screen.blit(BackGround.image, BackGround.rect)
        if level == '1111':
            screen.fill((255, 105, 180))
            colors = [(220, 20, 60), (139, 0, 139)]
            BackGround = Background('data/fon_map_3.jpg', [0, 0])
            screen.blit(BackGround.image, BackGround.rect)
        all_sprites.update()
        all_sprites.draw(screen)
        numbers_sprite.draw(screen)
        numbers_sprite_2.draw(screen)
        if r != 1000:
            bars0.draw(screen)
            bars1.draw(screen)
        if pygame.mouse.get_focused():
            mouse_but.draw(screen)
            DrawPictures()
        pygame.display.flip()
        clock.tick(40)
