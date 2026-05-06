import random
import sys
import time

CSI = "\033["
RESET = "\033[0m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BRIGHT_YELLOW = "\033[93m"
RED = "\033[31m"
BROWN = "\033[38;5;130m"


def build_tree_lines(height, star_on, ornament_mask=None):
    width = height * 2 - 1
    tree = []

    # Star: alternate between bright and regular yellow
    star_color = BRIGHT_YELLOW if star_on else YELLOW
    tree.append(" " * (height - 1) + star_color + "*" + RESET + " " * (height - 1))

    # Tree layers with colored leaves and ornaments
    if ornament_mask is None:
        ornament_mask = set()

    for level in range(height):
        leaves = []
        for pos in range(2 * level + 1):
            if (level, pos) in ornament_mask:
                leaves.append(RED + "o" + RESET)
            else:
                leaves.append(GREEN + "*" + RESET)
        padding = " " * (height - level - 1)
        tree.append(padding + "".join(leaves) + padding)

    # Trunk
    trunk_width = 3 if height >= 3 else 1
    trunk_padding = " " * ((width - trunk_width) // 2)
    for _ in range(2):
        tree.append(trunk_padding + BROWN + "#" * trunk_width + RESET + trunk_padding)

    return tree


def generate_ornament_mask(height, count):
    positions = []
    for level in range(1, height):
        for pos in range(2 * level + 1):
            if pos % 2 == 0:
                positions.append((level, pos))

    return set(random.sample(positions, min(count, len(positions))))


def print_dynamic_tree(height=8, frames=30, delay=0.15):
    ornament_count = max(3, height)
    for frame in range(frames):
        star_on = frame % 2 == 0
        ornament_mask = generate_ornament_mask(height, ornament_count)
        tree_lines = build_tree_lines(height, star_on, ornament_mask)
        sys.stdout.write(CSI + "2J" + CSI + "H")
        sys.stdout.write("\n".join(tree_lines) + "\n")
        sys.stdout.flush()
        time.sleep(delay)

    # Keep final frame on screen
    sys.stdout.write(CSI + "H")
    sys.stdout.write("\n".join(build_tree_lines(height, True, generate_ornament_mask(height, ornament_count))) + "\n")
    sys.stdout.flush()


if __name__ == "__main__":
    try:
        print_dynamic_tree(8, frames=60, delay=0.12)
    except KeyboardInterrupt:
        sys.stdout.write(RESET + "\n")
        sys.stdout.flush()
