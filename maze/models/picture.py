import pygame


class Wall(pygame.sprite.Sprite):
    """
    This is a class of wall picture
    """
    def __init__(self):
        super().__init__()
        img = pygame.image.load('./models/wall.png')
        self.image = pygame.transform.scale(img, (100, 100))
        self.rect = self.image.get_rect()


class Character(pygame.sprite.Sprite):
    """
    This is a class of Character picture
    """
    def __init__(self):
        super().__init__()
        image = pygame.image.load('./models/player.png')
        self.image = pygame.transform.scale(image, (100, 100))
        self.rect = self.image.get_rect()


class Items(pygame.sprite.Sprite):
    """
    This is a class of Items picture
    """
    def __init__(self):
        super().__init__()
        image = pygame.image.load('./models/item.png')
        self.image = pygame.transform.scale(image, (100, 100))
        self.rect = self.image.get_rect()


class Floor(pygame.sprite.Sprite):
    """"
    This is a class of floor picture
    """
    def __init__(self):
        super().__init__()
        image = pygame.image.load('./models/floor.png')
        self.image = pygame.transform.scale(image, (100, 100))
        self.rect = self.image.get_rect()


class Exit(pygame.sprite.Sprite):
    """
    This is a class of exit picture
    """
    def __init__(self):
        super().__init__()
        image = pygame.image.load('./models/exit.png')
        self.image = pygame.transform.scale(image, (100, 100))
        self.rect = self.image.get_rect()
