from pygame.image import load
from pygame.mask import from_surface
from pygame.sprite import Sprite
from pygame.sprite import Group
from pygame.transform import scale
import random
all_bullets = Group()
hero_group = Group()
enemy_group = Group()
hero_move = [0, 0]


class Character:
    """
    класс существа на карте
    """

    # параметры
    _HP = 1
    _armour = 1
    _damage = 1
    _cool_down = 5

    def __int__(self, hp, arm, dmg, cd):
        self._HP = hp
        self._armour = arm
        self._damage = dmg
        self._cool_down = cd

    # регистрация урона, полученного персонажем
    def received_damage(self, received_dmg):
        """
        снижение брони и здоровья в результате полученного урона
        :param received_dmg: полученный персонажем урон
        :return: void
        """
        self._HP = min(self._HP, self._HP - (received_dmg - self._armour))
        self._armour = max(self._armour - received_dmg, 0)


class Hero(Character, Sprite):
    """
    класс нашего персонажа
    """
    image = scale(load("hero.png"), (50, 50))

    def __init__(self, hp, arm, dmg, cd, x, y):
        super().__int__(hp, arm, dmg, cd)
        super().__init__(hero_group)
        self.image = Hero.image
        self.rect = self.image.get_rect()
        self.mask = from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.add(hero_group)
        self._crit = 0.1

    def update(self):
        self.rect.x += hero_move[0]
        self.rect.y += hero_move[1]

    def get_position(self):
        return self.rect.x + 50 / 2, self.rect.y + 50 / 2


class Enemy(Character, Sprite):
    """
    класс одного моба
    """
    image = scale(load("моб.png"), (60, 60))

    def __init__(self):
        super().__int__(random.randint(0, 10),
                        random.randint(0, 10),
                        random.randint(0, 10),
                        random.randint(0, 10),)
        super().__init__(enemy_group)
        self.image = Enemy.image
        self.rect = self.image.get_rect()
        self.mask = from_surface(self.image)
        self.rect.x = random.randint(0, 100)
        self.rect.y = random.randint(0, 100)
        self.add(enemy_group)
        print(self.__dict__)

    def update(self):
        Bullet((self.rect.x + 60/2, self.rect.y + 60/2), (random.randint(-5, 5), random.randint(-5, 5)), False)


class Bullet(Sprite):
    image = scale(load("Fireball.png"), (20, 20))
    shooter = True # true if hero, false if enemy

    def __init__(self, pos, direct, shooter, dmg=1):
        super().__init__(all_bullets)
        self.image = Bullet.image
        self.rect = self.image.get_rect()
        self.mask = from_surface(self.image)
        self.rect.x = pos[0] - 20 / 2
        self.rect.y = pos[1] - 20 / 2
        self.add(all_bullets)
        self.direct_x = direct[0]
        self.direct_y = direct[1]
        self.shooter = shooter
        self.damage = dmg

    def update(self):
        self.rect = self.rect.move(self.direct_x, self.direct_y)

