from personnages import Fantome, Jerry, Personnage, Spike, Tuffy


def main():
    try:
        Personnage("X")
    except TypeError as erreur:
        print(f"Erreur : {erreur}")
        print(
            "Python refuse car Personnage est abstraite : "
            "ses méthodes espece et repaire doivent être implémentées."
        )

    print(f"Méthodes abstraites de Fantome : {Fantome.__abstractmethods__}")
    try:
        Fantome()
    except TypeError as erreur:
        print(f"Impossible de créer Fantome : {erreur}")

    for personnage in (Jerry(), Tuffy(), Spike()):
        print(personnage.se_presenter())
    print(
        "Le résultat varie grâce au polymorphisme : "
        "espece et repaire sont définies par chaque sous-classe."
    )

    j = Jerry()
    j.subir(30)
    print(j)
    j.subir(500)
    print(j.est_hors_jeu())


if __name__ == "__main__":
    main()