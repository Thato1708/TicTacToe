def main():
    print("Tic Tac Toe")
    display_grid()
    start_game()

def start_game():
    game_end=False
    while not game_end:
        game_end=take_turn()
    print()
    print("Game Over")

#This is where we decide the winner

def take_turn():
    turn=1
    while True:
        if not turn%2==0:
            symbol="X"
        else:
            symbol="O"
        print(f"{symbol}'s turn")

        row=int(input("Choose row (1, 2, 3):"))
        if row < 1 or row > 3:
            print("Invalid row number. Please Try again")
            continue
        column=int(input("Choose a column (1, 2, 3):"))
        if column <1 or column > 3:
            print("Invalid column number. Please Try again")
            continue

        if not grid[row-1][column-1]==" ":
            print("This place is already occupied. Please Try again.")
            continue
        
        grid[row-1][column-1] = symbol
        display_grid()

        winner=display_winner()
        if winner == "X" or winner == "O":
            print(f"{winner} wins this game!")
            game_end=True
            return game_end
        
        if turn ==9: 
            print("Draw!")
            game_end=True
            return game_end
        
        turn += 1

#Drawing the game grid

grid = [[' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']]

def display_grid():
    print()
    print("+--+--+--+")
    for row in grid:
        print("|",end="")
        for column in row:
            print(f"{column} |", end="")
        print()
        print("+--+--+--+")
    print()

#Determining the winner

def display_winner():
    #rows
    for x in range(3):
        if grid[x][0]== grid[x][1] == grid[x][2]:
            return grid[x][0]

    #columns
    for y in range(3):
        if grid[0][y] == grid [1][y] == grid[2][y]:
            return grid[0][y]

    #diagonal 1
    if grid[0][0] == grid[1][1] == grid[2][2]:
        return grid[0][0]

    #diagonal 2
    if grid[0][2] == grid[1][1] == grid[2][0]:
        return grid[0][2]

    #no winner
    return " "


if __name__ == "__main__":
    main()
