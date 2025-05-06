# Projet de Gestion des Salaires et des Employés

## Description
Ce projet permet de calculer, afficher et exporter les informations relatives aux salaires des employés d'une entreprise, en fonction des données disponibles dans un fichier JSON. Il inclut également une interface graphique avec Streamlit pour afficher et analyser les informations sous forme de tableaux et de graphiques.

### Fonctionnalités :
- Calcul des salaires mensuels avec heures supplémentaires
- Affichage des salaires moyens, minimums et maximums par filiale
- Exportation des données en fichiers CSV
- Interface Streamlit pour l'affichage et la consultation des données

## Prérequis
Avant d'exécuter ce projet, vous devez avoir Python 3.6+ installé sur votre machine. Installez les packages suivants :

```bash
pip install -r requirements.txt
```

## Installation

1. Clonez ce repository sur votre machine locale :

```bash
git clone https://à-renseigner.git
```

2. Accédez au dossier du projet :

```bash
cd brief_salaires
```

3. Installez les dépendances nécessaires :

```bash
pip install -r requirements.txt
```

## Utilisation

### 1. Préparation des données
Le fichier `data/employes_data.json` doit contenir les données des employés sous la forme suivante:

```bash 
{
  "filiale_1": [
    {
      "name": "John Doe",
      "job": "Developpeur",
      "hourly_rate": 25,
      "weekly_hours_worked": 40,
      "contract_hours": 35
    },
    {
      "name": "Jane Doe",
      "job": "Designer",
      "hourly_rate": 20,
      "weekly_hours_worked": 38,
      "contract_hours": 35
    }
  ],
  "filiale_2": [
    {
      "name": "Alice Smith",
      "job": "Manager",
      "hourly_rate": 30,
      "weekly_hours_worked": 45,
      "contract_hours": 40
    }
  ]
}
```

### 2. Lancer l'application Streamlit
Lancez l'application avec :

```bash
streamlit run graphic_main.py
```

### 3. Fonctionnalités de l'interface graphique
- Affiche les données des employés et des salaires
- Filtre par nom ou par filiale

## Contribuer
Les contributions sont les bienvenues ! Pour contribuer, veuillez créer une "Pull Request".

## Licence
Ce projet est sous la licence [MIT](LICENSE).
