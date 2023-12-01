from random import randint as e
import time

def print_slow(text):
    for character in text:
        print(character, end='', flush=True)
        time.sleep(0.01) 
    print() 

def input_slow(text):
    for character in text:
        print(character, end='', flush=True)
        time.sleep(0.02) 
    return input()  


print_slow("Welcome to Tic Tac Toe! Only two players.")
print_slow("If you want to end, type end except for choosing a position.")
print_slow("The game continoues until one player has gotten a certain amount of points.")
amount_points =input_slow ("How many points should a player need to win? The default is 3.  ")
if amount_points== "default":
    amount_points=3
else:
    while not amount_points.isdigit():
        print_slow("Wrong input, please input a number greater then 0")
        amount_points =input_slow ("How many points should a player need to win? The default is 3.  ") 
        if amount_points.isdigit():
            amount_points = int(amount_points)
            continue
print_slow(f"The points to reach in order to win are {amount_points}")
print_slow("Points are earned by winning games of tic tac toe. HERE WE....GO!")
name = [" ", " "]
point_1 = 0
point_2 = 0
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

for i in range(2):
    name[i] = input("Player " + str(i + 1) + ", what is your name? ")
    print("Try to win, " + name[i] + "!")

for row in board:
    print("|".join(row)) 


winning_combinations = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)] 
]


def reset_board():
    for i in range(len(board)):
        for n in range(len(board[i])):
            board[i][n] = " "

def check_for_tie(board):
    for row in board:
        if " " in row:
            return False
    return True  
def game():
    global point_1, point_2
    global turn, amount_points
    turn = 0
    Flag = True
    while Flag == True:
        if point_1 == amount_points or point_2 == amount_points:
            Flag = False
        else:

            answer = input(f"{name[turn]}, Choose a number (1-9): ")
            print(f"{name[0]} has {point_1} points.")
            print(f"{name[1]} has {point_2} points.")
            print(f"Points needed to win {amount_points}")
            if answer == "end":
                Flag = False
            elif answer.isdigit() and int(answer) in range(1,10):
                position = int(answer)
                row = (position - 1) // 3
                col = (position - 1) % 3

                if 1 <= position <= 9 and board[row][col] == " ":
                    if turn % 2 == 0:
                        board[row][col] = "X"
                        turn+=1
                    else:
                        board[row][col] = "O"
                        turn-=1

                    for row in board:
                        print("|".join(row))


                    for combination in winning_combinations:
                        marks = [board[r][c] for r, c in combination]
                        if all(mark == "X" for mark in marks):
                            point_1+= 1
                            print(f"Congratulations {name[0]}! good job! Start new round!")
                            print(f"{name[0]} has {point_1} points.")
                            print(f"{name[1]} has {point_2} points.")
                            print(f"Points needed to win {amount_points}")
                            reset_board()

                        elif all(mark == "O" for mark in marks):
                            point_2+=1
                            print(f"Congratulations {name[1]}! good job! Start new round!")
                            print(f"{name[0]} has {point_1} points.")
                            print(f"{name[1]} has {point_2} points.")
                            print(f"Points needed to win {amount_points}")
                            reset_board()

                        elif check_for_tie(board):
                            print("It's a tie! Start new round!")
                            reset_board()
                else:
                    print("Invalid move! Try again!")
                    for row in board:
                        print("|".join(row))
            else:
                print("Wrong input, please input a number between 1-9")
                for row in board:
                        print("|".join(row))
    print("New Game!")
    

while True:
    point_1 = 0
    point_2 = 0
    game()
    if point_1 >= amount_points or point_2 >= amount_points:
        print_slow(f"{name[turn]}, You won!") 
        if input("Do you want to play another game? Y/N: ").lower() == "n":
            print(f"bye {name[1]} and {name[0]}")
            break
    if input == "end":
        print(f"bye {name[1]} and {name[0]}")
        break