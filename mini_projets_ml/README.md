# Mini projets Machine Learning

Petits projets pour apprendre le machine learning pas à pas avec Python.

## Installation

```bash
pip install -r mini_projets_ml/requirements.txt
```

## Projets

| # | Projet | Type | Ce qu'on apprend |
|---|--------|------|------------------|
| 01 | [Classification des fleurs d'iris](01_classification_iris/iris.py) | Classification | charger des données, train/test split, KNN, précision, matrice de confusion |
| 02 | [Prédire la progression du diabète](02_regression_diabete/diabete.py) | Régression | régression linéaire, erreur moyenne (MAE), score R² |

Lancer un projet :

```bash
python mini_projets_ml/01_classification_iris/iris.py
```

## Les étapes d'un projet ML (toujours les mêmes !)

1. **Charger** les données
2. **Explorer** les données (taille, colonnes, statistiques)
3. **Séparer** en données d'entraînement et de test
4. **Entraîner** un modèle
5. **Évaluer** le modèle sur les données de test
6. **Prédire** sur de nouvelles données

## Idées pour les prochains projets

- 03 : Détection de spam (texte → classification)
- 04 : Reconnaissance de chiffres manuscrits (`load_digits`)
- 05 : Regroupement de clients avec K-Means (apprentissage non supervisé)
- 06 : Survie du Titanic (nettoyage de données avec pandas)
