
import controller
import db
import pandas as pd


if __name__ == "__main__":
    # 0. Erstmal DB initialisieren
    db.initialize_db()

    while True:
        user_input = input(
            "\nWelchen Befehl willst du ausführen (scrape, retrieve oder export)?\n"
        )

        if user_input == "scrape":
            # Webscraper laufen lassen
            controller.scrape_new_products()
        elif user_input == "retrieve":
            # Daten von DB auslesen
            data = controller.retrieve_data()

            # 1. Daten in Pandas DataFrame überführen
            df = pd.DataFrame(data)

            # Daten anzeigen
            print(df)
        elif user_input == "export":
            # Daten von DB auslesen
            data = controller.retrieve_data()

            # 1. Daten in Pandas DataFrame überführen
            df = pd.DataFrame(data)

            # 2. Daten als CSV ausgeben
            df.to_csv('products.csv', index=False)

            print("Daten wurden als CSV exportiert.")
        else:
            print("Keine gültige Eingabe...")
           



# What now? - Potentielle Aufgaben für den Nachmittag
# 1. Daten in Pandas Dataframe überführen
# 2. Daten als CSV ausgeben
# 3. Nur Produkte einer Kategorie heraussuchen
# 4. Produkte nach Filtern heraussuchen
# 5. DB - Update
# 6. DB - Delete
# 7. DB erweitern
#   - Historie von Produktdaten
#   - Created Date erstellen
#   - Mehr Datenpunkte scrapen

