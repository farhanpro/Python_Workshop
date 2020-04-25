from random import random
board = [' ' for x in range(10)]    
def InsertLetter(letter,pos):         
    board[pos] = letter

def SpaceIsfree(pos):
    return board[pos] == ' '

def PrintBoard(board):
    print('   |  |  ')
    print(' ' + board[1] + ' | ' + board[2] + '| ' + board[3])
    print('   |  |  ')
    print('---------')
    print('   |  |  ')
    print(' ' + board[4] + ' | ' + board[5] + '| ' + board[6])
    print('   |  |  ')
    print('---------')
    print('   |  |  ')
    print(' ' + board[7] + ' | ' + board[8] + '| ' + board[9])
    print('   |  |  ')

def IsBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def IsWinner(b,l):
    return(b[1] == l and b[2] == l and b[3] == l) or (
        b[4] == l and b[5] == l and b[6] == l) or (
        b[7] == l and b[8] == l and b[9] == l) or (
        b[1] == l and b[5] == l and b[9] == l)or (
        b[3] == l and b[5] == l and b[7] == l)or(
        b[1] == l and b[4] == l and b[7] == l)or(
        b[2] == l and b[5] == l and b[8] == l)or(
        b[3] == l and b[6] == l and b[9] == l)

def PlayerMove():
    run = True
    while run:
        move = input("Please Select a Position to  enter the X between 1 to 9")
        try:
            move = int(move)
            if (move > 0) and  (move < 10):
                    if SpaceIsfree(move):
                        run = False
                        InsertLetter('X',move)
                    else:
                        print("Sorry, this space is occupied")
            else:
                print("Please type a number between  1 and 9")
        except:
            print("Please type a number")

def ComputerMove():
    PossibleMoves = [ x for x , letter in enumerate(board) if letter == ' ' and  x != 0]
    Move = 0

    for let in ['O' , 'X']:
        for i in PossibleMoves:
            BoardCopy = board[:]
            BoardCopy[i] = let
            if IsWinner(BoardCopy,let):
                Move = i
                return Move

    CornerOpen = [] 
    for  i in PossibleMoves:
        if i in [1,3,7,9]:
            CornerOpen.append(i)

    if len(CornerOpen) > 0:
        Move = selectRandom(CornerOpen)
        return Move
        
    if 5 in PossibleMoves:
        Move = 5
        return Move

    EdgesOpen = []
    for i in PossibleMoves:
        if i  in [2,4,6,8]:
            EdgesOpen.append(i)
    
    if len(EdgesOpen) > 0:
        Move = selectRandom(EdgesOpen)
        return