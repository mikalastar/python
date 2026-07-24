#methode vs fonction
#la methode depend de l'objet qui l'appelle
# methode = nomListe.fonction(element)
# la syntaxe d'une fonction c'est : nomFonction( arg1 , arg2 , ... )
# la syntaxe d'une methode : nomObjet.nomMethode( arg1 , arg2 , ... )
# creation , ajout , suppression , operations , recherches , duplications

# 1 Creation
#creer une liste d'infos contenant des infos sur une chose
#nomListe = list (( 'ele1' , 'ele2' , '...' ))
infos = list (( 'Malika' , 19 , 2007 ))
print(infos)
#creer une liste qui nous donne des nombres aleatoire dans une liste 
#nomListe = list( range ( 'start' , 'stop' , 'step' ))
nbrsImp = list ( range ( 1 , 102 , 2 ))
print(nbrsImp)
# 2 Ajout
#Ajouter un seul element a la fin de la liste
#nomListe.append('element')
infos.append( 'Bejaia')  
print(infos)  
#Ajouter des elements genre une liste entiere ou bien un seule element a la fin d'une liste
#nomListe.extend('seq')
langues = list(( 'AR' , 'FR' ,'EN' ))
infos.extend( langues )
print(infos)
#Ajouter creer un element a un index specifié il vas pas ecraser l'ancienne valeur qui été
#nomListe.insert( 'index ' , 'element')
infos.insert( 2 , 'Algerie')
print(infos)

#suppression
#remove sans indexe
#nomListe.remove( 'element' )
#infos.remove( 'Algerie' )
#print(infos)

#pop avec l'index et donne le resultat de suppression
infos.pop( 1 )
print(infos)
#et si on veux supprimer et renvoyer la valeur on utilise une variable 
ville = infos.pop(2)
print(ville)

#clear elle supprime tout les element d'une liste
#nomListe.clear()
#infos.clear()
#print(infos)

# l'instruction del elle utilise l'indexe et la plage genre un ensemble 
#del nomListe[ index]
#del nomListe[plage  2:5 ]
#del infos[2]
#del infos[3:5]
#print(infos)

#operations

#len() fonction qui renvoie le nombre d'elements dans la liste 
#len(nomListe)
taille = len (infos)
print (taille)
#sum fonction qui calcule la somme des elements d'une liste
#sum(nomListe)
L1= list ((1,2,3,4,5,3,6,7,8,9,10))
sam = sum(L1)
print(sum(L1)/len(infos))
print(sam)

#max , min
print(max (L1))
print(min(L1))
#on peut avec les string le programme vas voir par rapport a l'ordre alphabetique
print(min(infos))
print(max(infos))

#count permet d'identifier combien de fois l'element specifié apparait dans la liste
#c'est une methode pas une fonction
print(L1.count(3))


#reverse inverser l'ordre des elements d'une liste
infos.reverse()
print(infos)

#sort
# trier les elements de la liste
#nomListe.sort(key=...,reverse=...) 
#les deux parametres key et reverse sont optionnels
#key : specifier les critaire de trie (par defaut : aucune)
#reverse : si la valeur de ce parametre est true la liste sera triée par ordre decroissant (par defaut : false)
#exemple

#fonction de recherche un element a partir de l'index
#index
#nomListe.index( element ,debut ou commencer la recherche presque c'est 0 ,fin )
L= ['a' ,'b' ,'c', 'd', 'e' , 'f' , 'a', 'b', 'c', 'd' , 'e' , 'f']
print(L.index('b'))
print(L.index('b',5)) #on commence a partir de l'indexe 5
#print(L.index('a',3 ,6)) #erreur parceque a n'est pas situer entre eux
#print(L.index('y')) # erreur il n'existe pas
print(L.index('c',4,10))

#duplication
#copy
l1= [1,2,3,5,4]
l2=l1
l1.append(6)
print(l1)
print(l2)

#exercice1
#on a changer de position de deux elements
P=['ALGERIE' , 'MAROC' , 'TUNISIE' ,'MALI' , 'FRANCE']
p1=input('premier pays : ')
p2=input('deuxieme pays : ')
i = P.index(p1)
j = P.index(p2)
print(P)
P[i],P[j]=P[j],P[i]
print(P)

#exercice2

analyse=[10,12,14.5,6,2.5]
algebre=[8,6.5,12,14.5,10.5]
probabilite=[9.5,14,12,15,13.5]
statistique=[19,20,10,19,18]
print(sum(analyse))
print(sum(algebre))
print(sum(probabilite))
print(sum(statistique))
print(len(analyse))
print(len(algebre))
print(len(probabilite))
print(len(statistique))
print(max(analyse))
print(max(algebre))
print(max(probabilite))
print(max(statistique))
print(min(analyse))
print(min(algebre))
print(min(probabilite))
print(min(statistique))
s=sum(analyse + algebre + probabilite +statistique)
print(s)
m=s/len(analyse+algebre+probabilite+statistique)
print(m)
mx=max(analyse+algebre+probabilite+statistique)
print(mx)
mn=min(analyse+algebre+probabilite+statistique)
print(mn)


#pour savoire si un element appartiens a une liste on fait 
L=['Apple' , 'BANANE' ,'ANANASSE' , 'ORANGE']
print('ORANGE'in L)
print('FRAISE' in L)
print('FRAISE' not in L)