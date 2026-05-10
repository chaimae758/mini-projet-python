# Mini-Projet Python – Analyse E-commerce Sales Data

## Description
Analyse complète d'un dataset E-commerce réel avec Python.  
Dataset source : [Kaggle – E-commerce Data](https://www.kaggle.com/datasets/carrie1/ecommerce-data)

## Objectif
Analyser les ventes d'une boutique en ligne britannique (2010-2011)  
pour identifier les tendances, les produits stars et les marchés principaux.

## Dataset
- **Source** : Kaggle
- **Lignes** : 541,909 (392,692 après nettoyage)
- **Colonnes** : 8 variables (InvoiceNo, Quantity, UnitPrice, Country...)

## Structure du projet

mini-projet-python/
├── data.csv                  # Dataset original
├── projet_ecommerce.py       # Code Python complet
├── rapport_ecommerce.docx    # Rapport final
└── visualisation.png         # Graphiques générés


## Étapes réalisées
- **STEP 1** – Chargement des données
- **STEP 2** – Nettoyage (doublons, valeurs manquantes, types)
- **STEP 3** – Analyse (statistiques, groupby, tendances)
- **STEP 4** – Visualisation (4 graphiques Matplotlib)
- **STEP 5** – Interprétation et conclusions

## Résultats principaux
| Indicateur | Valeur |
|---|---|
| Transactions analysées | 392,692 |
| Meilleur marché | United Kingdom (7,285,024 €) |
| Meilleur mois | Novembre (1,156,205 €) |
| Panier moyen | 22.63 € |
| Clients uniques | 4,339 |

## Technologies utilisées
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-green)
![NumPy](https://img.shields.io/badge/NumPy-orange)
![Matplotlib](https://img.shields.io/badge/Matplotlib-red)

## Installation
```bash
pip install pandas numpy matplotlib
python projet_ecommerce.py
```
