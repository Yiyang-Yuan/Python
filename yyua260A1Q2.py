import random
import math

name = input("Please enter your character's name: ")
character_strength = random.randrange(150,251)
character_defence = random.randrange(100,201)
npc_strength = random.randrange(150,251)
npc_defence = random.randrange(100,201)

attack_player = (character_strength - npc_defence) * 1.5
finalattack_player = ( attack_player + abs(attack_player) ) / 2
attack_value1 = round(finalattack_player)
attack_npc = (npc_strength - character_defence) * 1.5
final_attack_npc = ( attack_npc + abs(attack_npc) ) / 2
attack_value2 = round(final_attack_npc)

print(name, " has a strength of ", character_strength, " and a defence of ", character_defence, ".", sep="")
print("The computer player has a strength of ", npc_strength, " and a defence of ", npc_defence, ".", sep="")
print(name, " has attacked the computer inflicting ", attack_value1, " damage.", sep="")
print("The computer has attacked ", name, " inflicting ", attack_value2, " damage.", sep="")

