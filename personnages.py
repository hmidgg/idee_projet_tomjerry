from abc import ABC, abstractmethod

# Définition de la classe abstraite Personnage
class Personnage(ABC):
    def __init__(self, nom, energie=100):
        self.nom = nom
        self.energie = energie

    @property
    @abstractmethod
    def espece(self):
        pass

    @abstractmethod
    def repaire(self):
        pass

    def est_hors_jeu(self):
        return self.energie <= 0

    def subir(self, degats):
        self.energie = max(0, self.energie - degats)

    def se_presenter(self):
        return f"Je suis {self.nom} ({self.espece}), mon repaire : {self.repaire()}."

    def __str__(self):
        return f"{self.nom} ({self.espece}, énergie={self.energie})"

# Définition de la classe fille Jerry
class Jerry(Personnage):
    espece = "souris"

    def __init__(self, energie=100):
        super().__init__("Jerry", energie)

    def repaire(self):
        return "le trou du mur"


# Définition de la classe fille Tuffy

class Tuffy(Personnage):
    espece = "souris"

    def __init__(self, energie=100):
        super().__init__("Tuffy", energie)

    def repaire(self):
        return "la boîte à biscuits"

# Définition de la classe fille Spike
class Spike(Personnage):
    espece = "chien"

    def __init__(self, energie=100):
        super().__init__("Spike", energie)

    def repaire(self):
        return "la niche"


class Fantome(Personnage):
    def repaire(self):
        return "le vieux manoir"