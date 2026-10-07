# Mini projet 02 : régression sur le diabète
# Objectif : prédire un nombre (la progression de la maladie après 1 an)
# à partir de mesures médicales (âge, IMC, tension...).

import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

# 1. Charger les données
diabete = load_diabetes(as_frame=True)
X = diabete.data
y = diabete.target

# 2. Explorer les données
print("Taille du tableau :", X.shape)
print(X.head())
print("\nStatistiques de la cible :")
print(y.describe())

# 3. Séparer en entraînement / test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Entraîner une régression linéaire
modele = LinearRegression()
modele.fit(X_train, y_train)

# 5. Évaluer
predictions = modele.predict(X_test)
print(f"\nErreur moyenne (MAE) : {mean_absolute_error(y_test, predictions):.1f}")
print(f"Score R² : {r2_score(y_test, predictions):.2f}  (1 = parfait, 0 = nul)")

# Quelles colonnes comptent le plus ?
print("\nPoids de chaque colonne :")
for colonne, poids in sorted(zip(X.columns, modele.coef_), key=lambda c: -abs(c[1])):
    print(f"  {colonne:>4} : {poids:8.1f}")

# Graphique : valeurs réelles vs prédites (idéal = points sur la diagonale)
plt.scatter(y_test, predictions, alpha=0.6)
plt.plot([y.min(), y.max()], [y.min(), y.max()], "r--")
plt.xlabel("Valeur réelle")
plt.ylabel("Valeur prédite")
plt.title("Régression linéaire - Diabète")
plt.savefig("diabete_predictions.png")
print("Graphique enregistré : diabete_predictions.png")

# A toi de jouer :
# - essaie : from sklearn.ensemble import RandomForestRegressor
# - garde seulement la colonne "bmi" et compare le score R²
