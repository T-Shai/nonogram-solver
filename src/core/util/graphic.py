"""
    PROJET ALGORITHMIQUE 2

    author : T-Sai & Ethan

    classe fenetre gerant l'affichage graphic
    avec tkinter
"""
from core.nonogram import Nonogram, CASE

from tkinter import Tk, Canvas, Frame, BOTH

class Fenetre(Frame):

    def __init__(self, taille=630):
        super().__init__()
        self.taille = taille
        self.canvas = Canvas(self)

    def matrixflip(m,d):
        tempm = m.copy()
        if d=='h':
            for i in range(0,len(tempm),1):
                    tempm[i].reverse()
        elif d=='v':
            tempm.reverse()
        return(tempm)

    def draw_nonogram(self, n : Nonogram, ok : bool):
        if ok:
            self.master.title(f"Grille {n.id} colorie :")
        else :
            self.master.title(f"Grille {n.id} n'a pas pu etre entierement colorie :")
        self.pack(fill=BOTH, expand=2)
        grille = Fenetre.matrixflip(n.grille, "h")

        for _ in range(3):
            grille = list(zip(*reversed(grille)))
        
        self.canvas.delete("all")
        
        ratio = int(max(self.taille/n.M, self.taille/n.N))
        diag = int(ratio * (2**0.5))
        for i, l in enumerate(grille):
            for j, c in enumerate(l):
                if grille[i][j] == CASE.VIDE:
                     self.canvas.create_rectangle(i * ratio, j * ratio, (i * ratio)+ diag, (j * ratio)+ diag, outline="#000", fill="#F00")
                if grille[i][j] == CASE.BLANC:
                    self.canvas.create_rectangle(i * ratio, j * ratio, (i * ratio)+ diag, (j * ratio)+ diag, outline="#000", fill="#FFF")
                if grille[i][j] == CASE.NOIR:
                    self.canvas.create_rectangle(i * ratio, j * ratio, (i * ratio)+ diag, (j * ratio)+ diag, outline="#000", fill="#000")
        
        self.canvas.pack(fill=BOTH, expand=1)
    
