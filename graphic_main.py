import streamlit as st
import pandas as pd
from components import salaires

salaires.print_in_csv()


def menu():
    """Menu pour interface graphique"""
    st.set_page_config(page_title="Répartition des employés", layout="wide")

    titles_tab = ["Données des employés", "Données des filiales"]
    tabs = st.tabs(titles_tab)

    with tabs[0]:
        print_employees()

    with tabs[1]:
        print_filiales()


def print_employees():
    """Fonction pour imprimer les employés depuis le csv employes.csv"""
    filiales = salaires.get_name()
    filiales.append("TOUT")
    file = pd.read_csv("employes.csv")
    option = st.selectbox(
        "De quelle filiale souhaitez-vous recevoir les données ?",
        options=filiales,
        index=None,
        placeholder="Veuillez choisir une option...",
    )

    if option:
        if option == "TOUT":
            st.dataframe(file)
        else:
            file_filtered = file[
                file["Nom"].isin([emp["name"] for emp in salaires.data[option]])
            ]
            file_filtered = file[
                file["Filiale"].isin([emp["filiale"] for emp in salaires.data[option]])
            ]
            st.dataframe(file_filtered)

    all_employees = [
        emp["name"] for filiale in salaires.data.values() for emp in filiale
    ]

    employe = st.text_input(
        "De quel employé souhaitez-vous recevoir les données ?",
        placeholder="Veuillez entrer un nom...",
    )

    if employe:
        matched = next(
            (name for name in all_employees if name.lower() == employe.lower()), None
        )  # va chercher le nom de l'employé qui correspond à celui demandé en évitant la casse
        if matched:
            df_employe = file[file["Nom"].str.lower() == matched.lower()]
            st.success(f"Données de {matched} :")
            st.dataframe(df_employe)
        else:
            st.warning("Aucun employé ne correspond à ce nom.")


def print_filiales():
    """Fonction pour afficher les données des filiales depuis le fichier filiales.csv"""
    salaries_filiales = pd.read_csv("filiales.csv")
    st.dataframe(salaries_filiales)


menu()
