#! /usr/bin/env python3

"""Listes simplement chaînées

TODO : 
Produire une version récursive de la fonction d’affichage 
Produire des fonctions calculant la taille de la liste en versions itératives et récursives
Tester pour des listes de taille vide, réduite à un élément ou plus longues
[BONUS] Permettre de pouvoir donner un nom à une liste
[BONUS] Ajouter un compteur permettant de savoir le nombre total de cellules produites pour gérer toutes les listes construites
"""

class Cellule:
    nombre_cellules_creees = 0

    @classmethod
    def afficher_nombre_cellules_creees(cls):
        print("Nb de cellules créees : " + str(cls.nombre_cellules_creees))

    def __init__(self, val, suiv=None):
        self.valeur = val   
        self.suivant = suiv
        Cellule.nombre_cellules_creees += 1

class ListeChainee:

    def renommer(self, nouveau_nom):
        self.nom_liste = nouveau_nom

    def __init__(self, nom="", n=None):
        self.nom_liste = nom
        self.tete = None

    def est_vide(self):
        return self.tete is None

    def cellule_tete(self):
        return self.tete

    def inserer_tete(self, val):
        nouvelle = Cellule(val, self.tete) 
        self.tete = nouvelle

    def supprimer_tete(self):      
        if self.tete is not None: 
            seconde = self.tete.suivant
            self.tete = seconde

    def afficher(self):
        print(f"Liste {self.nom_liste}: ", end="")
        courant = self.tete
        while courant is not None:
            print(courant.valeur, end=" -> ")
            courant = courant.suivant
        print("None")

    def afficher_recursif(self):
        def afficher_aux(cell) :
            if cell is None :
                print("None")
                return
            print(cell.valeur, end=" -> ")
            afficher_aux(cell.suivant)
        if self.tete is None: 
            print("Liste vide !")
        else:
            afficher_aux(self.tete)

    # Nombre de cellules en version itérative
    def longueur(self):
        dernier = self.tete
        l = 0
        while dernier != None : 
            l = l + 1
            dernier = dernier.suivant
        return l

    # Nombre de cellules en version récursive
    # utilisation d'une fonction locale
    def longueur_recursif(self):
        def longueur_rec(cell): 
            if cell is None:
                return 0
            else :
                l = 1 + longueur_rec(cell.suivant)
                return l
                
        if self.tete is None: 
            return 0
        else :
            return longueur_rec(self.tete)   


    def inserer_queue(self, val):
        nv_cell = Cellule(val)
        if self.tete is None:
            self.tete = nv_cell
            return

        dernier = self.tete
        while dernier.suivant is not None:
            dernier = dernier.suivant
        dernier.suivant = nv_cell


    def inserer_queue_recursif(self, val):
        nv_cell = Cellule(val)
        def inserer_queue_recursif_aux(cell):
            if cell.suivant is None: 
                cell.suivant = nv_cell
            else:
                inserer_queue_recursif_aux(cell.suivant)
        if self.tete is None:
            self.tete = nv_cell
        else: 
            inserer_queue_recursif_aux(self.tete)




    def supprimer_queue(self):
        if self.tete is None:
            return

        if self.tete.suivant is None:
            self.tete = None
            return

        courant = self.tete
        while courant.suivant.suivant is not None:
            courant = courant.suivant

        courant.suivant = None
    
    def supprimer_queue_recursif(self):
        def aux(cell):
            if cell.suivant is None:
                return None
            if cell.suivant.suivant is None:
                cell.suivant = None
                return cell
            cell.suivant = aux(cell.suivant)
            return cell

        if self.tete is None:
            return
        self.tete = aux(self.tete)



def tests():
    """"""
    L = ListeChainee()
    L.inserer_tete(10)
    L.inserer_tete(20)
    L.inserer_tete(30)

    L1 = ListeChainee()
    L1.inserer_tete(1)
    
    L2 = ListeChainee()

    L.afficher()
    L1.afficher()
    L2.afficher()

    L.afficher_recursif()
    L1.afficher_recursif()
    L2.afficher_recursif()

    print(L.longueur())
    print(L1.longueur())
    print(L2.longueur())

    print(L.longueur_recursif())
    print(L1.longueur_recursif())
    print(L2.longueur_recursif())

    L.supprimer_tete(); L.afficher()
    L.supprimer_tete(); L.afficher()
    L.supprimer_tete(); L.afficher()
    L.supprimer_tete(); L.afficher()

    L.inserer_tete(1); L.afficher()
    L.inserer_tete(2); L.afficher()
    L.inserer_tete(3); L.afficher()
    
    # BONUS
    L.supprimer_queue(); L.afficher()
    L.supprimer_queue(); L.afficher()
    L.supprimer_queue(); L.afficher()
    L.supprimer_queue(); L.afficher()

    L.inserer_queue(1); L.afficher()
    L.inserer_queue(2); L.afficher()
    L.inserer_queue(3); L.afficher()

    L.supprimer_queue_recursif(); L.afficher()
    L.supprimer_queue_recursif(); L.afficher()
    L.supprimer_queue_recursif(); L.afficher()
    L.supprimer_queue_recursif(); L.afficher()

    L.inserer_queue_recursif(1); L.afficher()
    L.inserer_queue_recursif(2); L.afficher()
    L.inserer_queue_recursif(3); L.afficher()


if __name__ == "__main__":
    tests()
