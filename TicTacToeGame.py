import random
import os


def PlayerInputting(arr, PlayerName):
    inputting = 1
    print(f"{PlayerName}'s Turn - ",end="")
    while inputting == 1:
        ch = int(input())
        # if arr[ch - 1] == '1' or arr[ch - 1] == '2' or arr[ch - 1] == '3' or arr[ch - 1] == '4' or arr[ch - 1] == '5' or arr[ch - 1] == '6' or arr[ch - 1] == '7' or arr[ch - 1] == '8' or arr[ch - 1] == '9':
        if arr[ch - 1] == ' ':
            inputting = 0
            return ch
        else:
            print(f"Cell Already Acquired...Enter Again.....{PlayerName}'s Turn - ",end="")


def PlayerVsPlayer():
    filled = 0
    turn = 0
    # arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    arr = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    CLR()
    PlayerOne = input("Enter Player 1's Name - ")
    PlayerTwo = input("Enter Player 2's Name - ")
    print("\r")
    CLR()
    print(f"{PlayerOne} VS {PlayerTwo}")
    Board(arr)
    while filled != 9:
        if turn == 0:
            ch = PlayerInputting(arr, PlayerOne)
            arr[ch - 1] = 'X'
            CLR()
            Board(arr)
            if CheckForWin(arr, PlayerOne, PlayerTwo) == 1:
                break
            filled = filled + 1
            turn = 1
        elif turn == 1:
            ch = PlayerInputting(arr, PlayerTwo)
            arr[ch - 1] = 'O'
            CLR()
            Board(arr)
            if CheckForWin(arr, PlayerOne, PlayerTwo) == 1:
                break
            filled = filled + 1
            turn = 0

    if filled >= 9:
        print("Game Drawn")


def CheckIfCPUCanPlaceThereSoThatUserDoesntWins(arr):
    if arr[0] == arr[1] and arr[2] == ' ' and arr[0] == 'X':
        return 3
    elif arr[0] == arr[2] and arr[1] == ' ' and arr[0] == 'X':
        return 2
    elif arr[1] == arr[2] and arr[0] == ' ' and arr[1] == 'X':
        return 1
    elif arr[0] == arr[3] and arr[6] == ' ' and arr[0] == 'X':
        return 7
    elif arr[0] == arr[6] and arr[3] == ' ' and arr[0] == 'X':
        return 4
    elif arr[3] == arr[6] and arr[0] == ' ' and arr[3] == 'X':
        return 1
    elif arr[1] == arr[4] and arr[7] == ' ' and arr[1] == 'X':
        return 8
    elif arr[1] == arr[7] and arr[4] == ' ' and arr[1] == 'X':
        return 5
    elif arr[7] == arr[4] and arr[1] == ' ' and arr[7] == 'X':
        return 2
    elif arr[2] == arr[5] and arr[8] == ' ' and arr[2] == 'X':
        return 9
    elif arr[2] == arr[8] and arr[5] == ' ' and arr[2] == 'X':
        return 6
    elif arr[5] == arr[8] and arr[2] == ' ' and arr[5] == 'X':
        return 3
    elif arr[5] == arr[4] and arr[3] == ' ' and arr[5] == 'X':
        return 4
    elif arr[3] == arr[5] and arr[4] == ' ' and arr[5] == 'X':
        return 5
    elif arr[3] == arr[4] and arr[5] == ' ' and arr[3] == 'X':
        return 6
    elif arr[7] == arr[8] and arr[6] == ' ' and arr[7] == 'X':
        return 7
    elif arr[6] == arr[8] and arr[7] == ' ' and arr[6] == 'X':
        return 8
    elif arr[7] == arr[6] and arr[8] == ' ' and arr[6] == 'X':
        return 9
    elif arr[8] == arr[4] and arr[0] == ' ' and arr[8] == 'X':
        return 1
    elif arr[8] == arr[0] and arr[4] == ' ' and arr[0] == 'X':
        return 5
    elif arr[0] == arr[4] and arr[8] == ' ' and arr[0] == 'X':
        return 9
    elif arr[6] == arr[4] and arr[2] == ' ' and arr[4] == 'X':
        return 3
    elif arr[6] == arr[2] and arr[4] == ' ' and arr[6] == 'X':
        return 5
    elif arr[2] == arr[4] and arr[6] == ' ' and arr[2] == 'X':
        return 7
    else:
        return 0


def CpuVsPlayer():
    filled = 0
    turn = 0
    # arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    arr = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    PlayerOne = input("Enter Player 1's Name - ")
    PlayerTwo = "CPU"
    print("\r")
    CLR()
    print(f"\t{PlayerOne} VS {PlayerTwo}")
    Board(arr)
    while filled != 9:
        if turn == 0:
            ch = PlayerInputting(arr, PlayerOne)
            arr[ch - 1] = 'X'
            CLR()
            Board(arr)
            if CheckForWin(arr, PlayerOne, PlayerTwo) == 1:
                break
            filled = filled + 1
            turn = 1
        elif turn == 1:
            if CheckIfCPUCanPlaceThereSoThatUserDoesntWins(arr) == 0:
                ch = RandomGenerator(arr)
                print(f"{PlayerTwo}'s Turn - {ch}")
                arr[ch - 1] = 'O'
            else:
                ch = CheckIfCPUCanPlaceThereSoThatUserDoesntWins(arr)
                arr[ch - 1] = 'O'

            CLR()
            Board(arr)
            if CheckForWin(arr, PlayerOne, PlayerTwo) == 1:
                break
            filled = filled + 1
            turn = 0

    if filled >= 9:
        CLR()
        print("Draw..!!")


# def CheckIfCPUCanWinByPlacingThere(arr):
#     if arr[0] == arr[1] and arr[2] == ' ' and arr[0] == 'O':
#         return 3
#     elif arr[0] == arr[2] and arr[1] == ' ' and arr[0] == 'O':
#         return 2
#     elif arr[1] == arr[2] and arr[0] == ' ' and arr[1] == 'O':
#         return 1
#     elif arr[0] == arr[3] and arr[6] == ' ' and arr[0] == 'O':
#         return 7
#     elif arr[0] == arr[6] and arr[3] == ' ' and arr[0] == 'O':
#         return 4
#     elif arr[3] == arr[6] and arr[0] == ' ' and arr[3] == 'O':
#         return 1
#     elif arr[1] == arr[4] and arr[7] == ' ' and arr[1] == 'O':
#         return 8
#     elif arr[1] == arr[7] and arr[4] == ' ' and arr[1] == 'O':
#         return 5
#     elif arr[7] == arr[4] and arr[1] == ' ' and arr[7] == 'O':
#         return 2
#     elif arr[2] == arr[5] and arr[8] == ' ' and arr[2] == 'O':
#         return 9
#     elif arr[2] == arr[8] and arr[5] == ' ' and arr[2] == 'O':
#         return 6
#     elif arr[5] == arr[8] and arr[2] == ' ' and arr[5] == 'O':
#         return 3
#     elif arr[5] == arr[4] and arr[3] == ' ' and arr[5] == 'O':
#         return 4
#     elif arr[3] == arr[5] and arr[4] == ' ' and arr[5] == 'O':
#         return 5
#     elif arr[3] == arr[4] and arr[5] == ' ' and arr[3] == 'O':
#         return 6
#     elif arr[7] == arr[8] and arr[6] == ' ' and arr[7] == 'O':
#         return 7
#     elif arr[6] == arr[8] and arr[7] == ' ' and arr[6] == 'O':
#         return 8
#     elif arr[7] == arr[6] and arr[8] == ' ' and arr[6] == 'O':
#         return 9
#     elif arr[8] == arr[4] and arr[0] == ' ' and arr[8] == 'O':
#         return 1
#     elif arr[8] == arr[0] and arr[4] == ' ' and arr[8] == 'O':
#         return 5
#     elif arr[0] == arr[4] and arr[8] == ' ' and arr[0] == 'O':
#         return 9
#     elif arr[6] == arr[4] and arr[2] == ' ' and arr[6] == 'O':
#         return 3
#     elif arr[6] == arr[2] and arr[4] == ' ' and arr[6] == 'O':
#         return 5
#     elif arr[2] == arr[4] and arr[6] == ' ' and arr[2] == 'O':
#         return 7
#     else:
#         return 0


def CheckForWin(arr, PlayerOne, PlayerTwo):
    if arr[0] == arr[1] and arr[1] == arr[2] and arr[0] == 'X':
        print(f"{PlayerOne} Wins!")
        return 1
    elif arr[3] == arr[4] and arr[4] == arr[5] and arr[3] == 'X':
        print(f"{PlayerOne} Wins!")
        return 1
    elif arr[6] == arr[7] and arr[7] == arr[8] and arr[6] == 'X':
        print(f"{PlayerOne} Wins!")
        return 1
    elif arr[0] == arr[3] and arr[3] == arr[6] and arr[0] == 'X':
        print(f"{PlayerOne} Wins!")
        return 1
    elif arr[1] == arr[4] and arr[4] == arr[7] and arr[1] == 'X':
        print(f"{PlayerOne} Wins!")
        return 1
    elif arr[2] == arr[5] and arr[5] == arr[8] and arr[2] == 'X':
        print(f"{PlayerOne} Wins!")
        return 1
    elif arr[0] == arr[4] and arr[4] == arr[8] and arr[0] == 'X':
        print(f"{PlayerOne} Wins!")
        return 1
    elif arr[2] == arr[4] and arr[4] == arr[6] and arr[2] == 'X':
        print(f"{PlayerOne} Wins!")
        return 1
    elif arr[0] == arr[1] and arr[1] == arr[2] and arr[0] == 'O':
        print(f"{PlayerTwo} Wins!")
        return 1
    elif arr[3] == arr[4] and arr[4] == arr[5] and arr[3] == 'O':
        print(f"{PlayerTwo} Wins!")
        return 1
    elif arr[6] == arr[7] and arr[7] == arr[8] and arr[6] == 'O':
        print(f"{PlayerTwo} Wins!")
        return 1
    elif arr[0] == arr[3] and arr[3] == arr[6] and arr[0] == 'O':
        print(f"{PlayerTwo} Wins!")
        return 1
    elif arr[1] == arr[4] and arr[4] == arr[7] and arr[1] == 'O':
        print(f"{PlayerTwo} Wins!")
        return 1
    elif arr[2] == arr[5] and arr[5] == arr[8] and arr[2] == 'O':
        print(f"{PlayerTwo} Wins!")
        return 1
    elif arr[0] == arr[4] and arr[4] == arr[8] and arr[0] == 'O':
        print(f"{PlayerTwo} Wins!")
        return 1
    elif arr[2] == arr[4] and arr[4] == arr[6] and arr[2] == 'O':
        print(f"{PlayerTwo} Wins!")
        return 1
    else:
        return 0


def RandomGenerator(arr):
    Done = 0
    ch = 0
    while Done == 0:
        ch = random.randint(1,9)
        # if arr[ch - 1] == '1' or arr[ch - 1] == '2' or arr[ch - 1] == '3' or arr[ch - 1] == '4' or arr[ch - 1] == '5' or arr[ch - 1] == '6' or arr[ch - 1] == '7' or arr[ch - 1] == '8' or arr[ch - 1] == '9':
        if arr[ch - 1] == ' ':
            Done = 1
            break
    return ch


def Board(arr):
    print("\t\t _____________________________ ")
    print("\t\t|         |         |         |")
    print(f"\t\t|    {arr[0]}    |    {arr[1]}    |    {arr[2]}    |")
    print("\t\t|_________|_________|_________|")
    print("\t\t|         |         |         |")
    print(f"\t\t|    {arr[3]}    |    {arr[4]}    |    {arr[5]}    |")
    print("\t\t|_________|_________|_________|")
    print("\t\t|         |         |         |")
    print(f"\t\t|    {arr[6]}    |    {arr[7]}    |    {arr[8]}    |")
    print("\t\t|_________|_________|_________|")
    print("\r")


def Game():
    print("\r")
    print("_________WELCOME TO TIC TAC TOE GAME_________")
    print("CHOOSE FROM BELOW")
    print("1.) PLAYER VS PLAYER")
    print("2.) CPU VS PLAYER")
    choice = int(input("Enter Choice - "))
    if choice == 1:
        PlayerVsPlayer()
    else:
        CpuVsPlayer()


def CLR():
    os.system("CLS")


def LetsGoBro():
    WantToPlay = '1'
    while WantToPlay == '1':
        Game()
        print("\r\r")
        print("You want to play more - 1 for Yes any other button to quit.")
        WantToPlay = input()


LetsGoBro()
