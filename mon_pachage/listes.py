#exo1
lettres=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lettres[:]#il va afficher toute la liste mais il la pas fait je sais pas pourquoi et j'ai la flemme de le savoir 
print(lettres[12] , lettres[8] , lettres[10] , lettres[0]) 
print(lettres[0:5]) #decoupage pour afficher les 4 premiers
#print(lettres[0,5]) on peut pas 
print(lettres[0] , lettres[2]) # affichage avec indexation
print(lettres[:4]) #affichage avec decoupage
print(lettres[0::3]) # les :: veux dire le pas 3
#exo2
semaine=['lundi','mardi','mercredi','jeudi','vendredi','samedi','dimanche']
print(semaine)
print(semaine[0], semaine[-7])
print('les deux jours de weekend sont :', semaine[-2], 'et', semaine[-1])

#exo3
n=int(input('entrer un nombre positive : '))
while n<0 :
    n=int(input('entrer un nombre positive : '))
N=list(range(1,n+1))
print(N)
P=list(range(0,n+1,2))
print(P)
I=list(range(1,n+1,2))
print(I) 

#operations sur les listes 
#concaténation
L1=[2,7,24,78]
L2=[15,2,-6,9]
L=L1 + L2
print(L)
#répétition
L=[4,2,9]
L*=3
print(L)
#comparaison
L1=[3,4,-5,10]
L2=[3,4,-5,10]
print(L1>=L2)
print(L1==L2)
print(L1<L2)
print(L1!=L2)

# le decoupage permet d'extraire une partie d'une liste  sans utiliser une boucle
#liste[debut:fin]
#lettres[:5]      # du début jusqu'à l'index 4 (équivalent à lettres[0:5])
#ettres[5:]      # de l'index 5 jusqu'à la fin
#ettres[:]       # toute la liste (une copie complète)
#lettres[debut:fin:pas]
#lettre[-3:]les 3derniers elements
#lettres[:-3] tout sauf les trois derniers 
