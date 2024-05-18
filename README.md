# Factorisation-LU

Ce code <code>python</code> servira à donner la factorisation d'une matrice carrée $A = (a_{ij})_{1\le i ,j\le n} \in \mathbb{M_n(R)}$ sous forme $A = L\cdot U$ avec $L \in \mathbb{M_n(R)}$ une matrice triangulaire <b>inférieure</b> dont la diagonale est formée par des $1$ ("Lower" pour $L$) et $U \in \mathbb{M_n(R)}$ ("Upper" pour $U$).

Pour l'execution, Il vous faut installer le package <b>Numpy</b>.

Ouvrir le Terminal et executer la commande suivante:
    
    pip install numpy

Voici l'algorithme de calcul:
 
-  On élimine le $a_{ij}$ coéfficient de la matrice mère, avec $j \le i$, multipliant à gauche par une matrice d'élimination $E_{ij}$, qui est définit par la matrice identité $I_n$ dont le coefficient à la $i^{ème}$ ligne et à la $j^{ème}$ colonne est remplacer par $- \dfrac{a_{ij}}{a_{jj}}$.
-  On obtient ainsi la matrice $U$.
-  L'inverse du produit des matrices d'élimination devient la matrice $L$
  
  Pour l'execution, tapez la commande:

    python main.py

La prochaine algorithme se portera sur l'algorithme de Crout

## ALgorithme de Crout
