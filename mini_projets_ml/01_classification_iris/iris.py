# Mini projet 01 : classification des fleurs d'iris
# Objectif : deviner l'espèce d'une fleur à partir de la taille de ses pétales et sépales.

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# 1. Charger les données
iris = load_iris(as_frame=True)
df = iris.frame
df["espece"] = df["target"].map(dict(enumerate(iris.target_names)))

# 2. Explorer les données
print("Taille du tableau :", df.shape)
print(df.head())
print("\nNombre de fleurs par espèce :")
print(df["espece"].value_counts())

# 3. Séparer : 80% pour entraîner, 20% pour tester
X = iris.data      # les mesures (entrées)
y = iris.target    # l'espèce (ce qu'on veut prédire)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 4. Entraîner un modèle KNN (k plus proches voisins)
modele = KNeighborsClassifier(n_neighbors=5)
modele.fit(X_train, y_train)

# 5. Évaluer sur les données de test (jamais vues pendant l'entraînement)
predictions = modele.predict(X_test)
precision = accuracy_score(y_test, predictions)
print(f"\nPrécision du modèle : {precision:.2%}")

# Matrice de confusion : montre où le modèle se trompe
ConfusionMatrixDisplay.from_predictions(
    y_test, predictions, display_labels=iris.target_names
)
plt.title("Matrice de confusion - Iris")
plt.savefig("iris_confusion.png")
print("Graphique enregistré : iris_confusion.png")

# 6. Prédire une nouvelle fleur
# [longueur sépale, largeur sépale, longueur pétale, largeur pétale] en cm
nouvelle_fleur = pd.DataFrame([[5.1, 3.5, 1.4, 0.2]], columns=X.columns)
espece = modele.predict(nouvelle_fleur)[0]
print("Nouvelle fleur ->", iris.target_names[espece])

# A toi de jouer :
# - change n_neighbors (1, 3, 10...) et regarde si la précision change
# - essaie un autre modèle : from sklearn.tree import DecisionTreeClassifier
