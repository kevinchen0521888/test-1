def print_christmas_tree(height=6):
    tree = []
    width = height * 2 - 1

    # Star
    tree.append(" " * (height - 1) + "*" + " " * (height - 1))

    # Tree layers
    for level in range(height):
        leaves = "*" * (2 * level + 1)
        padding = " " * (height - level - 1)
        tree.append(padding + leaves + padding)

    # Trunk
    trunk_width = 3 if height >= 3 else 1
    trunk_padding = " " * ((width - trunk_width) // 2)
    for _ in range(2):
        tree.append(trunk_padding + "#" * trunk_width + trunk_padding)

    print("\n".join(tree))

if __name__ == "__main__":
    print_christmas_tree(8)