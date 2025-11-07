#first name (markdaniel) last name (kuizon)

markdaniel_x = 0
markdaniel_y = 0

kuizon_x = 14
kuizon_y = 3

game_running = True

print(f"Find your last name at ({kuizon_x}, {kuizon_y})!")
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

    if markdaniel_x == kuizon_x and markdaniel_y == kuizon_y:
        print(f"Youu winn!! Congratss!!")
        game_running = False
