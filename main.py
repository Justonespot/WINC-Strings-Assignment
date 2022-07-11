# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
from tkinter import N

# Part 1

#1
Score_player_0 = 'Ruud Gullit '
Score_player_1 = 'Marco van Basten '

#2
goal_0 = 32
goal_1 = 54

#3
Score_player_time_0 = Score_player_0 + str (goal_0)
Score_player_time_1 = Score_player_1 + str (goal_1)
scorers = Score_player_time_0 + ', ' + Score_player_time_1

#4
report = Score_player_0 + 'scored in the ' + str (goal_0) + 'nd minute\n' + Score_player_1 + 'scored in the ' + str (goal_1) + 'th minute'

#Part 2

#1
player = 'Jan Wouters'

#2
first_name = player.split()[0]

#3
last_name = player.split()[1]
last_name_len = len (last_name)

#4
first_letter = (player[0])
name_short = first_letter + '. ' + last_name

#5
number_letters_first_name = len (first_name)
chant0 = number_letters_first_name * (first_name + '! ')
chant = chant0.strip ( )

#6
good_chant = chant == 'Jan! Jan! Jan!'




