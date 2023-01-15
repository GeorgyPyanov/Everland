import sys
from random import choice, randint
from pygameZoom import PygameZoom
import pygame
from pygame_textinput import TextInputVisualizer, TextInputManager
import sqlite3
from Tools import Background, Particle, Mouse, Sprite_Mouse_Location, Particle_2, Atom, load_image
import Map as Map


def one1():
    con = sqlite3.connect("riddle.db")
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM riddles""").fetchall()
    con.close()
    answer = choice(result)
    pygame.init()
    pygame.display.set_caption('Башня загадок')
    font = pygame.font.SysFont('data/shrift.ttf', 50)
    all_sprites = pygame.sprite.Group()
    mouse_but = pygame.sprite.Group()
    manager = TextInputManager()
    n = 3
    textinput_custom = TextInputVisualizer(manager=manager, font_object=font)
    textinput_custom.cursor_width = 0
    textinput_custom.cursor_blink_interval = 400
    textinput_custom.antialias = False
    textinput_custom.font_color = (0, 85, 170)
    screen = pygame.display.set_mode((1024, 522))
    pygameZoom = PygameZoom(1024, 522)
    bars0 = pygame.sprite.Group()
    bars1 = pygame.sprite.Group()
    a = ['Это старинное место называется Башня загадок', 'В это место еще в давние времена',
         'Приходили люди со всего королевства',
         'Чтобы испытать свою мудрость...',
         'В этой башне заключена древняя путеводная магия',
         'Освободи её и начни свой путь!']
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
    screen_rect = (0, 0, 1024, 522)
    clock = pygame.time.Clock()
    pygame.key.set_repeat(200, 25)
    BackGround = Background('data/bashnya_1.jpg', [0, 0])
    pygame_icon = pygame.image.load('data/avatar.jpeg')
    pygame.display.set_icon(pygame_icon)
    pygame.mixer.music.load("sounds/bashnya.mp3")
    pygame.mixer.music.play(-1)
    pygame.mouse.set_visible(False)
    mouse = Mouse(mouse_but)
    particles = []
    mouse_sprite = Sprite_Mouse_Location()
    colors = [(255, 255, 255), (1, 1, 1), (155, 155, 155)]
    list_pictures = ['fire.png', 'fire_2.png', 'fire_3.png']
    font = pygame.font.Font('data/shrift_2.ttf', 10)
    text = font.render(answer[0].rstrip(), True, (0, 0, 0))
    text_x = choice(range(500))
    text_y = choice(range(300, 500))
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    font = pygame.font.Font('data/shrift_2.ttf', 15)
    text1 = font.render(f'Попыток осталось: {str(n)} из 3', True, (0, 0, 0))
    text_x1 = 850
    text_y1 = 10
    text_w1 = text1.get_width()
    text_h1 = text1.get_height()
    screen.blit(text1, (text_x1, text_y1))
    na = True
    particles1 = []
    r = 0

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

    while True:
        screen.fill((225, 225, 225))
        events = pygame.event.get()
        textinput_custom.update(events)
        textinput_custom.font_color = choice(colors)
        for event in events:
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if textinput_custom.value.lower() != answer[1].rstrip():
                    n -= 1
                    text1 = font.render(f'Попыток осталось: {str(n)} из 3', True, (0, 0, 0))
                    textinput_custom.value = ''
                else:
                    BackGround = Background('data/bashnya.jpg', [0, 0])
                    text1 = font.render(f'Поздравляю, герой!', True, (0, 0, 0))
                    colors = [(222, 184, 135), (255, 248, 220)]
                    pygame.mixer.music.load("sounds/bashnya_on.mp3")
                    pygame.mixer.music.play(-1)
                    na = False
            if event.type == pygame.MOUSEMOTION:
                mouse_but.update(pos[0], pos[1])
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
                    if not na:
                        f = open("files/levels.txt", 'w')
                        f.seek(0)
                        f.write('1000')
                        f.close()
                        pygame.quit()
                        Map.main()
                        sys.exit()
        mouse_sprite.rect.x = pos[0]
        mouse_sprite.rect.y = pos[1]
        if n == 0:
            f = open("files/levels.txt", 'w')
            f.seek(0)
            f.write('2000')
            f.close()
            pygame.quit()
            Map.main()
            sys.exit()
        if r:
            bars.rect.x -= 2
        if r == 1000:
            for i in bars0:
                bars0.remove(i)
        if bars.rect.x < -300:
            r = 1000
            a = []
        for x in range(randint(15, 25)):
            particle = Particle_2(pos[0], pos[1], randint(0, 20) / 10,
                                  randint(-3, -1), randint(2, 5), choice(colors))
            particles.append(particle)
            if not na:
                for i in range(20):
                    particle = Particle_2(randint(0, 1000), randint(0, 500), randint(0, 20) / 10,
                                          randint(-3, -1), randint(2, 5), choice(colors))
                particles1.append(particle)
        screen.blit(pygameZoom.generate_surface(), (0, 0))
        pygameZoom.blit(BackGround.image, BackGround.rect)
        if na:
            pygameZoom.blit(text, (text_x, text_y))
        pygameZoom.blit(text1, (text_x1, text_y1))
        pygameZoom.render(screen, (0, 0))
        all_sprites.update()
        all_sprites.draw(screen)
        screen.blit(textinput_custom.surface, (50, 100))
        if r != 1000:
            bars0.draw(screen)
            bars1.draw(screen)
        if pygame.mouse.get_focused():
            mouse_but.draw(screen)
            DrawPictures()
        if not na:
            DrawPictures1()
        pygame.display.update()
        clock.tick(30)



