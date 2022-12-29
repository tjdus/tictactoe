import pygame
import random

WIDTH = 600
HEIGHT = 700

length = 150

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')
font= pygame.font.SysFont(font_name, 150, False, False)
tfont = pygame.font.SysFont(font_name, 150, False, False)

def DrawBoard(board):
    for i in range(2):
        for j in range(3):
            pygame.draw.line(screen, BLACK, [75+j*length, 150+ (i+1)*length], [75+(j+1)*length, 150 + (i+1)*length], 4)
            pygame.draw.line(screen, BLACK, [75+(i+1)*length, 150+ j*length], [75+(i+1)*length, 150 + (j+1)*length], 4)
    for i in range(3):
        for j in range(3):
            b= font.render(board[i*3+j], True, BLACK)
            screen.blit(b, [110+i*length, 180+j*length])

            
def makeMove(board, letter, move):
    board[move] = letter

def IsEmpty(board, move):
    return board[move]== ' '

def GetBoardCopy(board):
    boardCopy=[]
    for i in board:
        boardCopy.append(i)
    return boardCopy

def Result(board, letter):
    return (board[6] == board[7] and board[7]==board[8] and board[8] == letter) or \
    (board[0] == board[1] and board[1]==board[2] and board[2] == letter) or \
    (board[3] == board[4] and board[4]==board[5] and board[5] == letter) or \
    (board[6] == board[3] and board[3]==board[0] and board[0] == letter) or \
    (board[7] == board[4] and board[4]==board[1] and board[1] == letter) or \
    (board[8] == board[5] and board[2]==board[5] and board[5] == letter) or \
    (board[6] == board[4] and board[4]==board[2] and board[2] == letter) or \
    (board[8] == board[4] and board[4]==board[0] and board[0] == letter) or \
    (board[6] == board[7] and board[7]==board[8] and board[8] == letter) 

def GetPlayerMove(board):
    move = 10
    while True:
        while move==10:
            for event in pygame.event.get():
                '''
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        move= 1
                    elif event.key == pygame.K_2:
                        move= 2
                    elif event.key == pygame.K_3:
                        move= 3
                    elif event.key == pygame.K_4:
                        move= 4
                    elif event.key == pygame.K_5:
                        move= 5
                    elif event.key == pygame.K_6:
                        move= 6
                    elif event.key == pygame.K_7:
                        move= 7
                    elif event.key == pygame.K_8:
                        move= 8
                    elif event.key == pygame.K_9:
                        move= 9
                    else:
                        move==10
                '''
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    if x>=75 and x<=525 and y>=150 and y<=600:
                        if x<225:
                            if y<300:
                                move=7
                            elif y<450:
                                move=4
                            else:
                                move=1
                        elif x<375:
                            if y<300:
                                move=8
                            elif y<450:
                                move=5
                            else:
                                move=2
                        else:
                            if y<525:
                                move=9
                            elif y<450:
                                move=6
                            else:
                                move=3
                    else:
                        move= 10        
                
        if IsEmpty(board, move-1):
            return move-1
        else:
            move=10
            
            
def RandomMove(board, movelist):
    moves=[]
    for i in movelist:
        if IsEmpty(board, i):
            moves.append(i)
    if len(moves) != 0:
        return random.choice(moves)
    else:
        return None
            
def GetComputerMove(board, computer):
    if computer == 'O':
        player= 'X'
    else:
        player = 'O'
        
    for i in range(9):
        boardCopy = GetBoardCopy(board)
        if IsEmpty(boardCopy, i):
            makeMove(boardCopy,computer, i)
            if Result(boardCopy, computer):
                return i
    for i in range(9):
        boardCopy=GetBoardCopy(board)
        if IsEmpty(boardCopy, i):
            makeMove(boardCopy, player, i)
            if Result(boardCopy, player):
                return i
    move= RandomMove(board, [0,2,6,8])
    if move!= None:
        return move
    if IsEmpty(board, 4):
        return 4
    
    return RandomMove(board, [1,3,5,7])


def IsBoardFull(board):
    for i in range(9):
        if IsEmpty(board, i):
            return False
    return True

done = False

board=[' '] * 9


# 게임 반복 구간
while not done:
    screen.fill(WHITE)
    # 이벤트 반복 구간
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    player = 'O'
    computer = 'X'
    
    turn = 'player'
    gameIsplaying =True
    while gameIsplaying:
        if turn == 'player':
            move = GetPlayerMove(board)
            makeMove(board, player, move)
            
            if Result(board, player):
                DrawBoard(board)
                text = tfont.render("You Win!", True, RED)
                screen.blit(text, [50, 50])
                gameIsplaying = False
    
            else:
                if IsBoardFull(board):
                    DrawBoard(board)   
                    text = tfont.render("Tie!", True, RED)
                    screen.blit(text, [200, 50])
                    break
                else:
                    turn = 'computer'
        else:
            move= GetComputerMove(board, computer)
            makeMove(board, computer, move)
            
            if Result(board, computer):
                DrawBoard(board)
                text = tfont.render("You Lose!", True, RED)
                screen.blit(text, [50, 50])
                gameIsplaying=False
            else:
                if IsBoardFull(board):
                    DrawBoard(board)
                    text = tfont.render("Tie!", True, RED)
                    screen.blit(text, [200, 50])
                    break
                else:
                    turn = 'player'

    # 윈도우 화면 채우기
    
    DrawBoard(board)
    # 화면에 텍스트 표시

    # 화면 업데이트
    pygame.display.flip()

    # 초당 60 프레임으로 업데이트
    clock.tick(60)

# 게임 종료
pygame.quit()
