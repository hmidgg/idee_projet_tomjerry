from abc import ABC, abstractmethod

from personnages import Personnage


class Poursuivant(ABC):
    @abstractmethod
    def poursuivre(self, cible):
        pass


class Fuyard(ABC):
    @abstractmethod
    def esquiver(self, degats):
        pass


class Gadget(ABC):
    pass


class Chat(Personnage):
    espece = "chat"

    def __init__(self, nom, energie=100):
        super().__init__(nom, energie)


class Tom(Chat, Poursuivant, Fuyard):
    def __init__(self, energie=100):
        super().__init__("Tom", energie)

    def repaire(self):
        return "la maison de Tom"

    def poursuivre(self, cible):
        degats = 30
        cible.subir(degats)
        return degats

    def esquiver(self, degats):
        degats_subis = max(0, degats - 15)
        self.subir(degats_subis)
        return degats_subis


class Butch(Chat, Poursuivant):
    def __init__(self, energie=100):
        super().__init__("Butch", energie)

    def repaire(self):
        return "la maison de Butch"

    def poursuivre(self, cible):
        degats = 30
        cible.subir(degats)
        return degats


def roles(personnage):
    interfaces = (Poursuivant, Fuyard, Gadget)
    return [interface.__name__ for interface in interfaces if isinstance(personnage, interface)]