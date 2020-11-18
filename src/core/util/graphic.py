"""
    PROJET ALGORITHMIQUE 2

    author : T-Sai & Ethan


"""
from core.nonogram import Nonogram, CASE

from tkinter import Tk, Canvas, Frame, BOTH

class Fenetre(Frame):

    def __init__(self, taille=630):
        super().__init__()
        self.taille = taille
        self.canvas = Canvas(self)

    def draw_nonogram(self, n : Nonogram, ok : bool):
        if ok:
            self.master.title(f"Grille {n.id} colorie :")
        else :
            self.master.title(f"Grille {n.id} n'a pas pu etre entierement colorie :")
        self.pack(fill=BOTH, expand=2)
        grille = n.grille[:]

        for _ in range(3):
            grille = list(zip(*reversed(grille)))
        
        self.canvas.delete("all")
        
        ratioH = int(self.taille/n.M)
        ratioW = int(self.taille/n.N)
        diag = (ratioH ** 2 + ratioW ** 2)**0.5
        
        for i, l in enumerate(grille):
            for j, c in enumerate(l):
                if grille[i][j] == CASE.VIDE:
                     self.canvas.create_rectangle(i * ratioH, j * ratioW, (i * ratioH)+ diag, (j * ratioW)+ diag)
                     self.canvas.create_line(i * ratioH, (j * ratioW)+ diag)
                     self.canvas.create_line(j * ratioW, (i * ratioH)+ diag)
                if grille[i][j] == CASE.BLANC:
                    self.canvas.create_rectangle(i * ratioH, j * ratioW, (i * ratioH)+ diag, (j * ratioW)+ diag, outline="#000", fill="#FFF")
                if grille[i][j] == CASE.NOIR:
                    self.canvas.create_rectangle(i * ratioH, j * ratioW, (i * ratioH)+ diag, (j * ratioW)+ diag, outline="#000", fill="#000")
        
        self.canvas.pack(fill=BOTH, expand=1)
    
