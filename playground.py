import maptools
import chartools
import os

CURSOR = ">>> "
START_X = 1
START_Y = 1
START_Z = 0

def create_map():
	worldMap = maptools.coordSystem("World Map", 3,3,1)
	worldMap.getLocation(0,0,0).name = "SWVille"
	worldMap.getLocation(1,0,0).name = "SVille"
	worldMap.getLocation(2,0,0).name = "SEVille"
	worldMap.getLocation(0,1,0).name = "WVille"

	worldMap.getLocation(1,1,0).name = "CVille"
	worldMap.getLocation(1,1,0).nearDesc = "A flat land."
	worldMap.getLocation(1,1,0).items.append("sword")
	worldMap.getLocation(1,1,0).items.append("shield")
	worldMap.getLocation(1,1,0).items.append("armor")
	worldMap.getLocation(1,1,0).items.append("helmet")
	worldMap.getLocation(1,1,0).characters.append("Frank")
	worldMap.getLocation(1,1,0).characters.append("Joe")
	worldMap.getLocation(1,1,0).characters.append("Mike")
	worldMap.getLocation(1,1,0).characters.append("Arnold")

	worldMap.getLocation(2,1,0).name = "EVille"
	worldMap.getLocation(0,2,0).name = "NWVille"
	worldMap.getLocation(1,2,0).name = "NVille"
	worldMap.getLocation(2,2,0).name = "NEVille"

	return worldMap

def gameplay(player, worldMap):
	
	while True:
		curLoc = worldMap.getLocation(player.curXPos, player.curYPos, player.curZPos)
		print("What do you want to do?" )
		command = input(CURSOR)	
		command = str.lower(command)		
	
		if (command == 'look') or (command == 'l'):
			description = "You are in " + curLoc.name + "."
			description += curLoc.nearDesc
			
			if (len(curLoc.items) > 0):
				description = description + " Items are: "
				for item in enumerate(curLoc.items):
					description = description + item[1]
					if (item[0] < len(curLoc.items)-1):
						description = description + ", "
						
				description = description + ". "
			
			if (len(curLoc.characters) > 0):
				description = description + "Characters are: "
				for character in enumerate(curLoc.characters):
					description = description + character[1]
					if (character[0] < len(curLoc.characters)-1):
						description = description + ", "
	
				description = description + ". "
			print(description)
		elif (command == 'move') or (command == 'm'):
			avail_dirs = []
			if (player.curYPos < worldMap.yMax - 1) and (worldMap.getLocation(player.curXPos, player.curYPos + 1, player.curZPos).has_sEntrance == True):
				avail_dirs.append("North")
			if (player.curXPos < worldMap.xMax - 1) and (worldMap.getLocation(player.curXPos + 1, player.curYPos, player.curZPos).has_wEntrance == True):
				avail_dirs.append("East")
			if (player.curYPos > 0) and (worldMap.getLocation(player.curXPos, player.curYPos - 1, player.curZPos).has_nEntrance == True):
				avail_dirs.append("South")
			if (player.curXPos > 0) and (worldMap.getLocation(player.curXPos - 1, player.curYPos, player.curZPos).has_eEntrance == True):
				avail_dirs.append("West")
			if (player.curZPos < worldMap.zMax -1) and (worldMap.getLocation(player.curXPos, player.curYPos, player.curZPos + 1).has_dEntrance == True):
				avail_dirs.append("Up")
			if (player.curZPos > 0) and (worldMap.getLocation(player.curXPos, player.curYPos, player.curZPos - 1).has_uEntrance == True):
				avail_dirs.append("Down")
							
			move_q = "Which direction would you like to move? Available direcitions are "
			
			for direction in enumerate(avail_dirs):
				move_q += direction[1]
				if (direction[0] < len(avail_dirs) - 1):
					move_q += ","
					if (direction[0] == len(avail_dirs) - 2):
						move_q += " and "
					else:
						move_q += " "
				else:
					move_q += "."
			
			print(move_q)
			dir_command = input(CURSOR)
			dir_command = str.lower(dir_command)
			
			if (dir_command == 'n'):
				dir_command = "north"
			elif (dir_command == 'e'):
				dir_command = "east"
			elif (dir_command == 's'):
				dir_command = "south"
			elif (dir_command == 'w'):
				dir_command = "west"
			elif (dir_command == 'u'):
				dir_command = "up"
			elif (dir_command == 'd'):
				dir_command = "down"
			

			for direction in avail_dirs:
				if dir_command == str.lower(direction):
					if dir_command == "north":
						player.curYPos += 1
					elif dir_command == "east":
						player.curXPos += 1
					elif dir_command == "south":
						player.curYPos -= 1
					elif dir_command == "west":
						player.curXPos -= 1
					elif dir_command == "up":
						player.curZPos += 1
					elif dir_command == "down":
						player.curZPos -= 1
					else:
						print("Direction Unavailable")
				

		elif (command == 'quit') or (command == 'q'):
			break
		else:
			print("Invalid input.\n")

	return
		

def new_game():
	player = chartools.character()
	player.name = input("Character Name: ")

	while True:

		print("Character Race:\n\t1. [H]uman\n\t2. [E]lf\n\t3. [D]warf")
		race_choice = input(CURSOR)
	
		race_choice = str.lower(race_choice)	

		if (race_choice == '1') or (race_choice == 'human') or (race_choice == 'h'):
			player.race = "human"
			break
		elif (race_choice == '2') or (race_choice == 'elf') or (race_choice == 'e'):
			player.race = "elf"
			break
		elif (race_choice == '3') or (race_coice == 'dwarf') or (race_choice == 'd'):
			player.race = "dwarf"
			break
		else:
			print("Invalid Option\n")	
	
	article = "a"

	if (player.race == "elf"):
		article = "an"
	
	worldMap = create_map()

	player.curXPos = START_X
	player.curYPos = START_Y
	player.curZPos = START_Z
	
	print("Welcome, {}, to the world of {}, you begin your quest in {}.".format(player.name, worldMap.name, worldMap.getLocation(START_X,START_Y,START_Z).name),sep='')		
	gameplay(player,worldMap)
	
	return

def main_menu():
	os.system('clear')
	print("Welcome to Nick's Adventure Game!\n\n\n")
	menu_txt = "What would you like to do?\n\t1. [N]ew Game\n\t2. [L]oad Game\n\t3. [A]bout\n\t4. [Q]uit\n\n"
	p_menu_choice = ''

	while True:
		
		print(menu_txt)
		p_menu_choice = input(CURSOR)
		p_menu_choice = str.lower(p_menu_choice)	

		if (p_menu_choice == '1') or (p_menu_choice == "new game") or (p_menu_choice == "n"):
			new_game()
			
		elif (p_menu_choice == "2") or (p_menu_choice == "load game") or (p_menu_choice == "l"):
			print("You selected 'load game'")
			os.system('clear')
		elif (p_menu_choice == "3") or (p_menu_choice == "about") or (p_menu_choice == "a"):
			print("You selected 'about'")
			os.system('clear')
		elif (p_menu_choice == "q") or (p_menu_choice == "quit") or (p_menu_choice == '4'):
			break
		else:
			os.system('clear')
			print("Invalid Option\n")
			
	
	return

	


def main():
	main_menu()
	
	exit()
	

if __name__ == "__main__":
    main()
