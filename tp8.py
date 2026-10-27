import pandas as pd

#_recuperation des fichiers
df = pd.read_csv("qualite_industrielle - qualite_industrielle.csv")
print(df)
#nmbr ligne et col
print(df.shape)

#5premiere ligne
print(df.head())

# noms des colonmes
print(df.columns)
# infos sur data
print(df.info())
#verifer sil manque
print(df.isnull().sum())
#verifier les douubles
print(df.duplicated().sum())
#status
print(df.describe())
#nombre de chaque entite dans la colonme 
print(df["Produit"].value_counts())
print(df["Ligne_Production"].value_counts())
print(df["Resultat"].value_counts())

# Taux de défauts moyen par produit et par ligne
print(df.groupby("Produit")["Taux_Defauts_pct"].mean()) # group by --> regroupent des lignes / mean --> moyenne
print(df.groupby("Ligne_Production")["Taux_Defauts_pct"].mean())

# -------Nettoyage ----------
df = df.drop_duplicates() #supp des doublons
df = df.dropna()   #supp des manquants


#---sauvegarde--
df.to_csv("qualite_industrielle_net.csv" , index=False) #pour ne pas ajouter les indices 

import numpy as np
import matplotlib.pyplot as plt

plt.figure()# pour les trois s'affiche
plt.hist(df["Taux_Defauts_pct"], bins=10 , edgecolor="black")
plt.title("Répartition du taux de défauts")
plt.xlabel("Taux de défauts (%)")
plt.ylabel("Nombre de contrôles")


plt.figure()
moyennes = df.groupby("Ligne_Production")["Taux_Defauts_pct"].mean() #Taux de défauts moyen par lign
moyennes.plot(kind="bar", edgecolor="black")  # trace le diagramme en barres des moyennes
plt.title("Taux de défauts moyen par ligne de production")
plt.xlabel("Ligne de production")
plt.ylabel("Taux de défauts moyen (%)")
plt.xticks(rotation = 0)

plt.figure()
for resultat, groupe in df.groupby("Resultat"):
    plt.scatter(groupe["Nb_Defauts"], groupe["Cout_Non_Qualite_DH"], label=resultat)
plt.title("Coût de non-qualité selon le nombre de défauts")
plt.xlabel("Nombre de défauts")
plt.ylabel("Coût de non-qualité (DH)")
plt.legend()
 
plt.show()
 