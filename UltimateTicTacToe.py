import tkinter
import random
def UltimateTicTacToe():
    import os
    clear = lambda: os.system('clear')

    board_list = [
        [' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    ]
    
    ha = ['','','','','','','','','']
    
    global p1
    global p2

    
    def gameboard():
        print(f'''

          {ha[0]}Board 0           {ha[1]}Board 1           {ha[2]}Board 2
         {board_list[0][0]} | {board_list[0][1]} | {board_list[0][2]}         {board_list[1][0]} | {board_list[1][1]} | {board_list[1][2]}         {board_list[2][0]} | {board_list[2][1]} | {board_list[2][2]}
        -----------       -----------       -----------
         {board_list[0][3]} | {board_list[0][4]} | {board_list[0][5]}         {board_list[1][3]} | {board_list[1][4]} | {board_list[1][5]}         {board_list[2][3]} | {board_list[2][4]} | {board_list[2][5]}
        -----------       -----------       -----------
         {board_list[0][6]} | {board_list[0][7]} | {board_list[0][8]}         {board_list[1][6]} | {board_list[1][7]} | {board_list[1][8]}         {board_list[2][6]} | {board_list[2][7]} | {board_list[2][8]}
        
        
        
          {ha[3]}Board 3           {ha[4]}Board 4           {ha[5]}Board 5 
         {board_list[3][0]} | {board_list[3][1]} | {board_list[3][2]}         {board_list[4][0]} | {board_list[4][1]} | {board_list[4][2]}         {board_list[5][0]} | {board_list[5][1]} | {board_list[5][2]}
        -----------       -----------       -----------
         {board_list[3][3]} | {board_list[3][4]} | {board_list[3][5]}         {board_list[4][3]} | {board_list[4][4]} | {board_list[4][5]}         {board_list[5][3]} | {board_list[5][4]} | {board_list[5][5]}
        -----------       -----------       -----------
         {board_list[3][6]} | {board_list[3][7]} | {board_list[3][8]}         {board_list[4][6]} | {board_list[4][7]} | {board_list[4][8]}         {board_list[5][6]} | {board_list[5][7]} | {board_list[5][8]}
        
        
        
          {ha[6]}Board 6            {ha[7]}Board 7           {ha[8]}Board 8
         {board_list[6][0]} | {board_list[6][1]} | {board_list[6][2]}         {board_list[7][0]} | {board_list[7][1]} | {board_list[7][2]}         {board_list[8][0]} | {board_list[8][1]} | {board_list[8][2]}
        -----------       -----------       -----------
         {board_list[6][3]} | {board_list[6][4]} | {board_list[6][5]}         {board_list[7][3]} | {board_list[7][4]} | {board_list[7][5]}         {board_list[8][3]} | {board_list[8][4]} | {board_list[8][5]}
        -----------       -----------       -----------
         {board_list[6][6]} | {board_list[6][7]} | {board_list[6][8]}         {board_list[7][6]} | {board_list[7][7]} | {board_list[7][8]}         {board_list[8][6]} | {board_list[8][7]} | {board_list[8][8]}

         ''')
    
    
    
    def intro():
        rules = 'rules: figure it out'
        print(rules)
        p1 = input("Who is player 1? ")
        p2 = input("Who is player 2? ")
        a = random.randint(1,101)
        if a<=49:
            c = 0
            print(f"{p1} is first!")
        else:
            c = 1
            print(f'{p2} is first!')
        input("Press enter to begin")
        
        
        
    def p1_input(allcheck, gameslot):
        if allcheck:
            p1_gmslt = input('P1, choose the board number ')
            if p1_gmslt not in '012345678'  or board_list[int(p1_gmslt)][0] in '/\\':
                print("That is not a valid input. Try again")
                return p1_input(allcheck, gameslot)
            else:
                p1_choice = input('P1, choose where you would like to place your marker ')
                if p1_choice == '' or p1_choice not in '012345678' or board_list[int(p1_gmslt)][int(p1_choice)] != ' ':
                    print('That is not a valid input. Please try again.')
                    return p1_input(allcheck, gameslot)
                else:
                    return (int(p1_gmslt), int(p1_choice))
        
        else:
            p1_choice = input('P1, choose where you would like to place your marker ')
            if p1_choice == '' or p1_choice not in '012345678' or board_list[gameslot][int(p1_choice)] != ' ':
                print('That is not a valid input. Please try again.')
                return p1_input(allcheck, gameslot)
            else:
                return (gameslot, int(p1_choice))

    
    
    def p2_input(allcheck, gameslot):
        if allcheck:
            p1_gmslt = input('P2, choose the board number ')
            if p1_gmslt not in '012345678'  or board_list[int(p1_gmslt)][0] in '/\\':
                print('That is not a valid input. Try again')
                return p2_input(allcheck, gameslot)
            else:
                p1_choice = input('P2, choose where you would like to place your marker ')
                if p1_choice == '' or p1_choice not in '012345678' or board_list[int(p1_gmslt)][int(p1_choice)] != ' ':
                    print('That is not a valid input. Please try again.')
                    return p2_input(allcheck, gameslot)
                else:
                    return (int(p1_gmslt), int(p1_choice))
        
        else:
            p1_choice = input('P2, choose where you would like to place your marker ')
            if p1_choice == '' or p1_choice not in '012345678' or board_list[gameslot][int(p1_choice)] != ' ':
                print('That is not a valid input. Please try again.')
                return p2_input(allcheck, gameslot)
            else:
                return (gameslot, int(p1_choice))

    
    def all_checker(gameslot):
        if '\\' == board_list[gameslot][0] or '/' == board_list[gameslot][0]:
            return True
        else:
            return False
        
    def winsmallboardcheck(gameslot):
        if board_list[gameslot][0] == board_list[gameslot][1] == board_list[gameslot][2] != ' ':
            return True
        elif board_list[gameslot][3] == board_list[gameslot][4] == board_list[gameslot][5] != ' ':
            return True
        elif board_list[gameslot][6] == board_list[gameslot][7] == board_list[gameslot][8] != ' ':
            return True
        elif board_list[gameslot][0] == board_list[gameslot][4] == board_list[gameslot][8] != ' ':
            return True
        elif board_list[gameslot][6] == board_list[gameslot][4] == board_list[gameslot][2] != ' ':
            return True
        elif board_list[gameslot][0] == board_list[gameslot][3] == board_list[gameslot][6] != ' ':
            return True
        elif board_list[gameslot][1] == board_list[gameslot][4] == board_list[gameslot][7] != ' ':
            return True
        elif board_list[gameslot][2] == board_list[gameslot][5] == board_list[gameslot][8] != ' ':
            return True
        else:
            return False
        
    def overallgamewin():
        if board_list[0][0] == board_list[1][0] == board_list[2][0] != ' ':
            return True
        elif board_list[3][0] == board_list[4][0] == board_list[5][0] != ' ':
            return True
        elif board_list[6][0] == board_list[7][0] == board_list[8][0] != ' ':
            return True
        elif board_list[0][0] == board_list[4][0] == board_list[8][0] != ' ':
            return True
        elif board_list[6][0] == board_list[4][0] == board_list[2][0] != ' ':
            return True
        elif board_list[0][0] == board_list[3][0] == board_list[6][0] != ' ':
            return True
        elif board_list[1][0] == board_list[4][0] == board_list[7][0] != ' ':
            return True
        elif board_list[2][0] == board_list[5][0] == board_list[8][0] != ' ':
            return True
        else:
            return False

        
    
    def cross_creator(gameslot):
        board_list[gameslot][0] = '\\'
        board_list[gameslot][1] = ' '
        board_list[gameslot][2] = '/'
        board_list[gameslot][3] = ' '
        board_list[gameslot][4] = 'X'
        board_list[gameslot][5] = ' '
        board_list[gameslot][6] = '/'
        board_list[gameslot][7] = ' '
        board_list[gameslot][8] = '\\'

    def circle_creator(gameslot):
        board_list[gameslot][0] = '/'
        board_list[gameslot][1] = '-'
        board_list[gameslot][2] = '\\'
        board_list[gameslot][3] = '|'
        board_list[gameslot][4] = ' '
        board_list[gameslot][5] = '|'
        board_list[gameslot][6] = '\\'
        board_list[gameslot][7] = '-'
        board_list[gameslot][8] = '/'    
    
    def game():
        intro()
        gameboard()
        marker3 = p1_input(True, 0)
        board_list[marker3[0]][marker3[1]] = 'X'
        gameboard()
        gamestop = False
        while not gamestop:
            ha[marker3[1]] = '#'
            clear()
            gameboard()
            ha[marker3[1]] = ''
            marker2 = p2_input(all_checker(marker3[1]),marker3[1])
            board_list[marker2[0]][marker2[1]] = 'O'
            if winsmallboardcheck(marker2[0]):
                circle_creator(marker2[0])
                if overallgamewin():
                    gamestop = True
                    print(f"{p1} WINS! {p2} SUCKS!")
                clear()
                gameboard()
            ha[marker2[1]] = '#'
            clear()
            gameboard()
            ha[marker2[1]] = ''
            marker3 = p1_input(all_checker(marker2[1]), marker2[1])
            board_list[marker3[0]][marker3[1]] = 'X'
            if winsmallboardcheck(marker3[0]):
                cross_creator(marker3[0])
                if overallgamewin():
                    gamestop = True
                    print(f"{p1} WINS! {p2} SUCKS!")
                clear()
                gameboard()
    game()
UltimateTicTacToe()