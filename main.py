import sys, subprocess

class GameCharacter:
  def __init__(self, name, health):
      self.name = name
      self.health = health

player_position = [0, 0]  # Starting at top-left corner of the game map

# Define the GameCharacter class and other code as before
class GameCharacter:
    def __init__(self, name, health):
        self.name = name
        self.health = health

# Define the Monster class and create instances as before
class Monster:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

monster_in_room_2 = Monster("Goblin", 50, 20)

if player_position == [0, 1]:  # Assuming room 2 is at index [0, 1] in the game map
     print(f"You encounter {monster_in_room_2.name} with {monster_in_room_2.health} health and {monster_in_room_2.damage} damage.")


print("Welcome to Origin")

print("This game takes inspiration from a game I've played when i was younger called Soul Knight")

input('press enter to continue')

subprocess.run('clear', shell=True)



print("Long ago, there were 7 magic stones, each with their own colour.")

print("These magic stones were sacred relics created by 7 powerful bosses who had also made a dungeon to contain and protect each of them in a shrine.")

print("These stones maintained the balance of the world until one day, the 2 creators of the red stone, the Baby Dragon Bros, weren't satisfied with their power.  ")

print("They went on with their minions to invade the 6 other dungeons and steal the stones and corrupt each of their guardians to turn them to evil and they succeeded.")

print("Without the stones in their place with their creators, the world had descended into chaos and darkness.")

print("Can you defeat the Baby Bragon Bros and retrieve the magic stones?")


input('press enter to continue')

subprocess.run('clear', shell=True)



print("You find yourself as a knight with a sword in a lair full of 13 other heroes. a priest, a necromancer, a druid, a werewolf, a wizard, a vampire, an engineer, a rogue, a paladin, an elf, an alchemist, an assassin, and a berserker.")

print("You all had been working on rebuilding an ancient portal found in one of the 7 abandoned dungeons.")

input('press enter to continue')

subprocess.run('clear', shell=True)

print("This dungeon that had previosly belonged to Zulan the Colossus, a giant robot who protected the blue stone, was the final boss defeated by the dragons and left behind a hidden ancient portal that will bring you back in time to where the Baby Dragon Bros started their invasion.")

input('press enter to continue')

subprocess.run('clear', shell=True)



print("The portal lights up and on the other side you see a war controlled by the 2 dragons, attacking the shrines wave after wave. This was the battle that changed the course of history.")


answer = input("Shall you and your friends try rewriting that history?")

if (answer == "yes"): 
  print("You have entered the portal")

  input('press enter to continue')

  subprocess.run('clear', shell=True)

  
  print("You find yourselves in the magic stone room and see Zulan and his outnumbered looking army of robots far down the hall fighting the minions of the Baby Dragon Bros")

  input('press enter to continue')

  subprocess.run('clear', shell=True)
  
  print("Zulan: Thank goodness someone had found the portal! Maybe there is hope..")

  input('press enter to continue')

  subprocess.run('clear', shell=True)
  
  print("Zulan: All the other bosses have been defeated and tuned evil. Their stones have been taken.")

  input('press enter to continue')

  subprocess.run('clear', shell=True)
  
  print("Zulan: They've been pushing back and the stone isn't too far from us anymore.")

  input('press enter to continue')

  subprocess.run('clear', shell=True)
  
  print("Zulan: Behind me there is a turn that leads to the 2nd enterence of the shrine. I will stay here but i need all of you to go and protect it from that side. This will thin out their army and is our only chance at pushing them back!")

  input('press enter to continue')

  subprocess.run('clear', shell=True)
  
  print("You and your team quickly make your way around the turn leading to the shrine again. You see the blue magic stone but don't take much time to look at it.")
  print("Your friends put their maps away and get their weapons ready to defend the last uncaptured stone.")
  

  
elif (answer == "no"):
   print("You sit back and enjoy the dungeon as your friends enter the war.")
   print("You begin to feel guilty")

else:
  print("Invalid choice. Please choose yes or no.")



# Prompt the player to enter their username
player_name = input("Enter your desired username: ")

# Create a GameCharacter instance with the chosen username
player = GameCharacter(player_name, 100)

# Print a message confirming the chosen username
print(f"Player's username set to: {player.name}")


class GameCharacter:
  def __init__(self, name, health):
      self.name = name
      self.health = health


player1 = GameCharacter("Player 1", 100)

# Access and modify the health attribute of the player
print(f"{player1.name}'s health: {player1.health}")

# Decrease the player's health
player1.health -= 10
print(f"{player1.name}'s health after taking damage: {player1.health}")


class Monster:
  def __init__(self, name, health, damage):
      self.name = name
      self.health = health
      self.damage = damage

# Define a monster in room 2 with health and damage
monster_in_room_2 = Monster("Goblin", 50, 20)

# Access and modify the monster's attributes
print(f"{monster_in_room_2.name}'s health: {monster_in_room_2.health}")
print(f"{monster_in_room_2.name}'s damage: {monster_in_room_2.damage}")

# Sample usage in room 2 of the game
if player_position == [0, 1]:  # Assuming room 2 is at index [0, 1] in the game map
  print(f"You encounter {monster_in_room_2.name} with {monster_in_room_2.health} health and {monster_in_room_2.damage} damage.")

if player_position == [0, 1]:
    print(f"You encounter {monster_in_room_2.name} with {monster_in_room_2.health} health and {monster_in_room_2.damage} damage.")


game_map = [
  ['Room 1', 'Room 2', 'Room 3'],
  ['Room 4', 'Room 5', 'Room 6'],
  ['Room 7', 'Room 8', 'Room 9']
]

#  player position
player_position = [0, 0]  # Starting at top-left

# display the current room and possible directions
def display_room():
  current_room = game_map[player_position[0]][player_position[1]]
  print(f'You are in {current_room}')

  # valid movements
  possible_moves = []
  if player_position[0] > 0:
      possible_moves.append('up')
  if player_position[0] < len(game_map) - 1:
      possible_moves.append('down')
  if player_position[1] > 0:
      possible_moves.append('left')
  if player_position[1] < len(game_map[0]) - 1:
      possible_moves.append('right')

  print('Possible moves:', possible_moves)

# Main game loop
while True:
  display_room()
  user_input = input('Enter your move (up/down/left/right): ')

  if user_input == 'up' and player_position[0] > 0:
      player_position[0] -= 1
  elif user_input == 'down' and player_position[0] < len(game_map) - 1:
      player_position[0] += 1
  elif user_input == 'left' and player_position[1] > 0:
      player_position[1] -= 1
  elif user_input == 'right' and player_position[1] < len(game_map[0]) - 1:
      player_position[1] += 1
  else:
      print('Invalid move. Try again.')


