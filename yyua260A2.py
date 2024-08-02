"""
Name: Yiyang Yuan
username: yyua260
Dscription:
Runs a dice game called Cee-lo and 3 dice are rolled.
A Score is allocated to the dice roll depending on obtained values.
Finally, the winning rate is calculated by program 
In Cee-lo there are only 4 valid dice rolls:
 •4-5-6: The three dice rolled have the values 4, 5 and 6.
 •1-2-3: The three dice rolled have the values 1, 2 and 3.
 •Trip: All 3 dice rolled have the same value.
 •Point: 2 of the 3 dice rolled have the same value.
"""
import random

def main():
    user_name = "yyua260" #Add your username here
    player_wins = 0
    computer_wins = 0
    draws = 0
    player_selection = 1
    display_banner(user_name)
    while player_selection != 0:
        print()
        display_menu()
        player_selection = get_user_input()
        if player_selection == 1:
            player_roll = get_valid_roll()
            computer_roll = get_valid_roll()
            player_score = get_score(player_roll)
            computer_score = get_score(computer_roll)
            print()
            print_separator()
            print_roll("Player", player_roll, player_score)
            print_roll("Computer", computer_roll, computer_score)
            if player_score > computer_score:
                print("Player has won!")
                player_wins += 1
            elif player_score < computer_score:
                print("Computer has won!")
                computer_wins += 1
            else:
                print("It's a draw!")
                draws += 1
            print("Player wins:", player_wins, "Computer wins:", computer_wins, "Draws:", draws)
            print_separator()
    print()
    print_separator()
    print_player_stats(player_wins, computer_wins, draws)
    print_separator()
        
def print_separator():
    sentence = "*" * 46
    return sentence

def display_banner(user_name):
    name = "Cee-lo Game by " + user_name
    length = len(name)
    star = "*" * length
    print(star)
    print(name)
    print(star)

def display_menu():
    print("Please make a selection: ")
    print("Enter 1 to play a round of Cee-lo")
    print("Enter 0 to exit")

def get_user_input():
    number = input("Enter your selection: ")
    integer = int(number)
    while integer != 0 and integer != 1:
        print("Make a valid selection!")
        number = input("Enter your selection: ")
        integer = int(number)
    return integer

def roll_three_dice():
    dice1 = random.randrange(1,7)
    dice2 = random.randrange(1,7)
    dice3 = random.randrange(1,7)
    string = str(dice1) + str(dice2) + str(dice3)
    return string

def is_456(dice_str):
    if dice_str == "456" or dice_str == "546" or dice_str == "645" or dice_str == "465" or dice_str == "564" or dice_str == "654":
       return "True"
    else:
       return "False"

def is_123(dice_str):
    if dice_str == "123" or dice_str == "132" or dice_str == "213" or dice_str == "231" or dice_str == "312" or dice_str == "321":
       return "True"
    else:
       return "False"

def is_trip(dice_str):
    num1 = dice_str[0]
    num2 = dice_str[1]
    num3 = dice_str[2]
    str1 = num1 + num1 + num1
    str2 = num2 + num2 + num2
    str3 = num3 + num3 + num3
    if dice_str == str1 or dice_str == str2 or dice_str == str3:
        return True
    else:
        return False

def is_point(dice_str):
    num1 = dice_str[0]
    num2 = dice_str[1]
    num3 = dice_str[2]
    if num1 == num2 and num1 != num3 or num1 == num3 and num1 != num2 or num2 == num3 and num1 != num2:
        return True
    else:
        return False

def is_valid_roll(dice_str):
    a = is_123(dice_str)
    b = is_456(dice_str)
    c = is_point(dice_str)
    d = is_trip(dice_str)
    if a == True and a != c and a != d:
        return True
    elif b == True and b != c and b != d:
        return True
    elif c == True and c != a and c != b and c != d:
        return True
    elif d == True and d != a and d != b and d != c:
        return True
    else: 
        return False

def get_valid_roll():
    dice = roll_three_dice()
    while is_valid_roll(dice) == False:
        dice = roll_three_dice()
    return dice
    print("Valid Cee-lo roll:", get_valid_roll())

def type_of_roll(dice_str, player):
    a = is_123(dice_str)
    b = is_456(dice_str)
    c = is_point(dice_str)
    d = is_trip(dice_str)
    if a == True and a != c and a != d:
        return player + " has rolled a " + '123'
    elif b == True and b != c and b != d:
        return player + " has rolled a " + '456'
    elif c == True and c != a and c != b and c != d:
        return player + " has rolled a " + 'POINT'
    elif d == True and d != a and d != b and d != c:
        return player + " has rolled a " + 'TRIP'

def get_point_score(dice_str):
    num1 = dice_str[0]
    num2 = dice_str[1]
    num3 = dice_str[2]
    if num1 == num2 and num1 != num3:
        return int(num3) + 10
    elif num1 == num3 and num1 != num2:
        return int(num2) + 10
    elif num2 == num3 and num2 != num1:
        return int(num1) + 10

def get_trip_score(dice_str):
    num = dice_str[-1]
    score = 20 + int(num)
    return score

def get_score(dice_str):
    a = is_123(dice_str)
    b = is_456(dice_str)
    c = is_point(dice_str)
    d = is_trip(dice_str)
    e = get_point_score(dice_str)
    f = get_trip_score(dice_str)
    if a == True and c != True and d != True:
        return 0
    elif b == True and c != True and d != True:
        return 30
    elif c == True and a != True and b != True and d != True:
        return e
    elif d == True and a != True and b != True and c != True:
        return f

def print_roll(player_name, player_roll, player_score):
    a = type_of_roll(player_roll,player_name)
    print(player_name, "has rolled:", player_roll)
    print("(", a , " for a score of ", player_score, ")",sep="")

def print_player_stats(player_wins, computer_wins, draws):
    a = player_wins
    b = computer_wins
    c = draws
    if a + b + c == 0:
        print("Player wins:", player_wins)
        print("Win percentage: ", 0.0 , "%", sep="")
    else: 
        percentage = (a / (a + b + c)) * 100
        percent = round(percentage,1)
        print("Player wins:", player_wins)
        print("Win percentage: ", percent , "%", sep="")

main()
    
        
