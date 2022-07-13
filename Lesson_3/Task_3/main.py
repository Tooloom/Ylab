from typing import Union

from heroes import Superman, ChuckNorris
from places import Kostroma, Tokyo
from media import Media


def save_the_place(hero: Union[Superman, ChuckNorris], place: Union[Kostroma, Tokyo], news):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    news.create_news(hero, place)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma(), Media)
    print('-' * 20)
    save_the_place(ChuckNorris(), Tokyo(), Media)
