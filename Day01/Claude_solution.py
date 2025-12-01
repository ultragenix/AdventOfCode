"""
Advent of Code 2025 - Day 01 Solution
Version optimisée avec opérateur modulo
"""
input_path = "/home/genix/Workspace/AdventOfCode/Day01/input.txt"


def rotate(position, command):
    """
    Applique une rotation sur une piste circulaire de 100 positions (0-99).

    Args:
        position: Position actuelle (0-99)
        command: Commande (ex: 'L5' ou 'R3')

    Returns:
        Nouvelle position après rotation
    """
    direction = command[0]
    steps = int(command[1:])

    if direction == 'L':
        # Rotation gauche = soustraction
        return (position - steps) % 100
    else:  # direction == 'R'
        # Rotation droite = addition
        return (position + steps) % 100


# Exécution
position = 50
zero_count = 0

with open(input_path) as f:
    for line in f:
        position = rotate(position, line.strip())
        if position == 0:
            zero_count += 1

print(f'La solution est : {zero_count}')
