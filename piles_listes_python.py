#! /usr/bin/env python3

"""Implémentation des piles à l'aide de listes python """


class Pile:
    
    def __init__(self): self.data = []
    
    def est_vide(self):
        if len(self.data) < 1 :
            return True
        else : 
            return False
    
    def sommet(self):
        return self.data[-1]

    def empiler(self, x): 
        self.data.append(x)
    
    def depiler(self):
        depile = self.data.pop()
        return depile
    
    def longueur(self): 
        return len(self.data)
    
    def afficher(self):
        print(self.data)

if __name__ == "__main__":
    p1 = Pile()
    p1.empiler(1)
    p1.empiler(2)
    p1.empiler(3)
    p1. afficher()
    
    v = p1.depiler(); print("Extrait : " + str(v))
    v = p1.depiler(); print("Extrait : " + str(v))
    v = p1.depiler(); print("Extrait : " + str(v))
    p1. afficher()
