from ast import Str
from msilib import sequence
import os
from tkinter import *
from tkinter import simpledialog


import numpy as np
import random

from numpy.lib.function_base import _update_dim_sizes
import pygments
from LOGIC import *
from itertools import chain
from collections import Counter

from operator import itemgetter



import pygame

pygame.init()

pygame.display.set_caption('SCRABBLE')
global screen
screen = pygame.display.set_mode((1000, 1000))
screen.fill((255,255,255))




class board_field(pygame.sprite.Sprite):
    def __init__(self, i_pos, j_pos ,x, y, letter, bg, bonus=None):
        super().__init__()
        #element numbers in i,j matrix
        self.i_pos = i_pos
        self.j_pos = j_pos
        self.tile = None
        
        #field coordinates
        self.x = x
        self.y = y

        self.letter = ''
        self.single_letter = pygame.draw.rect(screen, bg, [x,y,47,47], 3)
        self.bonus = bonus
        
        self.is_filled = False
    
    
    #add tile on the board  
    def add_tile(self, lt):
        self.st_srf = pygame.Rect(self.x+4, self.y+4, 40, 40)
        self.tile = pygame.image.load(os.path.join('tiles',str(lt+'.png')))
        screen.blit(self.tile, self.st_srf)
        self.is_filled = True
        self.letter = lt
        print("ADD")
        
        pygame.display.update()
        
        
    def remove_tile(self):
        self.is_filled = False
        print("REMOVE")
        screen.fill((255,255,255), self.st_srf)
        del(self.tile)
        del(self.st_srf)
        pygame.display.update()

        
        
        
        


        

        
    



        
class board(board_field):
    def __init__(self):
        #create sprite group for single fields        
        self.board_fields = pygame.sprite.Group()
        
        #stores current and temporary state of the board
        self.curr_board = np.empty(shape=(15,15), dtype=str)
        self.tmp_board = np.empty(shape=(15,15), dtype=str)
        
    #draw board
        for i in range(15):
            tmp_fieldset = []
            
            for j in range(15):
             #bg adjustWment
                
                #based on the rules set in logic
                if special_field(i+1, j+1) == "TWS":
                    tmp_field = board_field(i, j, i*49, j*49, '', red, "TWS")
                elif special_field(i+1, j+1) == "DLS":
                    tmp_field = board_field(i, j, i*49, j*49, '', light_blue, "DLS")
                elif special_field(i+1, j+1) == "DWS":
                    tmp_field = board_field(i ,j, i*49, j*49,'', pink, "DWS")
                elif special_field(i+1, j+1) == "TLS":
                    tmp_field = board_field(i, j, i*49, j*49,'', blue, "TLS")
                elif special_field(i+1, j+1) == "CNT":
                    tmp_field = board_field(i, j, i*49, j*49,'', pink, "CNT")
                else:
                    tmp_field = board_field(i, j, i*49, j*49,'', black, None)
                
                self.board_fields.add(tmp_field)



''''''''''creates space for player letters every single turn'''                
class Player_Workplace(board_field):
    def __init__(self, player_name, player_letters):
        self.player_fields = pygame.sprite.Group()
        
        
        
        ####FONT
        ft = pygame.font.SysFont('Arial', 30)
        player_name_text = ft.render(player_name, True, black)
        self.player_name_text_rect = player_name_text.get_rect()
        self.player_name_text_rect.center = (150, 780)
        screen.blit(player_name_text, self.player_name_text_rect)
        pygame.display.update()
        ###########
        
        for i in range(7):
            for j in range(7):
                tmp_field = board_field(i, j, i*49, j*800, '', black, None)
            
                self.player_fields.add(tmp_field)
                pygame.display.update()

               
class Player():
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.player_letters = list()

        
        
        
       

class Game():
    def __init__(self):
        self.current_turn = 0
        self.letterset = generate_letterset()
        
    def choose_random_letters(self, nb_of_lt):
        chosen_letters_ix = random.choices([i for i in range (len(self.letterset))], k=int(nb_of_lt))
        #get random letters by indexes and remove drawn letters from letterset
        chosen_letters = [self.letterset[i] for i in chosen_letters_ix]
        self.letterset = [self.letterset[i] for i in range(len(self.letterset)) if i not in chosen_letters_ix]
        print(chosen_letters)
        return chosen_letters
        
        


b= board()


        
player_pool = [Player('Janusz'), Player('Grazyna')]
        

print(player_pool[0].name)
        
g = Game()
pl_wkspc = Player_Workplace(player_pool[1].name, player_letters=None)
                
player_pool[0].player_letters.append(g.choose_random_letters(7))           
            
print(player_pool[0].player_letters)  
print(g.letterset)
print(len(g.letterset))


        
 
      
        

   
 

running = True



pygame.display.update()
while running:
    
    #screen.fill(0,0,0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for element in b.board_fields.sprites():
                if element.single_letter.collidepoint(pos):
                    #check if clicked field is filled and insert tile here
                    if element.is_filled == False:
                        element.add_tile('A')
                        b.tmp_board[element.j_pos][element.i_pos] = 'A'

                    else:
                        element.remove_tile()
                        b.tmp_board[element.j_pos][element.i_pos] = ''
                    
                    
                    
                  
                  
                    
            
                
       
            
                        
                        
                        
                        
                

            
            
           
    #pygame.display.init()













