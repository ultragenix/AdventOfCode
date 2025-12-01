def rotationLeft(current_position, number_rotation):
    """
    Rotate left (counter-clockwise) on the circular track.

    Args:
        current_position: Current position (0-99)
        number_rotation: Number of steps to rotate left

    Returns:
        New position after rotating left
    """

    zero_count = 0
    # Rotate left the specified number of times
    for _ in range(number_rotation):
        current_position -= 1

        if current_position == 0:
            zero_count += 1

        # Wrap around: if position goes below 0, jump to 99
        if current_position == -1:
            current_position = 99

    return current_position, zero_count


position, zero_count = rotationLeft(50, 51)

print(f'on est a la position {position}')
print(f'on est passé  {zero_count} fois sur le zéro')
