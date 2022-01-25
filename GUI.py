from ast import Str
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





import pygame

pygame.init()

pygame.display.set_caption('SCRABBLE')
global screen
screen = pygame.display.set_mode((1000, 1000))
screen.fill((255,255,255))

letterset = generate_letterset()
print(letterset)


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
        
    def add_tile(self):
        self.st_srf = pygame.Rect(self.x+4, self.y+4, 40, 40)
        self.tile = pygame.image.load(os.path.join('tiles',str(random.choice(letterset)+'.png')))
        screen.blit(self.tile, self.st_srf)
        self.is_filled = True
        print("ADD")
        
        pygame.display.update()
        
        
    def remove_tile(self):
        self.is_filled = False
        print("REMOVE")
        screen.fill((255,255,255), self.st_srf)
        del(self.tile)
        del(self.st_srf)
        pygame.display.update()

        
        
        
        

# class single_tile(pygame.sprite.Sprite):
#     def __init__(self, x, y, letter, screen=None):
#         super().__init__()
#         self.x = x    
#         self.y = y
#         self.st_srf = pygame.Rect(self.x, self.y, 40,40)    
#         self.tile = pygame.image.load(os.path.join('tiles',str(random.choice(letterset)+'.png')))
#         screen.blit(self.tile, self.st_srf)
#         pygame.display.update()
        

        
    



        
class board(board_field):
    def __init__(self):
        #self.fieldset = []
        
        self.board_fields = pygame.sprite.Group()
        
        
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
                
                # tmp_fieldset.append(tmp_field)
                # tmp_fontset.append(tmp_field.change_text(''))
                # self.fieldset.append(tmp_fieldset)
                # self.fontset.append(tmp_fontset)
                
       




b= board()



        

        
    
        
            
        

    
        



class player():
    def __init__(self):
        pass

test_letters = ['A','B','C','D','E','F','G']
         
class player_board(board_field):
        def __init__(self, letterset = []):
            self.fieldset = []
            self.fontset = []
            self.curr_letterset = []
            self.player_area = pygame.draw.rect(screen, black, [10,465,451,150], 3)
            
            for j in range(16,197,30):
                self.board_field = board_field(j,470,'',black)
                
            
            
                
test = pygame.image.load(os.path.join('tiles','X.png')).convert()
print(test.get_size())


        
 
      
        

tile_group = pygame.sprite.Group()        
    


#single_letter = pygame.draw.rect(screen, (0,0, 255), [20,20,20,20], 2)

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
                    if element.is_filled == False:
                        element.add_tile()
                    else:
                        element.remove_tile()
                    
                    
                    
                  
                  
                    
            
                
       
            
                        
                        
                        
                        
                

            
            
           
    #pygame.display.init()














# ###########old

# root = Tk()
# root.geometry("800x600")
# root.title("SCRABBLE")



# class Field():
#     #generate field, set position x, position y, background color, bonus points, bonus type
#     def __init__(self, posx, posy, bg, bonus, bonus_type):
#         self.posx = posx
#         self.posy = posy
#         self.bonus = bonus
#         self.bonus_type = bonus_type
#         #generate text variable and button, put on desired place
#         self.txtvar = StringVar()
#         self.btn = Button(root, text="", width="4", bg=bg, textvariable=self.txtvar)
#         self.btn['command'] = lambda:[self.on_click_btn()]
#         self.btn.grid(row=posx,column=posy)


#     def on_click_btn(self):
#         #count blanks
#         bl = Counter(chain(*[x for x in B.board])).get('')
#         #get all neighbouring fields
#         if_move_possible = Counter([B.board[self.posx-2][self.posy-1],B.board[self.posx][self.posy-1],
#         B.board[self.posx-1][self.posy-2],B.board[self.posx-1][self.posy]])

#         #check the following conditions:
#         #text variable is blank, variable letter in use contains letter,
#         #at least one neighbouring field should be filled or number of blank fields should be 225 (state when game starts)
#         #additionally - direction x and y is filled in order to gather information about possible axis
#         if self.txtvar.get() == "" and B.liu is not None and (if_move_possible.get('') != 4 or bl == 225):
#             self.txtvar.set(B.liu)
#             B.tmp_board[self.posx-1][self.posy-1] = B.liu
#             B.directionx.append(self.posx-1)
#             B.directiony.append(self.posy-1)
#             B.liu = None
#         else:
#             if B.liu is None and self.txtvar.get() != "":
#                 B.tmp_board[self.posx-1][self.posy-1] = ''
#                 B.liu = self.txtvar.get()
#                 self.txtvar.set('')
         




# class Board(Field):
#     def __init__(self):
#         #generate letters
#         self.letters_list = list()
#         for lt in letters_freq:
#             self.letters_list.extend([lt[0] for i in range(lt[1])])
#         np.random.shuffle(self.letters_list)

#         #generate state of board
#         self.board = np.empty(shape=(15,15), dtype=str)
#         self.tmp_board = np.empty(shape=(15,15), dtype=str)
#         self.directionx = []
#         self.directiony = []

#         self.liu = None

#         #generate buttons
#         self.fieldset = []

#         for i in range(1,16):
#             tmp_fieldset = []
#             for j in range(1,16):
#                 if special_field(i,j) == "TWS":
#                     tmp_fld = Field(i,j,'red', 0, "TWS")
#                 elif special_field(i,j) == "DLS":
#                     tmp_fld = Field(i,j,'cyan', 0, "DLS")
#                 elif special_field(i,j) == "DWS":
#                     tmp_fld = Field(i,j,'pink', 0, "DWS")
#                 elif special_field(i,j) == "TLS":
#                     tmp_fld = Field(i,j,'blue', 0, "TLS")
#                 elif special_field(i,j) == "CNT":
#                     tmp_fld = Field(i,j,'orange', 0, "CNT")
#                 else:
#                     tmp_fld = Field(i,j,'white', 0, 0)
        
#                 tmp_fieldset.append(tmp_fld)
                
#             self.fieldset.append(tmp_fieldset)
            


    
#     #draw letters from resources
#     def get_letters(self, no):
#         temp_list = list()
#         for i in range(no):
#             drawn_letter = np.random.choice(self.letters_list)
#             temp_list.extend(drawn_letter)
#             self.letters_list.remove(drawn_letter)
#         return temp_list





# class Player_Field():
#     def __init__(self, posy, bg, strvalue):
#         self.txtvar = StringVar(value = strvalue)
#         self.btn = Button(root, text="", width="4", bg=bg, textvariable=self.txtvar)
#         self.btn['command'] = lambda:[self.on_click_lt()]
#         self.btn.grid(row=17,column=posy)

#     def on_destroy(self):
#         self.btn.destroy()
        

#     def on_click_lt(self):
#         #if field is not blank - get letter

#         if self.txtvar.get() != "" and B.liu is None:
#             B.liu = self.txtvar.get()
#             self.txtvar.set('')
#         else:
#             if B.liu is not None and self.txtvar.get() == "":
#                 self.txtvar.set(B.liu)
#                 B.liu = None




# class Player(Player_Field):
#     def __init__(self,name,score=0,pos=None):
#         self.pos = pos
#         self.name = name
#         self.score = score
#         self.letters_poss = []
#         self.tmp_field = []
#         self.pl_btn_fld = []
#         #generate score indicators for all players
#         self.pl_lbl_txt_var = StringVar()
#         self.pl_lbl_txt_var.set(self.name + ': ' + str(self.score))
#         self.pl_lbl = Label(root, textvariable=self.pl_lbl_txt_var)
#         self.pl_lbl.grid(row=self.pos, column=17)

        


#     def generate_pl_let(self):
#         self.pl_label = Label(root, text=self.name)
#         self.pl_label.grid(row=16,column=1, columnspan=3)
#         for k in range(1,8):
#             self.tmp_pl_field = Player_Field(k, 'white', self.letters_poss[k-1])
#             self.pl_btn_fld.append(self.tmp_pl_field)
        
#         self.pl_end_btn = Button(root, text='KONIEC TURY', command=lambda:[self.destroy_pl_let()])
#         self.pl_end_btn.grid(row=17,column=9, columnspan=4)

#         self.pl_chkbox = Checkbutton(root, text="WYMIANA")
#         self.pl_chkbox.grid(row = 17, column=13, columnspan=4)

#     def destroy_pl_let(self):
#         #destroy all widgets created for current player and change to the next player
        
#         for wdg in self.pl_btn_fld:
#             wdg.on_destroy()
#         self.pl_chkbox.destroy()
#         self.pl_end_btn.destroy()
#         self.pl_label.destroy()

    
#         if G.curr_player == G.no_players -1:
#             G.curr_player = 0
#             G.turn_state = True
#             G.curr_turn += 1
#         else:
#             G.curr_player += 1
#             G.turn_state = True
#             G.curr_turn += 1
        
        
        










# B = Board()


# class Game():
#     def __init__(self,no_players,turn_state=False):
#         self.game_state = False
#         self.turn_state = False
#         self.pl_pool = []
#         self.no_players = no_players
#         self.curr_player = 0
#         self.curr_word = []
#         self.curr_turn = 0


#         #create players for testing purposes
#         tmp_player = Player(name="Andrzej", pos=1)
#         self.pl_pool.append(tmp_player)
#         tmp_player = Player(name="Adam", pos=2)
#         self.pl_pool.append(tmp_player)

        

#         # for i in range(int(no_players)):
#         #     pl_name = simpledialog.askstring(prompt='Podaj imię gracza nr ' + str(i+1), title='Do dzieła!')
#         #     tmp_player = Player(name=pl_name, pos=i+1)
#         #    self.pl_pool.append(tmp_player)
        
#     def players_turn(self):
#         #check if number of letters is 0
        
            
            
            
#             self.pl_pool[self.curr_player].letters_poss = B.get_letters(7)
#             self.pl_pool[self.curr_player].generate_pl_let()
#             print('smt')
#             while True:
#                 print(self.turn_state)
#                 if self.turn_state == True:
#                     continue
            
            
            

        
            
        
        
   
        

       
        
        

# G = Game(2)


# G.players_turn()

# G.players_turn()
    
    





# if __name__ == "__main__":
#     root.mainloop()