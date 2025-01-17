from dataclasses import dataclass

from .interfaces import IOInterface


@dataclass
class OutputStruct:
    headline: str
    description: str


class Output(IOInterface):
    output_string = []

    def __init__(self, headline: str = None, description: str = None) -> None:
        self._headline = headline
        self._description = description

    def headline(self, headline: str = None):
        if headline:
            self._headline = headline

        self.output_string.append(self._headline)

        return self

    def description(self, description: str = None):
        if description:
            self._description = description

        self.output_string.append(self._description)

        return self

    def display(self) -> str:
        return "\n".join(self.output_string)
