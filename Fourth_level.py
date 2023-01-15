import sys
from random import randint, choice, shuffle
import pygame
import Map as Map
from End import end
from Tools import load_image, Particle_2, Mouse, Sprite_Mouse_Location, Particle, Atom


def four1():
    def load_level(filename):
        filename = "files/" + filename
        with open(filename, 'r') as mapFile:
            level_map = [line.strip() for line in mapFile]
        max_width = max(map(len, level_map))
        return list(map(lambda x: x.ljust(max_width, '.'), level_map))

    FPS = 50
    tile_images = {
        'wall': load_image('box.png'),
        'empty': load_image('grass.png'),
        'love': load_image('love.png')
    }
    player_image = load_image('fire_21.png')
    tile_width = tile_height = 64
    mouse_but = pygame.sprite.Group()

    class Tile(pygame.sprite.Sprite):
        def __init__(self, tile_type, pos_x, pos_y):
            super().__init__(tiles_group)
            self.image = tile_images[tile_type]
            self.rect = self.image.get_rect().move(
                tile_width * pos_x, tile_height * pos_y)

    class Love(pygame.sprite.Sprite):
        def __init__(self, tile_type, pos_x, pos_y):
            super().__init__(love_group)
            self.image = tile_images[tile_type]
            self.rect = self.image.get_rect().move(
                tile_width * pos_x, tile_height * pos_y)

    class Player(pygame.sprite.Sprite):
        def __init__(self, pos_x, pos_y):
            super().__init__(player_group)
            self.image = player_image
            self.rect = self.image.get_rect().move(
                tile_width * pos_x, tile_height * pos_y)
            self.pos = (pos_x, pos_y)

        def move(self, x, y):
            x0, y0 = self.pos
            if x < 0:
                if move(player, 'left'):
                    self.rect = self.rect.move(x, y)
                    self.pos = (self.pos[0] - 1, self.pos[1])
                    x0, y0 = self.pos
            elif x > 0:
                if move(player, 'right'):
                    self.rect = self.rect.move(x, y)
                    self.pos = (self.pos[0] + 1, self.pos[1])
                    x0, y0 = self.pos
            elif y > 0:
                if move(player, 'down'):
                    self.rect = self.rect.move(x, y)
                    self.pos = (self.pos[0], self.pos[1] + 1)
                    x0, y0 = self.pos
            elif y < 0:
                if move(player, 'up'):
                    self.rect = self.rect.move(x, y)
                    self.pos = (self.pos[0], self.pos[1] - 1)
                    x0, y0 = self.pos
            while True:
                shuffle(level_map)
                if level_map[y0][x0] != '#' and (y0 == 0 or y0 == 7 or (level_map[y0 + 1][x0] != '#' or
                                                                        level_map[y0 - 1][x0] != '#'
                                                                        or level_map[y0][x0 + 1] != '#' or
                                                                        level_map[y0][x0 - 1] != '#')):
                    break
            for i in tiles_group:
                tiles_group.remove(i)
            for i in love_group:
                love_group.remove(i)
            generate_level(level_map, False)

    def terminate():
        pygame.quit()
        sys.exit()

    def generate_level(level, j=True):
        new_player, x, y = None, None, None
        for y in range(len(level)):
            for x in range(len(level[y])):
                if level[y][x] == '.':
                    Tile('empty', x, y)
                elif level[y][x] == '#':
                    Tile('wall', x, y)
                elif level[y][x] == '@':
                    Tile('empty', x, y)
                    if j:
                        new_player = Player(x, y)
                elif level[y][x] == '*':
                    Tile('empty', x, y)
                    Love('love', x, y)
        return new_player, x, y

    def move(hero, movement):
        x, y = hero.pos
        if movement == 'up':
            if y > 0 and (level_map[y - 1][x] != '#'):
                return True
        elif movement == 'down':
            if y < 7 and (level_map[y + 1][x] != '#'):
                return True
        elif movement == 'left':
            if x >= 0 and (level_map[y][x - 1] != '#'):
                return True
        elif movement == 'right':
            if x < level_x and (level_map[y][x + 1] != '#'):
                return True

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

    pygame.init()
    pygame.display.set_caption('Лабиринт')
    size = width, height = 1024, 512
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1024, 512))
    screen.fill((255, 255, 255))
    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    love_group = pygame.sprite.Group()
    level_map = load_level('level.txt')
    player, level_x, level_y = generate_level(level_map)
    ran = True
    mouse = Mouse(mouse_but)
    particles = []
    mouse_sprite = Sprite_Mouse_Location()
    colors = [(255, 0, 0), (220, 20, 60), (128, 0, 0)]
    list_pictures = ['snowflakes_1.png', 'snowflakes_2.png', 'snowflakes_3.png']
    na = True
    particles1 = []
    screen_rect = (0, 0, 1024, 512)
    pygame.mouse.set_visible(False)
    pygame_icon = pygame.image.load('data/avatar.jpeg')
    pygame.display.set_icon(pygame_icon)
    pygame.mixer.music.load("sounds/love.mp3")
    pygame.mixer.music.play(-1)
    bars0 = pygame.sprite.Group()
    bars1 = pygame.sprite.Group()
    a = ['Поздравляю, герой!', 'Ты дошел до последнего испытания',
         'Но не расслабляйся!', 'Это лабиринт сердца...',
         'В нем все возможно, бесконечно и непостоянно...',
         'Я не дам тебе никаких советов...']
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
    while ran:
        screen.fill((225, 225, 225))
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and na and not a:
                if event.key == pygame.K_UP:
                    player.move(0, -64)
                if event.key == pygame.K_DOWN:
                    player.move(0, 64)
                if event.key == pygame.K_RIGHT:
                    player.move(64, 0)
                if event.key == pygame.K_LEFT:
                    player.move(-64, 0)
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
        mouse_sprite.rect.x = pos[0]
        mouse_sprite.rect.y = pos[1]
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
        for i in love_group:
            if pygame.sprite.collide_rect(i, player):
                pygame.quit()
                end()
                sys.exit()
        if na:
            tiles_group.draw(screen)
            player_group.draw(screen)
            love_group.draw(screen)
        all_sprites.update()
        all_sprites.draw(screen)
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



