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
