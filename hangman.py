#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 14:58:04 2019

@author: gautamvenkatesh
"""
import random
import os
clear = lambda: os.system('clear')

def full_game():
	def word_input():
	    f = open('/Users/gautamvenkatesh/Coding/word_list.txt','r')
	    word_list = f.read()
	    random_num = random.randint(0,1000)
	    return word_list.split()[random_num]
	
	global rand_word
	rand_word = word_input()
	    
	def guessword_list():
	    guesswordli = []
	    for i in range(0,len(rand_word)):
	        guesswordli.append(' ')
	    return guesswordli
	    
	def letter_input():
	    letter = input('What letter do you choose?')
	    if letter not in 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z' or letter == '':
	        print('Enter a valid input')
	        return letter_input()
	    else:
	        return letter
	
	global guess_list    
	guess_list = guessword_list()
	    
	def guess_list_changer():
	    global guess_list
	    global rand_word
	    letter = letter_input()
	    randwordlist = list(rand_word)
	    if letter in randwordlist:
	        for i in range(0,len(randwordlist)):
	            if letter == randwordlist[i]:
	                guess_list[i] = letter
	        return guess_list
	    else:
	        return False
	
	global head
	global pot_head
	global neck1
	global pot_neck1
	global arms1
	global pot_arms1
	global arms2
	global pot_arms2
	global leg1
	global leg2
	global pot_leg1
	global pot_leg2
	global pot_head2
	head = ''
	pot_head = '(˙ ͜˙)'
	neck1 = ''
	pot_neck1 = '|'
	arms1 = ' '
	arms2 = ' '
	pot_arms1 = '_'
	pot_arms2 = '_'
	leg1 = ' '
	leg2 = ' '
	pot_leg1 = '⅃'
	pot_leg2 = 'L'
	pot_head2 = '(x︵x)'

	        
	def drawing(placeholder, guessword):
	    print(f"     ____________\n    |            |\n    |         {arms1}{head}{arms2}\n    |            {neck1}\n    |           {leg1} {leg2}\n    |\n    |\n    |\n    |\n    |\n    |\n    |\n    |                 {guessword}\n    |                {placeholder}\n    |\n___________")
	        
	def game_setup():
	    global rand_word
	    global placeholder
	    placeholder = ''
	    for i in range(0,len(rand_word)):
	        placeholder = placeholder + '  __'
	    guessword = ''
	    for i in range(0,len(rand_word)):
	        guessword = guessword + ' ' + guess_list[i] + '  '
	    drawing(placeholder = placeholder, guessword = guessword)
	        
	def winner_check():
	    global guess_list
	    global rand_word
	    if list(rand_word) == guess_list:
	        return True
	    else:
	        return False

	global counter
	counter = 0
	def game():
	    clear()
	    b=1
	    global rand_word
	    global counter
	    global head
	    global pot_head
	    global neck1
	    global pot_neck1
	    global arms1
	    global pot_arms1
	    global arms2
	    global pot_arms2
	    global leg1
	    global leg2
	    global pot_leg1
	    global pot_leg2
	    print('HANGMAN\nHere are the rules to the game:\n1. A random word has been selected and you must guess what it is\n2. If you get a letter wrong, you will add one more part to the hanging body\n3. If the body is completed, you lose!')
	    input("Press enter to begin")
	    game_setup()
	    while counter<=5 and not winner_check():
	        clear()
	        game_setup()
	        if guess_list_changer() != False:
	            pass
	        else:
	            if counter == 0:
	                head = pot_head
	            elif counter == 1:
	                neck1 = pot_neck1
	            elif counter == 2:
	                arms1 = pot_arms1
	            elif counter == 3:
	                arms2 = pot_arms2
	            elif counter == 4:
	                leg1 = pot_leg1
	            elif counter == 5:
	                leg2 = pot_leg2
	                head = pot_head2 
	                b=0
	                game_setup()
	            counter = counter + 1
	        if b == 0:
	            clear()
	            game_setup()
	            print(f'You Lose! The correct word was {rand_word}!')
	    if winner_check():
	        clear()
	        game_setup()
	        print('You won!')         
	       
	        
	game()

def cont():
	global yorn
	yorn = input('Press y to continue. Press n to exit.\ny/n?')
	if yorn == 'y':
		return True
	elif yorn == 'n':
		return False
	else:
		print('Enter a valid input')
		return cont()
full_game()
while cont():
	full_game()
