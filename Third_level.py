from random import choice, randint
import pygame
from Tools import Background, Mouse, Sprite_Mouse_Location, load_image, Particle, Particle_2

pygame.init()
pygame.display.set_caption('Дом всех вещей')
all_sprites = pygame.sprite.Group()
mouse_but = pygame.sprite.Group()
lives = pygame.sprite.Group()
mini_game = pygame.sprite.Group()
mini_game_0 = pygame.sprite.Group()
mini_game_1 = pygame.sprite.Group()
level = 3
screen = pygame.display.set_mode((1024, 522))
screen_rect = (0, 0, 1024, 522)
clock = pygame.time.Clock()
pygame.key.set_repeat(200, 25)
BackGround = Background('data/dom.jpg', [0, 0])
pygame_icon = pygame.image.load('data/avatar.jpeg')
pygame.display.set_icon(pygame_icon)
pygame.mixer.music.load("sounds/boy.mp3")
pygame.mixer.music.play(-1)
pygame.mouse.set_visible(False)
mouse = Mouse(mouse_but)
particles = []
mouse_sprite = Sprite_Mouse_Location()
colors = [(255, 0, 148), (253, 108, 43), (255, 0, 0)]
list_pictures = ['fire.png', 'fire_2.png', 'fire_3.png']
for i in range(3):
    sprite1 = pygame.sprite.Sprite()
    sprite1.image = load_image("fire_20.png")
    sprite1.rect = sprite1.image.get_rect()
    sprite1.rect.x = 900 + i * 40
    sprite1.rect.y = 0
    lives.add(sprite1)
particles1 = []
gaga = True
h = 0
sprite = pygame.sprite.Sprite()
sprite.image = load_image("chelovek.png")
sprite.rect = sprite.image.get_rect()
sprite.rect.x = 450
sprite.rect.y = 280
all_sprites.add(sprite)
sprite1 = pygame.sprite.Sprite()
sprite1.image = load_image("monstr_0.png")
sprite1.rect = sprite1.image.get_rect()
sprite1.rect.x = 50
sprite1.rect.y = 50
all_sprites.add(sprite1)
sprite2 = pygame.sprite.Sprite()
sprite2.image = load_image("pen_0.png")
sprite2.rect = sprite1.image.get_rect()
sprite2.rect.x = 800
sprite2.rect.y = 300
all_sprites.add(sprite2)
sprite3 = pygame.sprite.Sprite()
sprite3.image = load_image("pen_0.png")
sprite3.rect = sprite1.image.get_rect()
sprite3.rect.x = 850
sprite3.rect.y = 400
all_sprites.add(sprite3)
sprite4 = pygame.sprite.Sprite()
sprite4.image = load_image("pen_1.png")
sprite4.rect = sprite1.image.get_rect()
sprite4.rect.x = 700
sprite4.rect.y = 350
all_sprites.add(sprite4)
p = True
na = 0
sprite5 = pygame.sprite.Sprite()
sprite5.image = load_image("tablichka_3.png")
sprite5.rect = sprite1.image.get_rect()
sprite5.rect.x = 0
sprite5.rect.y = 483
all_sprites.add(sprite5)
c = True
button = 3
monster = 2
ca = False


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


def create_particles(position, list_pictures_0, k=False):
    particle_count = 20
    numbers = range(-5, 6)
    for _ in range(particle_count):
        if k:
            Particle((position[0] - 10, position[1]), choice(numbers), choice(numbers), mini_game_1, 0.5, screen_rect,
                     list_pictures_0)
        else:
            Particle((position[0] - 10, position[1]), choice(numbers), choice(numbers), all_sprites, 0.5, screen_rect,
                     list_pictures_0)


class Pyl(pygame.sprite.Sprite):
    def __init__(self, y, k, n, la):
        super().__init__(y)
        image = load_image(k)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 980
        self.rect.y = 390 + la * 44
        self.n = n

    def update(self):
        self.rect.x -= self.n
        if self.rect.x == -44:
            mini_game.remove(self)


while True:
    na += 1
    if gaga:
        if na % 2 == 0:
            p = not p
    else:
        if na % 3 == 0:
            p = not p
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
            if event.button == 1 and pygame.sprite.collide_rect(sprite5, mouse_sprite) and button != 3:
                pygame.mixer.music.load("sounds/library.mp3")
                pygame.mixer.music.play(-1)
                for i in mini_game_0:
                    mini_game_0.remove(i)
                for i in mini_game:
                    mini_game.remove(i)
                mini_game_0.add(sprite5)
                sprite6 = pygame.sprite.Sprite()
                sprite6.image = load_image("polki.png")
                sprite6.rect = sprite1.image.get_rect()
                sprite6.rect.x = 0
                sprite6.rect.y = 0
                mini_game.add(sprite6)
                sprite7 = pygame.sprite.Sprite()
                sprite7.image = load_image("polki.png")
                sprite7.rect = sprite1.image.get_rect()
                sprite7.rect.x = 1024
                sprite7.rect.y = 0
                mini_game.add(sprite7)
                sprite8 = pygame.sprite.Sprite()
                sprite8.image = load_image("chelovek_0.png")
                sprite8.rect = sprite8.image.get_rect()
                sprite8.rect.x = 100
                sprite8.rect.y = 390
                mini_game.add(sprite8)
                sprite5.rect.x = 0
                sprite5.rect.y = 0
                na = 8
                pr = 0
                c = False
                while True:
                    c = False
                    pr += na
                    screen.fill((225, 225, 225))
                    events = pygame.event.get()
                    for i in events:
                        pos = pygame.mouse.get_pos()
                        if i.type == pygame.QUIT:
                            exit()
                        if i.type == pygame.MOUSEMOTION:
                            mouse_but.update(pos[0], pos[1])
                        if i.type == pygame.MOUSEBUTTONDOWN:
                            create_particles(pygame.mouse.get_pos(), list_pictures, True)
                        if i.type == pygame.KEYDOWN:
                            if i.key == pygame.K_UP:
                                if sprite8.rect.y != 390:
                                    sprite8.rect.y = sprite8.rect.y - 44
                            if i.key == pygame.K_DOWN:
                                if sprite8.rect.y != 478:
                                    sprite8.rect.y = sprite8.rect.y + 44
                            if i.key == pygame.K_LEFT:
                                if sprite8.rect.x >= 44:
                                    sprite8.rect.x = sprite8.rect.x - 44
                            if i.key == pygame.K_RIGHT:
                                if sprite8.rect.x < 980:
                                    sprite8.rect.x = sprite8.rect.x + 44
                    mouse_sprite.rect.x = pos[0]
                    mouse_sprite.rect.y = pos[1]
                    sprite6.rect.x = sprite6.rect.x - na
                    sprite7.rect.x = sprite7.rect.x - na
                    if sprite6.rect.x == -1024:
                        sprite6.rect.x = 0
                    if sprite7.rect.x == 0:
                        sprite7.rect.x = 1024
                    if button == 1:
                        sprite5.image = load_image("tablichka_2.png")
                    elif button == 2:
                        sprite5.image = load_image("tablichka_1.png")
                    elif button == 3:
                        sprite5.image = load_image("tablichka_0.png")
                    for x in range(randint(15, 25)):
                        particle = Particle_2(pos[0], pos[1], randint(0, 20) / 10,
                                              randint(-3, -1), randint(2, 5),
                                              choice([(165, 38, 10), (77, 34, 14), (243, 71, 35)]))
                        particles.append(particle)
                        particles1.append(particle1)
                    if pr % choice(range(1, 100)) == 0 and pr % 66 < 4:
                        ab = choice([0, 1, 2])
                        p = Pyl(mini_game, 'pyl.png', na, ab)
                    if pr % 7000 == 0:
                        qw = [0, 1, 2]
                        del qw[qw.index(ab)]
                        ab0 = choice(qw)
                        p = Pyl(mini_game_0, choice(['predmety_0.png', 'predmety_1.png',
                                                     'predmety_2.png', 'predmety_3.png']), na, ab0)
                    for i in mini_game_0:
                        if pygame.sprite.collide_rect(i, sprite8):
                            mini_game_0.remove(i)
                            button += 1
                    for i in mini_game:
                        if i != sprite8 and i != Particle and pygame.sprite.collide_rect(i, sprite8):
                            c = True
                            break
                    if c:
                        for i in lives:
                            lives.remove(i)
                            break
                        level -= 1
                        button = 0
                        break
                    if button == 3:
                        break
                    mini_game.update()
                    mini_game.draw(screen)
                    mini_game_0.update()
                    mini_game_0.draw(screen)
                    mini_game_1.update()
                    mini_game_1.draw(screen)
                    lives.draw(screen)
                    if pygame.mouse.get_focused():
                        mouse_but.draw(screen)
                        DrawPictures()
                    Draw_person()
                    pygame.display.update()
                    clock.tick(60)
                if button == 0:
                    sprite5.image = load_image("tablichka_3.png")
                    sprite5.rect.x = 0
                    sprite5.rect.y = 483
                elif button == 3:
                    sprite5.image = load_image("tablichka_0.png")
                    sprite5.rect.x = 0
                    sprite5.rect.y = 468
                pygame.mixer.music.load("sounds/boy.mp3")
                pygame.mixer.music.play(-1)
            elif event.button == 1 and pygame.sprite.collide_rect(sprite5, mouse_sprite):
                ca = True
                button = 0
                pygame.mixer.Sound('sounds/ogon.mp3').play()
    if ca:
        h += 4
        sprite2.rect.x += 5
        sprite3.rect.x += 5
        sprite4.rect.x += 5
    if h == 480:
        ca = False
        h = 0
        sprite2.rect.x = 800
        sprite2.rect.y = 300
        sprite4.rect.x = 700
        sprite4.rect.y = 350
        sprite3.rect.x = 850
        sprite3.rect.y = 400
        monster += 1
        sprite1.rect.x = 50
        sprite1.rect.y = 50
    if monster == 0:
        sprite1.image = load_image("monstr_0.png")
    elif monster == 1:
        sprite1.image = load_image("monstr_1.png")
    elif monster == 2:
        sprite1.image = load_image("monstr_2.png")
    elif monster == 3:
        sprite1.image = load_image("monstr_30.png")
        sprite1.rect.x = 50
        sprite1.rect.y = 350
    mouse_sprite.rect.x = pos[0]
    mouse_sprite.rect.y = pos[1]
    if button == 0:
        sprite5.image = load_image("tablichka_3.png")
        sprite5.rect.x = 0
        sprite5.rect.y = 483
    elif button == 3:
        sprite5.image = load_image("tablichka_0.png")
        sprite5.rect.x = 0
        sprite5.rect.y = 468
    for x in range(randint(15, 25)):
        if gaga:
            particle = Particle_2(pos[0], pos[1], randint(0, 20) / 10,
                                  randint(-3, -1), randint(2, 5), choice(colors))
            particle1 = Particle_2(510, 380, randint(-10 - h, 10 + h) / 2,
                                   randint(1 - h, 5 + h), randint(2, 5 + h // 100 * 3), choice(colors))
            particles.append(particle)
            particles1.append(particle1)
        else:
            for i in range(20):
                particle = Particle_2(randint(0, 1000), randint(0, 500), randint(0, 20) / 10,
                                      randint(-3, -1), randint(2, 5), choice(colors))
            particles1.append(particle)
    if gaga:
        if p and na % 2 == 0:
            sprite2.rect.x += 1
            sprite3.rect.x += 2
            sprite4.rect.x += 3
            if ca:
                sprite1.rect.y -= 5
        elif not p and na % 2 == 0:
            sprite2.rect.x -= 1
            sprite3.rect.x -= 2
            sprite4.rect.x -= 3
            if ca:
                sprite1.rect.y += 5
    else:
        if p and na % 2 == 0:
            sprite2.image = load_image("pen_0.png", None, 255, 10)
            sprite3.image = load_image("pen_0.png", None, 255, 10)
            sprite4.image = load_image("pen_1.png", None, 255, 10)
        elif not p and na % 2 == 0:
            sprite2.image = load_image("pen_0.png", None, 255, -10)
            sprite3.image = load_image("pen_0.png", None, 255, -10)
            sprite4.image = load_image("pen_1.png", None, 255, -10)
    if monster == 3 and gaga:
        gaga = False
        pygame.mixer.music.load("sounds/tanez.mp3")
        pygame.mixer.music.play(-1)
        all_sprites.remove(sprite5)
        for i in lives:
            lives.remove(i)
        sprite2.rect.x = 250
        sprite3.rect.x = 850
        sprite4.rect.x = 650
        sprite2.rect.y = 300
        sprite3.rect.y = 300
        sprite4.rect.y = 300
    if level == 0:
        pygame.mixer.music.load("sounds/boy_1.mp3")
        pygame.mixer.music.play(-1)
        level = 10000
        all_sprites.remove(sprite5)
        for i in lives:
            lives.remove(i)
    if level == 10000:
        sprite2.rect.x += 5
        sprite3.rect.x += 5
        sprite4.rect.x += 5
        sprite1.rect.x += 1
    if sprite2.rect.x >= 1025 and sprite3.rect.x >= 1025 and sprite5.rect.x >= 1025 or sprite1.rect.x == 250 \
            and level == 10000:
        level = 10001
        BackGround = Background('data/dom_2.jpg', [0, 0])
        colors = [(1, 1, 1), (0, 0, 0)]
        pygame.mixer.Sound('sounds/proigr.mp3').play()

    all_sprites.update()
    all_sprites.draw(screen)
    lives.draw(screen)
    if pygame.mouse.get_focused():
        mouse_but.draw(screen)
        DrawPictures()
    Draw_person()
    pygame.display.update()
    clock.tick(30)
