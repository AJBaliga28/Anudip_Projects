def sum(a, b, c):
    """
    Calculates the sum of three numbers.

    Args:
        a (int): First number.
        b (int): Second number.
        c (int): Third number.

    Returns:
        int: Sum of the three numbers.
    """
    return a + b + c

def printBoard(xState, yState):
    """
    Prints the Tic-Tac-Toe board.

    Args:
        xState (list): List representing the X player's moves.
        yState (list): List representing the O player's moves.
    """
    print("\n")
    # Mapping the X and O states to the board positions
    positions = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    for i in range(3):
        row = [positions[i*3], positions[i*3+1], positions[i*3+2]]
        print(" | ".join(['X' if xState[pos] else ('O' if yState[pos] else str(pos)) for pos in row]))
        if i < 2:
            print("--|---|--")

def checkWin(xState, yState):
    """
    Checks if there is a winner in the Tic-Tac-Toe game.

    Args:
        xState (list): List representing the X player's moves.
        yState (list): List representing the O player's moves.

    Returns:
        int: 1 if X wins, 0 if O wins, -1 if no winner.
    """
    winConditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in winConditions:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("\nX won!\n")
            return 1
        if sum(yState[win[0]], yState[win[1]], yState[win[2]]) == 3:
            print("\nO won!\n")
            return 0
    return -1

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    yState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    turn = 1 # 1 for X and 0 for O
    print("Welcome!\n")

    while(True):
        printBoard(xState, yState)
        
        if turn == 1:
            print("\nX plays!")
            value = int(input("Enter a value: "))
            if xState[value] == 1 or yState[value] == 1:
                print("Position already taken. Try again!")
                continue
            xState[value] = 1
        else:
            print("O plays!")
            value = int(input("Enter a value: "))
            if xState[value] == 1 or yState[value] == 1:
                print("Position already taken. Try again!")
                continue
            yState[value] = 1
            
        cWin = checkWin(xState, yState)
        if cWin != -1:
            print("Match over!")
            break
        turn = 1 - turn
