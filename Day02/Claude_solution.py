input_path = "/home/genix/Workspace/AdventOfCode2025/Day02/input.txt"


def charger_input(path):
    with open(path) as f:
        return f.read().strip().split(',')


def est_nombre_valide(nombre):
    """Vérifie si un nombre a un nombre pair de digits et si ses deux moitiés sont identiques"""
    str_nombre = str(nombre)
    nb_digits = len(str_nombre)

    # Nombre impair de digits = invalide
    if nb_digits % 2 != 0:
        return False

    # Vérifier si les deux moitiés sont identiques
    milieu = nb_digits // 2
    return str_nombre[:milieu] == str_nombre[milieu:]


def extraire_range(range_str):
    """Extrait start et end d'une string '220067-226752'"""
    debut, fin = range_str.split("-")
    return int(debut), int(fin)


def trouver_nombres_valides(ranges):
    """Trouve tous les nombres valides dans les ranges données"""
    nombres_valides = []

    for range_str in ranges:
        debut, fin = extraire_range(range_str)

        for nombre in range(debut, fin + 1):
            if est_nombre_valide(nombre):
                nombres_valides.append(nombre)

    return nombres_valides


# Exécution
my_input = charger_input(input_path)
nombres_valides = trouver_nombres_valides(my_input)
solution = sum(nombres_valides)

print(f'Nombres valides trouvés: {len(nombres_valides)}')
print(f'Solution partie 1 jour 2: {solution}')
