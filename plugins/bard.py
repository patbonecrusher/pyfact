
from dataclasses import dataclass
from game import factory


@dataclass
class Bard:
    name: str
    instrument: str = "flute"
    def make_a_noise(self) -> None:
        print(f"toss a coin to your witcher ! {self.instrument}")

def initialize() -> None:
    factory.register("bard", Bard)
