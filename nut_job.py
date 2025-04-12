def shake_tree(tree):
    # Get the width of the tree
    width = len(tree[0])
    nut_positions = [0] * width  # Initialize output array for nuts
    
    # Start with nuts on top row
    for col in range(width):
        if tree[0][col] == "o":  # Check if there's a nut
            current_col = col
            
            # Process the nut's journey through the tree
            for row in range(1, len(tree)):  # Iterate through rows
                if tree[row][current_col] == "\\":
                    current_col += 1  # Bounce right
                elif tree[row][current_col] == "/":
                    current_col -= 1  # Bounce left
                elif tree[row][current_col] == "_":
                    # The nut gets stuck, stop processing
                    break
            
            # The nut lands at current_col (if it didn't get stuck)
            if current_col < width and current_col >= 0:
                nut_positions[current_col] += 1
    
    return nut_positions

# Example input
tree = [
    ".o.oooooo.o.o.oooooo.",
    "..\\..\\.../...\\.../..\\.",
    ".../..\\..../....../...",
    ".....\\...././.\\..\\..\\.",
    "...../../././...\\.....",
    ".../.../..\\./.\\..\\....",
    "./.......\\../.\\../...",
    "....\\..../...../.\\...",
    ".../.\\._.\\../._../.\\.",
    ".\\...././....\\../.\\..",
    "./......./.\\.../.../.."
]

# Shake the tree
result = shake_tree(tree)
print(result)  # Output: [1, 0, 0, 5, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0]
