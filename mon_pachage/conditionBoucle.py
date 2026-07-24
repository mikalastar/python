#maximum de deux nombres
#print("programme qui calcule le maximum de deux nombres")
#a=int(input("donner le premier nombre: "))
#b=int(input("donner le deuxième nombre: "))
#if a>b:
#     print("le maximum est a",a)
#else:
#        print("le maximum est b",b)

#division de deux nombres
#a=int(input("donner le premier nombre: "))
#b=int(input("donner le deuxième nombre: "))
#if b==0:
#    print("la division par zéro n'est pas possible")
#else:
#    c=a/b
#    print("le résultat de la division est:",c)


#temperature=float(input("donner la température en degré Celsius: "))
#if temperature <0:
#   print("glace")
#elif temperature>100:
#    print("vapeur")
#else:
#    print("liquide")
#    input("appuyer sur une touche pour quitter")


#A = int ( input (" Veuillez entrer la valeur de A : " ) )
#B = int ( input (" Veuillez entrer la valeur de B : " ) )
#MAX = A if A > B else B
#print (" Le maximum est : ", MAX)

# multiplication d'un nombre int
#A= int(input("donner la valeur de A:"))
#print("la table de multiplication de",A)
#i=0
#while i<=10:
#    resultat=A*i
#    print(A,"*",i,"=",resultat)
#    i+=1

#A=int(input("entrer un nombre entre 10 et 20 : "))
#while A<10 or A>20:
#    if A<10:
#        print("Plus Grand!")
#    else:
#        print("Plus Petit!")
#    A=int(input("entrer un nombre entre 10 et 20 : "))
#print("Bravo vous avez entrer un nombre entre 10 et 20")
        #AUTRE VERSION 
#N=int(input("entrer un nombre entre 10 et 20:"))
#while N<10 or N>20:
#    print("erreur")
#    N=int(input("entrer un nombre entre 10 et 20:"))
#print("merci")

  #LA SOMME DES NOMBRES SUPERIEUR DE 1
#N=int(input("entrer un entier strictement superieur a 1 : "))
#while N<=1:
#    print("erreur!")
#    N=int(input("entrer un entier strictement superieur a 1 : "))
#r=0
#i=1
#while i<=N:
#    r=r+i
#    i+=1
#print("la somme de 1 a ",N,"est:" ,r)    


      #BREAK
#print("entrer 8 entiers:")
#s=0
#for i in range(8):
#    N=int(input("entrer un entier"+str(i+1)+":"))
#    #print(i) le programme vas just nous afficher l'indice par exemple je rentre le premier nombre il vas afficher que l'indice de ce nombre est 0
#    if N<0:
#        break
#    s=s+N
#print("la somme est:" , s)  

     #continue
print("entrer 8 entiers:")
s=0
for i in range(8):
    N=int(input("entrer un entier"+str(i+1)+":"))
    #print(i) le programme vas just nous afficher l'indice par exemple je rentre le premier nombre il vas afficher que l'indice de ce nombre est 0
    if N<0:
        continue
    s=s+N
print("la somme est:" , s)