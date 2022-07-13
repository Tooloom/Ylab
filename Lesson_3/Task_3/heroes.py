from abc import ABC, abstractmethod

from antagonistfinder import AntagonistFinder
from attack_pack import *


class SuperHero(ABC):
    @abstractmethod
    def find(self, place):
        pass

    @abstractmethod
    def attack(self):
        pass


class Ultimate(ABC):
    @abstractmethod
    def ultimate(self):
        pass


class Superman(Hook, Laser, Ultimate, SuperHero):
    def __init__(self, name='Clark Kent', can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)

    def attack(self):
        return self.hook()

    def ultimate(self):
        return self.incinerate_with_lasers()


class ChuckNorris(Gun, SuperHero):
    def __init__(self, name='Chuck Norris', can_use_ultimate_attack=False):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)

    def attack(self):
        return self.fire_a_gun()
