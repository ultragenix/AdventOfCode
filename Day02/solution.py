"""
Advent of Code 2025 - Day 02 Solution
Problem: Find all IDs within given ranges that have an even number of digits
         and where the first half equals the second half.

Example: 123123 is valid (6 digits, "123" == "123")
         1234 is not valid (4 digits, but "12" != "34")
"""

input_path = "/home/genix/Workspace/AdventOfCode2025/Day02/input.txt"

# Liste pour stocker les ranges d'IDs à analyser
my_input = []

# Lecture du fichier d'entrée
# Le fichier contient des ranges séparés par des virgules (ex: "1-10,20-30")
with open(input_path) as f:
    for line in f:
        my_input = line.split(',')


def has_matching_halves(number_str):
    """
    Vérifie si un nombre (sous forme de string) a ses deux moitiés identiques.

    Args:
        number_str (str): Le nombre à vérifier sous forme de string

    Returns:
        bool: True si les deux moitiés sont identiques, False sinon

    Example:
        has_matching_halves("123123") -> True
        has_matching_halves("1234") -> False
    """
    midpoint = len(number_str) // 2
    first_half = number_str[:midpoint]
    second_half = number_str[midpoint:]

    return first_half == second_half


def check_valid_id(id_number):
    """
    Vérifie si un ID est valide selon les critères du problème.
    Un ID est valide si ses deux moitiés sont identiques.

    Args:
        id_number (int): L'ID à vérifier

    Returns:
        int: L'ID lui-même s'il est valide, 0 sinon
    """
    if has_matching_halves(str(id_number)):
        return id_number
    else:
        return 0


# Liste pour accumuler tous les IDs valides trouvés
valid_ids = []


def find_valid_id(candidate_id):
    """
    Vérifie si un ID candidat est valide et l'ajoute à la liste globale si c'est le cas.
    Un ID doit avoir un nombre pair de chiffres pour être considéré.

    Args:
        candidate_id (int): L'ID à analyser
    """
    num_digits = len(str(candidate_id))

    # Vérifier si le nombre a un nombre pair de chiffres
    if num_digits % 2 == 0:
        validated_id = check_valid_id(candidate_id)

        # Si l'ID est valide (> 0), l'ajouter à la liste
        if validated_id > 0:
            valid_ids.append(validated_id)


def process_ranges(ranges_array):
    """
    Parcourt tous les ranges d'IDs et vérifie chaque ID dans chaque range.

    Args:
        ranges_array (list): Liste des ranges sous forme de strings "start-end"

    Example:
        process_ranges(["1-100", "200-300"])
    """
    for range_str in ranges_array:
        # Séparer le range en début et fin
        parts = range_str.split("-")
        range_start = int(parts[0])
        range_end = int(parts[1])

        # Analyser chaque ID dans le range (inclusif)
        for id_to_check in range(range_start, range_end + 1):
            find_valid_id(id_to_check)


# Exécution principale
# Traiter tous les ranges d'IDs
process_ranges(my_input)

# Calculer la somme de tous les IDs valides trouvés
solution = sum(valid_ids)

# Afficher le résultat
print(f'La solution de la partie 1 du jour 2 est : {solution}')


# ============================================================================
# ANALYSE DE PERFORMANCE ET SOLUTION OPTIMISÉE
# ============================================================================
# Note: La solution ci-dessus parcourt tous les nombres dans chaque range,
# ce qui peut être très lent pour de grands ranges.
#
# Solution optimisée possible:
# Au lieu de tester chaque nombre, on pourrait générer directement les nombres
# valides en construisant uniquement les nombres où les deux moitiés sont égales.
# Exemple: pour les nombres à 6 chiffres, générer 100100, 101101, etc.
