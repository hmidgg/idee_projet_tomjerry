from interfaces import Butch, Chat, Fuyard, Poursuivant, Tom, roles
from personnages import Jerry, Personnage


def main():
    try:
        Chat("Felix")
    except TypeError as erreur:
        print(f"Chat('Felix') : {erreur}")
    print(f"Chat.__abstractmethods__ : {Chat.__abstractmethods__}")

    tom = Tom()
    butch = Butch()
    print(
        "Tom est Chat, Personnage, Poursuivant et Fuyard :",
        isinstance(tom, Chat)
        and isinstance(tom, Personnage)
        and isinstance(tom, Poursuivant)
        and isinstance(tom, Fuyard),
    )
    print(f"roles(Tom()) : {roles(tom)}")
    print(f"roles(Butch()) : {roles(butch)}")

    cible = Jerry()
    print(f"Tom().poursuivre(Jerry()) : {tom.poursuivre(cible)}")
    print(f"Énergie de Jerry après la poursuite : {cible.energie}")
    print(f"Tom().esquiver(50) : {Tom().esquiver(50)}")
    print(f"Tom().esquiver(10) : {Tom().esquiver(10)}")
    print(f"Tom.__mro__ : {Tom.__mro__}")
    print(
        "Sans esquiver(), Tom resterait abstraite ; la création de la classe "
        "serait permise, mais Tom() lèverait une TypeError."
    )


if __name__ == "__main__":
    main()
