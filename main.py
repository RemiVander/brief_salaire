from components import salaires


def menu():
    """Menu pour interface en ligne de commande."""
    filiales = salaires.get_name()
    filiales_str = " - ".join(filiales)
    while True:
        salaires.medium_salary()
        act = input(
            f"Bonjour \n De quelle filiale souhaitez-vous les détails? \n {filiales_str}"
            " \nTapez ALL pour tout voir \n"
            " \nTapez INFOS pour voir les salaires moyens\n"
            " \nTapez CSV pour générer un csv\n"
            " \nTapez 0 pour quitter \n"
        )
        if act == "0":
            print("Au revoir")
            break
        elif act == "ALL":
            salaires.print_details_employees()
        elif act == "INFOS":
            salaires.get_results_enterprises()
        elif act == "CSV":
            salaires.print_in_csv()
        else:
            salaires.print_details_one_enterprise(act)


menu()
