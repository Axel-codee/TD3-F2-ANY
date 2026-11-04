#! /usr/bin/env python3

"""Implémentation des files à l'aide de listes python """


class File:

    def __init__(self): 
        self.data = []

    def est_vide(self): 
        return self.data == []

    def premier(self) : 
        return self.data[0]
    
    def enfiler(self, x): 
        self.data.append(x)
    
    def defiler(self):
        return self.data.pop(0)
    
    def longueur(self): 
        return len(self.data)
    
    def afficher(self):
        print(self.data)


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
    
