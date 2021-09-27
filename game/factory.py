from collections.abc import Callable

from typing import Any
from game.character import GameCharacter


characters_creation_funcs: dict[str, Callable[..., GameCharacter]] = {}

def register(character_type: str, creation_func: Callable[..., GameCharacter]):
    """Register a new game character type"""
    characters_creation_funcs[character_type] = creation_func

def unregister(character_type: str):
    characters_creation_funcs.pop(character_type, None)

def create(arguments: dict[str, Any]) -> GameCharacter:
    item_copy = arguments.copy()
    character_type = item_copy.pop("type")
    try:
        creation_fn = characters_creation_funcs[character_type]
        return creation_fn(**item_copy)
    except KeyError:
        raise ValueError(f"Unknown character {character_type!r}") from None
