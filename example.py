import json

from dataclasses import dataclass
from pyramda import map as pmap

from game import factory
from game import loader



@dataclass
class Sorcerer:
    name: str

    def make_a_noise(self) -> None:
        print("Aaaargh!")


@dataclass
class Wizard:
    name: str

    def make_a_noise(self) -> None:
        print("Wizz!")


@dataclass
class Witcher:
    name: str

    def make_a_noise(self) -> None:
        print("hmmm")


def main() -> None:

    factory.register("sorcerer", Sorcerer)
    factory.register("wizard", Wizard)
    factory.register("witcher", Witcher)

    with open("./level.json", encoding="utf-8") as file:
        data = json.load(file)
        loader.load_plugins(data["plugins"])

        characters = [factory.create(item) for item in data["characters"]]
        print(characters)

        pmap(lambda c: c.make_a_noise(), characters)
        # for character in characters:
        #     print(character, end="\t")
        #     character.make_a_noise()


if __name__ == "__main__":
    # execute only if run as a script
    main()
