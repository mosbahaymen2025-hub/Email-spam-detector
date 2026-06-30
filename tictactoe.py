board = [' ' for _ in range(9)]

def print_board():
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]} ")
    print ("\n")
    print(f"{board[3]} | {board[4]} | {board[5]} ")
    print ("\n")
    print(f"{board[6]} | {board[7]} | {board[8]} ")
    print ("\n")


#def check_winner(player):
#    test = False
#    if (board[0] == player and board[1] == player and board[2] == player ):
 #       test = True
  #  elif (board[3] == player and board[4] == player and board[5] == player ):
   #     test = True
    #elif (board[6] == player and board[7] == player and board[8] == player ):
    #    test = True
    #elif (board[0] == player and board[3] == player and board[6] == player ):        bad solution too complexe  !!!!
    #    test = True 
    #elif (board[1] == player and board[4] == player and board[7] == player ):
    #    test = True
    #elif (board[2] == player and board[5] == player and board[8] == player ):
    #    test = True
    #elif (board[0] == player and board[4] == player and board[8] == player ):
    #    test = True
    #elif (board[2] == player and board[4] == player and board[6] == player ):
    #    test = True
    #return test
def check_winner(player):
    test = False
    winning_combination = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for this_comb in winning_combination:
            if player == board[this_comb[0]] and player == board[this_comb[1]] and player == board[this_comb[2]]:
                test = True
    return test

def playing (p1,p2):
    i=0
    while not check_winner(p1) and not check_winner(p2) and i<9:
        if i % 2 == 0:
            x=-1
            while not (0<=x and x<=8) or board[x] != ' ':
                x = int(input("player 1 play and X in a case from 0 to 8:"))
            board[x]='X'
        #else:
        #    x=-1
        #    while not (0<=x and x<=8) or board[x] != ' ':
        #        x = int(input("player 2 play and O in a case from 0 to 8:"))              !!!  h_u_m_a_n  2  !!!
        #    board[x]='O'

        #else:
        #    for j in range (0,9):
        #        if (board[j] == ' '):                              auto but dump place "O"  in the furt epty cas it find 
        #            board[j]='O'
        #            break
        else : 
            is_maximizing = True
            final_best_score = - float('inf')
            final_best_index = - 1
            for j in range (0 , 9):
                if board[j]==' ':
                    board[j]=p2
                    score = minimax(False, p1 , p2)
                    board[j]=' '
                    if score > final_best_score:
                        final_best_score = score
                        final_best_index = j
            board[final_best_index] = p2

        i = i+1
        print_board()
    print("Did X win?", check_winner(p1))
    print("Did O win?", check_winner(p2))

def minimax(is_maximizing,p1,p2):
    if check_winner(p1):
        return (-1)
    elif check_winner(p2):
        
        return 1
    else:
        #test = True
        #for i in range (0,9):
        #    if (board[i] != ' '):          this is my way but in python there is a function colled 

        #                                                     !!!!! "in" !!!!! 

        #                                                       to check this 
        #        test = False
        #if test == True
        #    return 0

        if ' ' not in board:
            return 0
    
        else:
            if is_maximizing:
                best_score = -float('inf')
                for j in range (0 , 9):
                    if (board[j] == ' '):
                        board[j]=p2
                        score = minimax(False,p1,p2)
                        board[j] = ' '
                        best_score = max(best_score, score)
                return best_score
            else :
                best_score = float('inf')
                for j in range (0 , 9):
                    if (board[j] == ' '):
                        board[j]=p1
                        score = minimax(True,p1,p2)
                        board[j] = ' '
                        best_score = min(best_score, score)
                return best_score

player1 = 'X'
player2 = 'O'
playing(player1,player2)
