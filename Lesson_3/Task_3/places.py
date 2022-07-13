from abc import ABC, abstractmethod


class Place(ABC):
    @abstractmethod
    def antagonist_maker(self):
        pass


# -------------------------------------------------
class Kostroma(Place):
    name = 'Kostroma'

    @staticmethod
    def get_orcs():
        print('Orcs hid in the forest')  # easter egg detected

    def antagonist_maker(self):
        self.get_orcs()


class Tokyo(Place):
    name = 'Tokyo'

    @staticmethod
    def get_godzilla():
        print('Godzilla stands near a skyscraper')

    def antagonist_maker(self):
        self.get_godzilla()

