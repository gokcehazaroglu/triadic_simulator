import sys, os, copy, inspect
from Triadic import *
from random import *

def print_scores(list_players):
	print 'Total:'
	for i in list_players:
		print i.name+': '+str(i.money)
	print ''

def play(list_players,who_plays,target,amount,op):
	if not op=='n':
		print ('player '+list_players[who_plays].name+' gives '+str(amount)+'/'+str(list_players[who_plays].money)+' to player '+list_players[target].name+', player '+list_players[target].name+' receives '+str(3*amount)+'\n')
	# print 'player '+list_players[target].name+' receives '+str(3*amount)+'\n'
	list_players[who_plays].money=list_players[who_plays].money-amount
	list_players[target].money=list_players[target].money+3*amount
	if not op=='n':
		print_scores(list_players)


def play_random(list_players,who_plays,op):
	# print 'who plays: '+str(who_plays)+'\n'
	# target=sample([i for i in list_players if not i==list[who_plays]],1)
	target=sample([i for i in range(0,len(list_players)) if not i==who_plays],1)[0]
	# print 'target: '+str(target)+'\n'
	amount=randint(1,list_players[who_plays].money)
	play(list_players,who_plays,target,amount,op)
	dissim_index=0
	l=[i.money for i in list_players]
	mean=sum(l)/len(l)
	for i in l:
		dissim_index=dissim_index+abs(i-mean)
	dissim_index=float(dissim_index)/sum(l)
	return [target,amount,dissim_index]

def play_egalitarian(list_players,who_plays):
	all_moves=[]
	for i in range(1,20):
		copy_list_players=copy.deepcopy(list_players)
		# all_moves=all_moves.append([k for k in play_random(copy_list_players,who_plays)])
		all_moves.append(play_random(copy_list_players,who_plays,'n'))
	dissims=[i[2] for i in all_moves]
	for i in all_moves:
		print i
	min_dis_ind=dissims.index(min(dissims))
	print 'chosen move is '+str(min_dis_ind)
	move=all_moves[min_dis_ind]
	play(list_players,who_plays,move[0],move[1],'y')



def main():
	num_players=3
	num_turns=randint(1,7)

	players=[]
	turns=[]

	for i in range(0,num_players):
		my_Agent=Agent(100,num_turns,'equality')
		players.append(my_Agent)
		turns.append(my_Agent)
		print my_Agent

	players[0].name='A0'
	players[1].name='A1'
	players[2].name='A2'

	# print players[0]
	# print turns[0]

	while len(turns)>0:
		whose_turn=randint(0,len(turns)-1)
		whose_turn_players=players.index(turns[whose_turn])
		print '\nwhose turn: '+str(whose_turn)+' '+turns[whose_turn].name+'\n'
		if whose_turn==0:
			play_egalitarian(players,whose_turn_players)
		else:
			play_random(players,whose_turn_players,'y')
		turns[whose_turn].num_turns=turns[whose_turn].num_turns-1
		print turns[whose_turn].name+' turns: '+str(turns[whose_turn].num_turns)+'\n'

		if turns[whose_turn].num_turns==0:
			print turns[whose_turn].name+' is removed.\n'
			turns.pop(whose_turn)

	# print players[0]
	
if __name__ == '__main__':
	main()