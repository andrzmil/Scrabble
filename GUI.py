from ast import Str
from tkinter import *

import numpy as np
import random
from LOGIC import *


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
        if self.txtvar.get() == "" and B.liu is not None:

            self.txtvar.set(B.liu)
            B.board[self.posx-1][self.posy-1] = B.liu
            
            B.liu = None
            print(B.board)
            print(P.letters_poss)

        else:
            if B.liu is None and self.txtvar.get() != "":
                B.board[self.posx-1][self.posy-1] = ''
                B.liu = self.txtvar.get()
                self.txtvar.set('')
                print(B.board)




class Board(Field):
    def __init__(self):
        #generate letters
        self.letters_list = list()
        for lt in letters_freq:
            self.letters_list.extend([lt[0] for i in range(lt[1])])
        np.random.shuffle(self.letters_list)

        #generate state of board
        self.board = np.empty(shape=(15,15), dtype=str)

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

            print(B.liu)
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
        
        pl_end_btn = Button(text='KONIEC TURY')
        pl_end_btn.grid(row=17,column=9, columnspan=5)
            # tmp_pl_btn_var = StringVar(value=self.letters_poss[k-1])
            # tmp_pl_btn = Button(root, width="4", textvariable=tmp_pl_btn_var, command=lambda:[self.on_click_lt()])
            # tmp_pl_btn.grid(row=17,column=k)
            # self.pl_btn_fld.append(tmp_pl_btn)
            # self.pl_btn_var_fld.append(tmp_pl_btn_var)






B = Board()



P = Player("Zbyszek",pos=1)
P.letters_poss = B.get_letters(7)


P.generate_pl_let()



if __name__ == "__main__":
    root.mainloop()