from dataclasses import dataclass

from .interfaces import IOInterface


@dataclass
class UserInputStruct:
    headline: str
    description: str
    data: str


class Input(IOInterface):
    def __init__(self, headline: str = None, description: str = None, data: str = None) -> None:
        self._headline = headline
        self._description = description
        self._data = data

    def headline(self, headline: str = None):
        if headline:
            self._headline = headline

        return self

    def description(self, description: str = None):
        if description:
            self._description = description

        return self

    def display(self):
        pass

    def prompt(self) -> str:
        return input(f"{self._headline}\n{self._description}: ")
