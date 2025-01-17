import os
from abc import ABC, abstractmethod


class IOInterface(ABC):
    def clear(self):
        """Clear the terminal screen"""

        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

        return self

    @abstractmethod
    def headline(self, headline: str = None):
        pass

    @abstractmethod
    def description(self, description: str = None):
        pass

    @abstractmethod
    def display(self) -> str:
        pass
