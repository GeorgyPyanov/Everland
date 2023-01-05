import random
import pygame
from Tools import Particle, load_image


class Mountain(pygame.sprite.Sprite):
    image = load_image("mountains.png")

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Mountain.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = height


def create_particles(position):
    particle_count = 20
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers), all_sprites, 0.5, screen_rect,
                 ["snowflakes_1.png", 'snowflakes_3.png', 'snowflakes_2.png'])


pygame.init()
pygame.display.set_caption('Начало')
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
screen_rect = (0, 0, width, height)
running = True
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()
snow_list = []
pygame.mixer.music.load("sounds/snow.mp3")
mountain = Mountain()
pygame_icon = pygame.image.load('data/avatar.jpeg')
pygame.display.set_icon(pygame_icon)
for i in range(50):
    x = random.randrange(0, 600)
    y = random.randrange(0, 600)
    snow_list.append([x, y])
pygame.mixer.music.play(-1)
sprite = pygame.sprite.Sprite()
sprite.image = load_image("name.png")
sprite.rect = sprite.image.get_rect()
sprite.rect.x = 20
sprite.rect.y = 20
all_sprites.add(sprite)
font = pygame.font.Font('data/shrift.ttf', 15)
text = font.render("Вы чувствуете,как наполняетесь снежным настроением", True, (0, 0, 255))
text_x = width // 2 - text.get_width() // 2
text_y = height // 2 - text.get_height() // 2 + 70
text_w = text.get_width()
text_h = text.get_height()
screen.blit(text, (text_x, text_y))
text1 = font.render("Чтобы начать,"
                    "просто нажмите волшебную левую кнопку мыши", True, (0, 0, 255))
text_x1 = width // 2 - text.get_width() // 2 - 20
text_y1 = height // 2 - text.get_height() // 2 + 90
text_w1 = text.get_width()
text_h1 = text.get_height()
screen.blit(text1, (text_x1, text_y1))
n = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            create_particles(pygame.mouse.get_pos())
    screen.fill((0, 0, 0))
    for i in range(len(snow_list)):
        pygame.draw.circle(screen, [255, 255, 255], snow_list[i], 2)
        snow_list[i][1] += 1
        if snow_list[i][1] > 600:
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            x = random.randrange(0, 600)
            snow_list[i][0] = x
    if n >= 40:
        screen.blit(text, (text_x, text_y))
        screen.blit(text1, (text_x1, text_y1))
    if n == 180:
        n = 0
    n += 1
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(40)

pygame.quit()