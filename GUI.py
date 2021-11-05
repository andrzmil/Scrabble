from ast import Str
from os import remove
from tkinter import *
from tkinter import simpledialog


import numpy as np
import random

from numpy.lib.function_base import _update_dim_sizes
from LOGIC import *
from itertools import chain
from collections import Counter

root = Tk()
root.geometry("800x600")
root.title("SCRABBLE")






class Field():
    #generate field, set position x, position y, background color, bonus points, bonus type
    def __init__(self, posx, posy, bg, bonus, bonus_type):
        self.posx = posx
        self.posy = posy
        self.bonus = bonus
        self.bonus_type = bonus_type
        #generate text variable and button, put on desired place
        self.txtvar = StringVar()
        self.btn = Button(root, text="", width="4", bg=bg, textvariable=self.txtvar)
        self.btn['command'] = lambda:[self.on_click_btn()]
        self.btn.grid(row=posx,column=posy)


    def on_click_btn(self):
        #count blanks
        bl = Counter(chain(*[x for x in B.board])).get('')
        #get all neighbouring fields
        if_move_possible = Counter([B.board[self.posx-2][self.posy-1],B.board[self.posx][self.posy-1],
        B.board[self.posx-1][self.posy-2],B.board[self.posx-1][self.posy]])

        #check the following conditions:
        #text variable is blank, variable letter in use contains letter,
        #at least one neighbouring field should be filled or number of blank fields should be 225 (state when game starts)
        #additionally - direction x and y is filled in order to gather information about possible axis
        if self.txtvar.get() == "" and B.liu is not None and (if_move_possible.get('') != 4 or bl == 225):
            self.txtvar.set(B.liu)
            B.tmp_board[self.posx-1][self.posy-1] = B.liu
            B.directionx.append(self.posx-1)
            B.directiony.append(self.posy-1)
            B.liu = None
        else:
            if B.liu is None and self.txtvar.get() != "":
                B.tmp_board[self.posx-1][self.posy-1] = ''
                B.liu = self.txtvar.get()
                self.txtvar.set('')
         




class Board(Field):
    def __init__(self):
        #generate letters
        self.letters_list = list()
        for lt in letters_freq:
            self.letters_list.extend([lt[0] for i in range(lt[1])])
        np.random.shuffle(self.letters_list)

        #generate state of board
        self.board = np.empty(shape=(15,15), dtype=str)
        self.tmp_board = np.empty(shape=(15,15), dtype=str)
        self.directionx = []
        self.directiony = []

        self.liu = None

        #generate buttons
        self.fieldset = []

        for i in range(1,16):
            tmp_fieldset = []
            for j in range(1,16):
                if special_field(i,j) == "TWS":
                    tmp_fld = Field(i,j,'red', 0, 0)
                elif special_field(i,j) == "DLS":
                    tmp_fld = Field(i,j,'cyan', 0, 0)
                elif special_field(i,j) == "DWS":
                    tmp_fld = Field(i,j,'pink', 0, 0)
                elif special_field(i,j) == "TLS":
                    tmp_fld = Field(i,j,'blue', 0, 0)
                elif special_field(i,j) == "CNT":
                    tmp_fld = Field(i,j,'orange', 0, 0)
                else:
                    tmp_fld = Field(i,j,'white', 0, 0)
        
                tmp_fieldset.append(tmp_fld)
                
            self.fieldset.append(tmp_fieldset)
            


    
    #draw letters from resources
    def get_letters(self, no):
        temp_list = list()
        for i in range(no):
            drawn_letter = np.random.choice(self.letters_list)
            temp_list.extend(drawn_letter)
            self.letters_list.remove(drawn_letter)
        return temp_list





class Player_Field():
    def __init__(self, posy, bg, strvalue):
        self.txtvar = StringVar(value = strvalue)
        self.btn = Button(root, text="", width="4", bg=bg, textvariable=self.txtvar)
        self.btn['command'] = lambda:[self.on_click_lt()]
        self.btn.grid(row=17,column=posy)

    def on_destroy(self):
        self.btn.destroy()
        

    def on_click_lt(self):
        #if field is not blank - get letter

        if self.txtvar.get() != "" and B.liu is None:
            B.liu = self.txtvar.get()
            self.txtvar.set('')
        else:
            if B.liu is not None and self.txtvar.get() == "":
                self.txtvar.set(B.liu)
                B.liu = None




class Player(Player_Field):
    def __init__(self,name,score=0,pos=None):
        self.pos = pos
        self.name = name
        self.score = score
        self.letters_poss = []
        self.tmp_letter = []
        self.pl_btn_fld = []
        #generate score indicators for all players
        self.pl_lbl_txt_var = StringVar()
        self.pl_lbl_txt_var.set(self.name + ': ' + str(self.score))
        self.pl_lbl = Label(root, textvariable=self.pl_lbl_txt_var)
        self.pl_lbl.grid(row=self.pos, column=17)

        


    def generate_pl_let(self):
        self.pl_label = Label(root, text=self.name)
        self.pl_label.grid(row=16,column=1, columnspan=3)
        for k in range(1,8):
            self.tmp_pl_field = Player_Field(k, 'white', self.letters_poss[k-1])
            self.pl_btn_fld.append(self.tmp_pl_field)
        
        self.pl_end_btn = Button(root, text='KONIEC TURY', command=lambda:[self.destroy_pl_let()])
        self.pl_end_btn.grid(row=17,column=9, columnspan=4)

        self.pl_chkbox = Checkbutton(root, text="WYMIANA")
        self.pl_chkbox.grid(row = 17, column=13, columnspan=4)

    def destroy_pl_let(self):
        #destroy all widgets created for current player and change to the next player
        self.pl_chkbox.destroy()
        self.pl_end_btn.destroy()
        self.pl_label.destroy()
        for wdg in self.pl_btn_fld:
            wdg.on_destroy()

    def new_turn(self):
        if G.curr_player == G.no_players -1:
            G.curr_player = 0
            G.turn_state = True
            G.curr_turn += 1
        else:
            G.curr_player += 1
            G.turn_state = True
            G.curr_turn += 1
        
        
        










B = Board()


class Game():
    def __init__(self,no_players,turn_state=False):
        self.game_state = False
        self.turn_state = False
        self.pl_pool = []
        self.no_players = no_players
        self.curr_player = 0
        self.curr_word = []
        self.curr_turn = 0


        #create players for testing purposes
        tmp_player = Player(name="Andrzej", pos=1)
        self.pl_pool.append(tmp_player)
        tmp_player = Player(name="Adam", pos=2)
        self.pl_pool.append(tmp_player)

        

        # for i in range(int(no_players)):
        #     pl_name = simpledialog.askstring(prompt='Podaj imię gracza nr ' + str(i+1), title='Do dzieła!')
        #     tmp_player = Player(name=pl_name, pos=i+1)
        #    self.pl_pool.append(tmp_player)
        
    def players_turn(self):
        #check if number of letters is 0
        if len(self.pl_pool[self.curr_player].letters_poss) == 0:
            self.pl_pool[self.curr_player].letters_poss = B.get_letters(7)
            self.pl_pool[self.curr_player].generate_pl_let()
        else:
            self.pl_pool[self.curr_player].generate_pl_let()
            

        
            
        
        
   
        

       
        
        

G = Game(2)

G.players_turn()





if __name__ == "__main__":
    root.mainloop()