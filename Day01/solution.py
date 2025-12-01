"""
Advent of Code 2025 - Day 01 Solution
Circular position tracker with rotation commands

The puzzle involves tracking a position on a circular track (0-99)
starting at position 50. Commands like 'L5' or 'R3' rotate left/right
by the specified number of steps. Count how many times position 0 is reached.
"""

# Input file path containing rotation commands (L/R followed by number)
input_path = "/home/genix/Workspace/AdventOfCode/Day01/input.txt"


def rotationCall(current_position, selected_input):
    """
    Parse and execute a rotation command.

    Args:
        current_position: Current position on the circular track (0-99)
        selected_input: Command string starting with 'L' or 'R' followed by a number

    Returns:
        New position after rotation
    """
    # Check if command is a left rotation (e.g., 'L5')
    if selected_input.startswith("L"):
        number_rotation = int(selected_input[1:])  # Extract number after 'L'
        new_position = rotationLeft(current_position, number_rotation)

    # Check if command is a right rotation (e.g., 'R3')
    if selected_input.startswith("R"):
        number_rotation = int(selected_input[1:])  # Extract number after 'R'
        new_position = rotationRight(current_position, number_rotation)

    return new_position


def rotationLeft(current_position, number_rotation):
    """
    Rotate left (counter-clockwise) on the circular track.

    Args:
        current_position: Current position (0-99)
        number_rotation: Number of steps to rotate left

    Returns:
        New position after rotating left
    """
    # Rotate left the specified number of times
    for _ in range(number_rotation):
        current_position -= 1
        # Wrap around: if position goes below 0, jump to 99
        if current_position == -1:
            current_position = 99

    return current_position


def rotationRight(current_position, number_rotation):
    """
    Rotate right (clockwise) on the circular track.

    Args:
        current_position: Current position (0-99)
        number_rotation: Number of steps to rotate right

    Returns:
        New position after rotating right
    """
    # Rotate right the specified number of times
    for _ in range(number_rotation):
        current_position += 1
        # Wrap around: if position reaches 100, jump to 0
        if current_position == 100:
            current_position = 0

    return current_position


# Main puzzle execution
# Starting position for the puzzle
current_position = 50

# Counter for how many times we reach position 0
solution = 0

# Read and process each rotation command from input file
with open(input_path) as f:
    for line in f:
        # Execute the rotation command and update position
        current_position = rotationCall(current_position, line)
        print(current_position)

        # Increment counter each time we reach position 0
        if current_position == 0:
            solution += 1

# Display the final answer
print(f'la solution est :{solution}')
