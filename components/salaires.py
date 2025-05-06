import json
import csv

with open("data/employes_data.json", "r", encoding="utf-8") as fichier_source:
    data = json.load(fichier_source)
from tabulate import tabulate


def get_name() -> list:
    """Renvoie la liste des filiales sous forme de liste"""
    return list(data.keys())


def calcul_salaire(taux: int, worked_hours: int, contract_hours: int) -> float:
    """Calcule le salaire mensuel avec majoration à 1.5x pour les heures supplémentaires, sur 4 semaines."""
    if worked_hours > contract_hours:
        heures_normales = contract_hours
        heures_sup = worked_hours - contract_hours
    else:
        heures_normales = worked_hours
        heures_sup = 0

    salaire_hebdo = (heures_normales * taux) + (heures_sup * taux * 1.5)
    salaire_mensuel = salaire_hebdo * 4
    return round(salaire_mensuel, 2)


# création des tableaux et objets qui serviront à stocker les données
salaires_globaux = []
stats_filiales = {}
stats_globales = []
all_employees = []


def medium_salary():
    """Pour chaque filiale, calcule le salaire des employés.
    Calcule le salaire moyen, affiche les salires mini et maxi par filiale, et enfin au global
    """
    for filiale, employes in data.items():
        salaires = []
        for emp in employes:
            salaire = calcul_salaire(
                emp["hourly_rate"], emp["weekly_hours_worked"], emp["contract_hours"]
            )
            salaires.append(salaire)
            salaires_globaux.append(salaire)

        stats_filiales[filiale] = {
            "salaire_moyen": round(sum(salaires) / len(salaires), 2),
            "salaire_min": min(salaires),
            "salaire_max": max(salaires),
        }

    stats_globales.append(
        {
            "salaire_moyen": round(sum(salaires_globaux) / len(salaires_globaux), 2),
            "salaire_min": min(salaires_globaux),
            "salaire_max": max(salaires_globaux),
        }
    )


def get_results_enterprises():
    """renvoie des informations sur les salaires dans les filiales"""
    for key, filiales in stats_filiales.items():
        print(
            f"{key}\n"
            f"Le salaire moyen est de :{filiales['salaire_moyen']} €\n"
            f"Le salaire minimum est de :{filiales['salaire_min']} €\n"
            f"Le salaire minimum est de :{filiales['salaire_max']} €\n"
        )


def print_details_employees():
    """affiche le détails de tous les employés"""
    all_employees = []
    to_print = []
    for key, employees in data.items():
        for emp in employees:
            all_employees.append(emp)

    for emp in all_employees:
        row = [
            emp["name"],
            emp["job"],
            emp["hourly_rate"],
            emp["weekly_hours_worked"],
            emp["contract_hours"],
        ]
        to_print.append(row)
    headers = ["Nom", "Poste", "Taux horaire", "Heures/semaine", "Heures contrat"]
    print(tabulate(to_print, headers=headers, tablefmt="pretty"))


def print_details_one_enterprise(name):
    """affiche le détail d'une fililiale. N'est pas sensible à la casse."""
    all_employees = []
    to_print = []
    for key, employees in data.items():
        if key.lower() == name.lower():
            for emp in employees:
                all_employees.append(emp)

            for emp in all_employees:
                row = [
                    emp["name"],
                    emp["job"],
                    emp["hourly_rate"],
                    emp["weekly_hours_worked"],
                    emp["contract_hours"],
                ]
                to_print.append(row)
            headers = [
                "Nom",
                "Poste",
                "Taux horaire",
                "Heures/semaine",
                "Heures contrat",
            ]
            print(tabulate(to_print, headers=headers, tablefmt="pretty"))
    else:
        pass


def print_in_csv():
    """Impression des données de toutes les filiales dans un fichier csv"""
    medium_salary()
    all_employees = []
    for key, employees in data.items():
        for emp in employees:
            emp["filiale"] = key
            all_employees.append(emp)

    with open("employes.csv", "w", newline="", encoding="utf-8") as f:
        ecrivain = csv.writer(f)
        headers = [
            "Filiale",
            "Nom",
            "Poste",
            "Taux horaire",
            "Heures/semaine",
            "Heures contrat",
            "Salaire",
        ]
        ecrivain.writerow(headers)

        for emp in all_employees:
            salaire = int(
                calcul_salaire(
                    emp["hourly_rate"],
                    emp["weekly_hours_worked"],
                    emp["contract_hours"],
                )
            )
            row = [
                emp["filiale"],
                emp["name"],
                emp["job"],
                emp["hourly_rate"],
                emp["weekly_hours_worked"],
                emp["contract_hours"],
                salaire,
            ]
            ecrivain.writerow(row)

    with open("filiales.csv", "w", newline="", encoding="utf-8") as f:
        ecrivain = csv.writer(f)

        ecrivain.writerow([])
        ecrivain.writerow(["Résumé des salaires par filiale"])
        headers = ["Filiale", "Salaire moyen", "Salaire mini", "Salaire maxi"]
        ecrivain.writerow(headers)

        for key, filiales in stats_filiales.items():
            row = [
                key,
                filiales["salaire_moyen"],
                filiales["salaire_min"],
                filiales["salaire_max"],
            ]
            ecrivain.writerow(row)

        ecrivain.writerow([])
        ecrivain.writerow(["Résumé des salaires de l'entreprise"])
        headers = ["Salaire moyen", "Salaire mini", "Salaire maxi"]
        ecrivain.writerow(headers)

        global_stats = stats_globales[0]
        row = [
            global_stats["salaire_moyen"],
            global_stats["salaire_min"],
            global_stats["salaire_max"],
        ]
        ecrivain.writerow(row)
        
