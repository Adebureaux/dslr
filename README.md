# Prédiction des maisons de Hogwarts — Logistic Regression

## Présentation du projet

Ce projet a pour objectif de prédire la **maison de Hogwarts** d’un élève à partir de ses notes et de certaines informations personnelles, en utilisant une **régression logistique multi-classe (one-vs-all)** implémentée **from scratch**.

Aucune bibliothèque de machine learning (comme scikit-learn) n’est utilisée.  
L’entraînement repose uniquement sur des **outils mathématiques implémentés manuellement** et sur la **descente de gradient**.

---

## Structure du projet
.
├── datasets/
│   ├── dataset_test.csv
│   └── dataset_train.csv
│
├── src/
│   ├── config/
│   │   └── constants.py
│   ├── stats/
│   │   └── descriptive.py
│   ├── utils/
│   │   └── parser.py
│
├── describe.py
├── histogram.py
├── logreg_predict.py
├── logreg_train.py
├── pair_plot.py
├── requirements.txt
├── scatter_plot.py
└── README.md


## Notions

La regression logistique permet la classification de données selon plusieurs categories

L'entrainement des poids d'un modèle de regression logistique se fait par répétition:
* Prédictions
* Auto-évaluation des resultats
* Adaptation des poids du modèle

Une fois que n_répétitions ont été réalisées, les poids sont sauvegardés et utilisés ensuite comme modèle définitif.

### L'importance des paramètres dans la recherche de performances:
* Trop ou pas assez entrainer son modèle (n_repetition): Risques de modèle sur ou sous entrainé (on parle de modèle overfitté lorsque ce dernier ne devient compétent que sur le set de données sur lequel il a été entrainé)
* Evaluation sur un set de données utilisé pour l´entrainement: évaluation faussée.
* Learning rate: un learning rate trop petit peut allourdir et rallonger l'entrainement et risquer d'overfitter le modèle, un learning rate trop grande présente le risque de ne jamais trouver le point le plus bas recherché lors de la descente de grandient.
