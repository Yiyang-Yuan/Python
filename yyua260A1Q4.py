import random

dice1 = random.randrange(1,6)
dice2 = random.randrange(1,6)
dice3 = random.randrange(1,6)
dice4 = random.randrange(1,6)
dice5 = random.randrange(1,6)

print("*" * 45)

print("REACH 100 IN THREE ROUNDS! Initial total: 0")

print("*" * 45)

print()
print()

print("Round 1:")
print("Your dice: ", dice1, dice2, dice3, dice4, dice5)
User_chose1 = input("  Tens? ")
User_chose2 = input("  Units? ")

num1 = User_chose1[-1]
num2 = User_chose2[-1]
dice = str(dice1) + str(dice2) + str(dice3) + str(dice4) + str(dice5)
position1 = dice[int(num1) - 1]
position2 = dice[int(num2) - 1]

total_value = position1 + position2
dice_value1 = 100 - int(total_value)
print("Dice value: ", total_value)
print("Your current total: ", total_value)

print()
print()
print()

dice1 = random.randrange(1,6)
dice2 = random.randrange(1,6)
dice3 = random.randrange(1,6)
dice4 = random.randrange(1,6)
dice5 = random.randrange(1,6)

print("Round 2:")
print("Your dice: ", dice1, dice2, dice3, dice4, dice5)
User_chose3 = input("  Tens? ")
User_chose4 = input("  Units? ")

num3 = User_chose3[-1]
num4 = User_chose4[-1]
dice = str(dice1) + str(dice2) + str(dice3) + str(dice4) + str(dice5)
position3 = dice[int(num3) - 1]
position4 = dice[int(num4) - 1]

total_value2 = position3 + position4
dice_value2 = 100 - int(total_value2)
print("Dice value: ", total_value2)
current_total2 = int(total_value) + int(total_value2)
print("Your current total: ", str(current_total2))

print()
print()
print()

dice1 = random.randrange(1,6)
dice2 = random.randrange(1,6)
dice3 = random.randrange(1,6)
dice4 = random.randrange(1,6)
dice5 = random.randrange(1,6)

print("Round 3:")
print("Your dice: ", dice1, dice2, dice3, dice4, dice5)
User_chose5 = input("  Tens? ")
User_chose6 = input("  Units? ")

num5 = User_chose5[-1]
num6 = User_chose6[-1]
dice = str(dice1) + str(dice2) + str(dice3) + str(dice4) + str(dice5)
position5 = dice[int(num5) - 1]
position6 = dice[int(num6) - 1]

total_value3 = position5 + position6
dice_value3 = 100 - int(total_value3)
print("Dice value: ", total_value3)

print()
print()

current_total3 = int(total_value) + int(total_value2) + int(total_value3)
away_distance = 100 - current_total3

print("*" * 29)

print("Your final score: ", current_total3)
print("You are", away_distance, "away from the goal")

print("*" * 29)
