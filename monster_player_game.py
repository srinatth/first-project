
# player = ['manuel',10,16,return 100]
from random import randint

game_running = True

game_result = []

def calculate_monster_attack():
	return randint(monster['attack_min'],monster['attack_max'])

def game_ends(winner_name):
	print('{} won the game'.format(winner_name)) 	

while game_running == True:
	counter = 0
	new_round = True
	player = {'name':'Manuel','attack': 13,'heal':16,'health':100}
	monster = {'name':'Max','attack_min':10,'attack_max':20,'health':100}
 	
 	# print('---' * 10)
	print('Enter player name')
	player['name'] = input()

	print(player['name'] + ' has ' + str(player['health']) + ' health')
	print(monster['name'] + ' has ' + str(monster['health']) + ' health')


	while new_round == True:

		counter = counter + 1
		player_won = False
		monster_won = False

		print('---' * 10)
		print('please select action')
		print('1. Attack')
		print('2. heal')
		print('3. exit game')

		player_choice = int(input())

		if player_choice == 1:
			monster['health'] = monster['health']-player['attack']
			if monster['health'] <= 0:
				player_won = True
			else:
				# monster_attack = randint(monster['attack_min'],monster['attack_max']) 
				player['health'] = player['health']-calculate_monster_attack()
				if player['health'] <= 0:
					monster_won = True
			

		elif player_choice == 2:
			# monster_attack = randint(monster['attack_min'],monster['attack_max'])
			player['health'] = player['health']+player['heal']

			player['health'] = player['health']-calculate_monster_attack()
			if player['health'] <= 0:
				monster_won = True


			
		elif player_choice == 3:
			new_round = False
			game_running = False

		else:
			print('select correct input')

		if player_won == False and monster_won == False:
			print(player['name'] + ' has ' + str(player['health']) + ' left')
			print(monster['name'] + ' has ' + str(monster['health']) + ' left')  	

		elif player_won:
			game_ends(player['name'])
			round_result = {'name':player['name'],'health':player['health'],'round':counter}
			game_result.append(round_result)
			new_round = False

		elif monster_won:
			game_ends(monster['name'])	
			round_result = {'name':monster['name'],'health':monster['health'],'round':counter}
			game_result.append(round_result)	
			new_round = False		

