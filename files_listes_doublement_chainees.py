#! /usr/bin/env python3

"""Implémentation des files à l'aide de listes doublement chainées """

from listes_doublement_chainees import ListeDoublementChainee

class File:

    def __init__(self): 
        self.data = ListeDoublementChainee()

    def est_vide(self): 
        return self.data.est_vide()
    
    def premier(self) : 
        if self.est_vide() : 
            return "La file est vide !"
        else : 
            return self.data.tete.valeur
    
    def enfiler(self, x): 
        self.data.inserer_queue(x)
    
    def defiler(self):
        val = self.premier()
        self.data.supprimer_tete()
        return val
    
    def longueur(self): 
        return self.data.longueur()
    
    def afficher(self):
        self.data.afficher()


if __name__ == "__main__":
    p1 = File() 
    p1.enfiler(1)
    p1.enfiler(2)
    p1.enfiler(3)
    p1.afficher()
    
    v = p1.defiler(); print("Extrait : " + str(v))
    v = p1.defiler(); print("Extrait : " + str(v))
    v = p1.defiler(); print("Extrait : " + str(v))
    p1.afficher()
    
