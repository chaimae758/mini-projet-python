import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Chargement des données 

df = pd.read_csv("data.csv", encoding='latin1')

# Affichage des premières lignes
print(" Premières lignes ")
print(df.head())

# Dimensions du dataset
print("\nDimensions ")
print(df.shape)

# Informations générales
print("\nInformations ")
print(df.info())

# Nettoyage 

# Supprimer les doublons
df.drop_duplicates(inplace=True)

#  Supprimer les valeurs manquantes
df.dropna(subset=['CustomerID', 'Description'], inplace=True)

# Supprimer quantités et prix négatifs
df = df[df['Quantity'] > 0]
df = df[df['UnitPrice'] > 0]

# Convertir la date
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Ajouter colonne TotalPrice
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

print("Shape après nettoyage:", df.shape)
print("Valeurs nulles:", df.isnull().sum().sum())
print(df.head())


#Analyse

#Statistiques générales
print(df[['Quantity', 'UnitPrice', 'TotalPrice']].describe())

#Top 5 pays
df.groupby('Country')['TotalPrice'].sum()\
  .sort_values(ascending=False).head(5)

#Top 5 produits
df.groupby('Description')['Quantity'].sum()\
  .sort_values(ascending=False).head(5)

#Ventes par mois

df['Month'] = df['InvoiceDate'].dt.month
print(df.groupby('Month')['TotalPrice'].sum().sort_values(ascending=False).head(5))


#Visualisation 

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('E-commerce Sales Analysis', fontsize=16, fontweight='bold')

#Top 5 Pays
top_countries = df.groupby('Country')['TotalPrice'].sum()\
                  .sort_values(ascending=False).head(5)
axes[0,0].bar(top_countries.index, top_countries.values,
              color=['#2196F3','#4CAF50','#FF9800','#E91E63','#9C27B0'])
axes[0,0].set_title('Top 5 Pays par CA')
axes[0,0].set_ylabel('Chiffre d affaires (€)')
axes[0,0].tick_params(axis='x', rotation=15)

#Evolution ventes par mois
monthly = df.groupby('Month')['TotalPrice'].sum()
axes[0,1].plot(monthly.index, monthly.values,
               marker='o', color='#2196F3', linewidth=2)
axes[0,1].fill_between(monthly.index, monthly.values,
                        alpha=0.2, color='#2196F3')
axes[0,1].set_title('Evolution des Ventes par Mois')
axes[0,1].set_xlabel('Mois')
axes[0,1].set_ylabel('CA (€)')
axes[0,1].set_xticks(range(1,13))

#Top 5 Produits
top_products = df.groupby('Description')['Quantity'].sum()\
                 .sort_values(ascending=False).head(5)
axes[1,0].barh(top_products.index, top_products.values, color='#4CAF50')
axes[1,0].set_title('Top 5 Produits les plus vendus')
axes[1,0].set_xlabel('Quantite vendue')

#Distribution des prix
axes[1,1].hist(df[df['UnitPrice'] < 20]['UnitPrice'],
               bins=40, color='#FF9800', edgecolor='white')
axes[1,1].set_title('Distribution des Prix')
axes[1,1].set_xlabel('Prix (€)')
axes[1,1].set_ylabel('Frequence')

plt.tight_layout()
plt.savefig('visualisation.png', dpi=150, bbox_inches='tight')
plt.show()



#Interprétation 

print("=" * 50)
print("CONCLUSIONS ET INTERPRÉTATION")
print("=" * 50)

#Marché principal
top_country = df.groupby('Country')['TotalPrice'].sum()\
                .sort_values(ascending=False).index[0]
top_ca = df.groupby('Country')['TotalPrice'].sum()\
           .sort_values(ascending=False).values[0]
print(f"\n1. MARCHÉ PRINCIPAL:")
print(f"   → {top_country} est le marché dominant")
print(f"   → CA total: {top_ca:,.2f} €")

#Meilleure période
best_month = df.groupby('Month')['TotalPrice'].sum().idxmax()
print(f"\n2. MEILLEURE PÉRIODE:")
print(f"   → Le mois {best_month} (Novembre) est le plus rentable")
print(f"   → Les ventes augmentent en fin d'année (fêtes)")

#Produit star
best_product = df.groupby('Description')['Quantity'].sum()\
                 .sort_values(ascending=False).index[0]
print(f"\n3. PRODUIT STAR:")
print(f"   → '{best_product}'")
print(f"   → C'est le produit le plus vendu en quantité")

#Prix
avg_price = df['UnitPrice'].mean()
avg_total = df['TotalPrice'].mean()
print(f"\n4. ANALYSE DES PRIX:")
print(f"   → Prix moyen par produit: {avg_price:.2f} €")
print(f"   → Panier moyen: {avg_total:.2f} €")
print(f"   → La majorité des produits coûtent moins de 5 €")

#Volume
print(f"\n5. VOLUME DES TRANSACTIONS:")
print(f"   → {len(df):,} transactions valides analysées")
print(f"   → {df['CustomerID'].nunique():,} clients uniques")
print(f"   → {df['Description'].nunique():,} produits différents")

print("\n" + "=" * 50)
print("FIN DE L'ANALYSE")
print("=" * 50)