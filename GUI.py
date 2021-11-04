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
    def __init__(self, posx, posy, bg, bonus, state):
        self.posx = posx
        self.posy = posy
        self.bonus = bonus
        self.state = state
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



        if self.txtvar.get() == "" and B.liu is not None and (if_move_possible.get('') != 4 or bl == 225):

            self.txtvar.set(B.liu)
            B.tmp_board[self.posx-1][self.posy-1] = B.liu
            B.directionx.append(self.posx-1)
            B.directiony.append(self.posy-1)
            B.liu = None
            print(B.board)
            print(B.directionx)
            print(B.directiony)
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
        self.name = name
        self.score = score
        self.letters_poss = list()
        self.tmp_letter = []
        self.pl_btn_fld = []
        self.pl_lbl_txt_var = StringVar()
        self.pl_lbl_txt_var.set(self.name + ': ' + str(self.score))
        self.pl_lbl = Label(root, textvariable=self.pl_lbl_txt_var)
        self.pl_lbl.grid(row=pos, column=17)

        global pl_dropped_letters


    def generate_pl_let(self):
        pl_label = Label(text=self.name)
        pl_label.grid(row=16,column=1, columnspan=3)
        for k in range(1,8):
            tmp_pl_field = Player_Field(k, 'white', self.letters_poss[k-1])
            self.pl_btn_fld.append(tmp_pl_field)
        
        self.pl_end_btn = Button(text='KONIEC TURY')
        self.pl_end_btn.grid(row=17,column=9, columnspan=4)

        self.pl_chkbox = Checkbutton(text="WYMIANA")
        self.pl_chkbox.grid(row = 17, column=13, columnspan=4)

    def destroy_pl_let(self):
        self.pl_chkbox.destroy()
        self.pl_end_btn.destroy()
        
        
        










B = Board()


class Game():
    def __init__(self,no_players,turn_state=False):
        self.turn_state = False
        self.pl_pool = []
        self.no_players = no_players
        self.curr_player = 0
        self.curr_word = []
        for i in range(int(no_players)):
            pl_name = simpledialog.askstring(prompt='Podaj imię gracza nr ' + str(i+1), title='Do dzieła!')
            tmp_player = Player(name=pl_name, pos=i+1)
            self.pl_pool.append(tmp_player)
        np.random.shuffle(self.pl_pool)


            


        self.pl_pool[self.curr_player].letters_poss = B.get_letters(7)
        self.pl_pool[self.curr_player].generate_pl_let()
        a = simpledialog.askstring(title='aaaa', prompt='aaaaa')
        self.pl_pool[self.curr_player].destroy_pl_let()
        

G = Game(2)



# P = Player("Zbyszek",pos=1)
# P.generate_pl_let()
# P.letters_poss = B.get_letters(7)

if __name__ == "__main__":
    root.mainloop()