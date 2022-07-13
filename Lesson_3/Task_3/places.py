from abc import ABC, abstractmethod


class Place(ABC):
    @abstractmethod
    def antagonist_maker(self):
        pass


# -------------------------------------------------
class Kostroma(Place):
    city_name = 'Kostroma'

    def get_orcs(self):
        print('Orcs hid in the forest')  # easter egg detected

    def antagonist_maker(self):
        self.get_orcs()


class Tokyo(Place):
    name = 'Tokyo'

    def get_godzilla(self):
        print('Godzilla stands near a skyscraper')

    def antagonist_maker(self):
        self.get_godzilla()

