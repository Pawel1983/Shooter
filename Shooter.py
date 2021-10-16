import pygame, random
from sys import exit


class Crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("graphics/crosshair.png")
        self.rect = self.image.get_rect()
        # self.gunshot = pygame.mixer.Sound("sound/gunshot.wav")

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Balloon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.balloons = []
        self.balloons.append(pygame.transform.rotozoom(pygame.image.load("graphics/red-balloon/1.png"), 0, 0.4))
        self.balloons.append(pygame.transform.rotozoom(pygame.image.load("graphics/red-balloon/2.png"), 0, 0.4))
        self.balloons.append(pygame.transform.rotozoom(pygame.image.load("graphics/red-balloon/3.png"), 0, 0.4))
        self.balloons.append(pygame.transform.rotozoom(pygame.image.load("graphics/red-balloon/4.png"), 0, 0.4))
        self.balloons.append(pygame.transform.rotozoom(pygame.image.load("graphics/red-balloon/5.png"), 0, 0.4))
        self.balloons.append(pygame.transform.rotozoom(pygame.image.load("graphics/red-balloon/6.png"), 0, 0.4))
        self.pos_x = random.randint(100, 1820)
        self.pos_y = 1100
        self.current_index = 0
        self.image = self.balloons[self.current_index]
        self.rect = self.image.get_rect()
        self.rect.center = [self.pos_x, self.pos_y]

    def shoot(self):
        # self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, balloon_group, True)

    def update(self):
        self.rect.y -= 2


class Boom(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.booms = []
        self.is_animated = False
        self.booms.append(pygame.transform.rotozoom(pygame.image.load("graphics/red-balloon/1.png"), 0, 0.4))
        self.booms.append(pygame.transform.rotozoom(pygame.image.load("graphics/red-balloon/2.png"), 0, 0.4))
        self.booms.append(pygame.transform.rotozoom(pygame.image.load("graphics/red-balloon/3.png"), 0, 0.4))
        self.booms.append(pygame.transform.rotozoom(pygame.image.load("graphics/red-balloon/4.png"), 0, 0.4))
        self.booms.append(pygame.transform.rotozoom(pygame.image.load("graphics/red-balloon/5.png"), 0, 0.4))
        self.booms.append(pygame.transform.rotozoom(pygame.image.load("graphics/red-balloon/6.png"), 0, 0.4))
        self.pos_x = random.randint(100, 1820)
        self.pos_y = 1100
        self.current_boom_index = 0
        self.image = self.booms[self.current_boom_index]
        self.rect = self.image.get_rect()

    def animate(self):
        if self.is_animated is True:
            self.current_boom_index += 0.3
            if self.current_boom_index >= len(self.booms):
                self.current_boom_index = 0
                self.is_animated = False
            self.image = self.booms[int(self.current_boom_index)]

    def update(self):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.is_animated = True
        self.animate()

# Game setup
pygame.init()
screen = pygame.display.set_mode((1920, 1000))
pygame.display.set_caption("Shooter by Tata")
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
game_active = True

# Background
background = pygame.image.load("graphics/Forest_Background.png").convert()
background = pygame.transform.rotozoom(background, 0, 1.05)

# Groups
crosshair = Crosshair()
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

balloon = Balloon()
balloon_group = pygame.sprite.Group()
balloon_group.add(balloon)

boom = Boom()
boom_group = pygame.sprite.Group()
boom_group.add(boom)

# Timer
balloon_timer = pygame.USEREVENT + 1
pygame.time.set_timer(balloon_timer, 1800)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == balloon_timer:
                balloon_group.add(Balloon())

        if event.type == pygame.MOUSEBUTTONDOWN:
            balloon.shoot()

    # Game active
    if game_active:
        screen.blit(background, (-200, -900))

        boom_group.draw(screen)
        boom_group.update()

        balloon_group.draw(screen)
        balloon_group.update()

        crosshair_group.draw(screen)
        crosshair_group.update()


    # Intro
    # else:
    #     screen.fill("grey")

    pygame.display.update()
    clock.tick(60)
