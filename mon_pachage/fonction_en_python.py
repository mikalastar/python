#les fonctions 
#DECLARATION DES FONCTIONS
A=int(input("donner une valeur de A:"))
B=int(input("donner une valeur de B:"))
def meme_signe(A,B) :
    if A>0 and B>0 or A<0 and B<0:
        print("les deux nombres ont le meme signe")
    else:
        print("les deux nombres n'ont pas le meme signe")
def min(A,B) :
    if A<B :
        min = A
    else:
        min = B
        return min   
def max(A,B) :
    if A>B :
        max = A
    else:
        max = B
        return max     
#APPEL DES FONCTIONS
meme_signe(A,B)
print("le minimum est:", min(A,B))
print("le maximum est:", max(A,B))


##calculatrice

def addition(a,b):
    return a+b
def soustraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    if b==0:
        return "Error: Division by zero"
    else:
        return a/b
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print("Addition: ", addition(a, b))
print("Subtraction: ", soustraction(a, b))
print("Multiplication: ", multiplication(a, b))
print("Division: ", division(a, b))


import math
print("Square root of 16:", math.sqrt(16))
print("GCD of 48 and 18:", math.gcd(48, 18))                                          