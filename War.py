#script to play war card game
import random
import time
random.seed(time.time())

#two lists of cards
def gen_deck():
	hand_1, hand_2 = [x for x in range(1,14)]*2,[x for x in range(1,14)]*2
	hand_1, hand_2 = random.sample(hand_1,len(hand_1)),random.sample(hand_2,len(hand_2))
	return hand_1, hand_2

#while loop comparing first card in lists
turns = 0
list = []

def War(hand_1,hand_2,play): #War function

	num_war = 3 #cards in a war
	
	if len(hand_1) == 0 or len(hand_2) == 0: # no need for war, return with winner
		if len(hand_1) > len(hand_2): hand_1.extend(random.sample(play,2))
		else: hand_2.extend(random.sample(play,2))
		return
	else:
		num_war = min(len(hand_1),len(hand_2),num_war) # else remaining cards or maximum
	
	#add to stash
	war_play = [play,[hand_1.pop(0) for x in range(1,num_war+1)],
					 [hand_2.pop(0) for x in range(1,num_war+1)]]
	flat_war_play = [val for sublist in war_play for val in sublist]
	
	if flat_war_play[-1-num_war] > flat_war_play[-1]: #compare last cards
		hand_1.extend(random.sample(flat_war_play,len(flat_war_play)))
	elif flat_war_play[-1-num_war] < flat_war_play[-1]:
		hand_2.extend(random.sample(flat_war_play,len(flat_war_play)))
	elif flat_war_play[-1-num_war] == flat_war_play[-1]: #recursion if tie again
		War(hand_1,hand_2,flat_war_play)
		return
		
def play_war(hand_1,hand_2): #main function
	
	turns = 0
	
	while bool(hand_1) & bool(hand_2): #play until an empty hand
		turns += 1

		play = [hand_1.pop(0),hand_2.pop(0)] #play card
		if play[0] > play[1]: #give cards to winner
			hand_1.extend(random.sample(play,2))
		elif play[0] < play[1]:
			hand_2.extend(random.sample(play,2))
		elif play[0] == play[1]: #go to war
			War(hand_1,hand_2,play)
	list.append(turns) #output list

for x in range(1,1001): #play x games
	hand_1, hand_2 = gen_deck()
	play_war(hand_1,hand_2)

#print(list)

import xlwt #export turns required for a win to excel

wb = xlwt.Workbook()
ws = wb.add_sheet('Sheet 1')

listdata = list

# write each item in the list to consecutive columns on the first row
for index, item in enumerate(listdata):
        ws.write(index, 0, item) 

wb.save('War_stats.xls')
