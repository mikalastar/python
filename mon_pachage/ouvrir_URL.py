#ouvrir URL d'un siteweb

#methode 1
import webbrowser # permet d'ouvrir le site directement dans le mon navigateur pas dans le terminal mon programme python ne recupere rien 
webbrowser.open("https://www.google.com/")

#methode 2
import urllib.request # permet de recuperer le contenu d'un site web et de l'afficher dans le terminal
#le programme envoie une requete http au site web et recupere le contenu
repense=urllib.request.urlopen("https://www.google.com/")
contenu=repense.read()
print(contenu)

#methode 3
import urllib.request
with urllib.request.urlopen('http://www.python.org/') as f:
    print(f.read(300)) # pour ne pas afficher tout le contenu du site web on peut mettre un nombre entre parenthese pour afficher que les 300 premiers caracteres