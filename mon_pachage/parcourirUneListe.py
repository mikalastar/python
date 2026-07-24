#parcourir une liste 
#avec for
#quand on a la liste prete
#for element in nomListe :
infos =['Anas' , 'Radi' , 2000 , 'France' , 'Paris']
for Radi in infos :
    print(Radi)

#avec for et rang il nous afficheles elements de la liste avec leurs indice
#on peux modifier la liste comparer les elements par leurs positions l'index
for i in range(len(infos)):
    print( i+1,'est:', infos[i] )

#avec for et enumerateil nous afficheles elements de la liste avec leurs indice
for i , v in enumerate(infos , start=1) :
    print(i , ' ' , v)

#avec while on peux l'utiliser si on veux un break
#i=0
#while i < len(infos) :
    #print(infos[i])
    #i+=1


#avec for et zip
#parcourir les elements de deux ou plusieurs listes 
#la boucle s'arretera au dernier element de la liste ayant le plus petit nombre d'element
fruits = ['pomme' , 'ananas' , 'banane']
prix = [ 12.5 , 14.8 ,11.9]
etat= [ 'bon' ,'tres bien ' , 'exellent']
for fruits , prix,etat  in zip(fruits , prix , etat):
    print(fruits ,':' , prix ,' €',etat)


#note =[]
#pour remplir la liste
#for i in range (5):
#    print('donner la note num ',i+1,':', end='' )
  # note.append(float(input()))
   #pour parcourrir la liste
#for v in note :
#    print('la note de l etudiant num ' , i , 'est : ', v)  



x=int(input('donner la valeur de x :'))
L=[]
for i in range (5) :
    print('l[' , i+1 , '] =' , end='' )
    L.append(int(input()))
if x in L:
    print(x,'se touve dans L')
else:
    print(x,'ne se trouve pas dans L')


L=[]
for i in range (5) :
    print('l[' , i+1 , '] =' , end='' )
    L.append(int(input()))
print('le max est : ',max(L))

nom= []
matier1=[]
matier2=[]
for i in range (5) :
    print('nom[' , i+1 , '] =' , end='' )
    nom.append((input(' nom : ')))
    m1.append(float(input('m1 : ')))
    m2.append(float(input('')))
for nom , m1 , m2 in zip(nom,m1,m2):
    print(nom , 'a eu' ,(m1+m2)/2)