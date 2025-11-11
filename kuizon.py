#first name (markdaniel) last name (kuizon)
print("Welcome to Kuizon's Maze")

markdaniel_x = 0
markdaniel_y = 0

treasure_x = 14
treasure_y = 3

game_running = True

print(f"Find the treasure at ({treasure_x}, {treasure_y})!")
while game_running:
    move = input("Enter move (w/a/s/d or Q to quit): ").lower()

    if move == "w":
        markdaniel_x += 1
    elif move == "s":
        markdaniel_x += 1
    elif move == "a":
        markdaniel_y += 1
    elif move == "d":
        markdaniel_y += 1
    elif move == "q":
        print("Game Exited.")
        break
    else:
        print("Invalid move! Use W, A, S, D, or Q only.")
        continue

    print(f"Player position: ({markdaniel_x}, {markdaniel_y})")

    if markdaniel_x == treasure_x and markdaniel_y == treasure_y:
        print(f"CONGRATSS! YOU FOUND THE TREASURE!!! You're richh  now!!")
        game_running = False
