from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine, delete, select


# 1. Refernz zum SQL-Table
# 2. Gleichzeitig eine Python-Klasse, die mit Python-nativen Typings arbeitet
class Hero(SQLModel, table=True):
    # Wenn optional, dann erstellt sqlmodel selbst eine ID nach "auto-increment" Prinzip
    # Man kann auch einen custom Primary Key definieren, dann muss man aber selbst aufpassen, dass man keine Einträge doppelt besetzt
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


hero1 = Hero(name="Deadpond")
hero2 = Hero(name="Spiderboi")


# Der Motor, der zwischen Python und der Datenbank sitzt und arbeitet
engine = create_engine("sqlite:///./heroes.db")  # -> wir verwenden SQLITE
# Registriert alle Tabellen, die wir in unserem Skript erstellen und erstellt diese in der Datenbank, wenn sie nicht existieren.
SQLModel.metadata.create_all(engine)


## Wir gehen die CRUD Operation durch...

# CREATE
with Session(engine) as session:
    session.add(hero1)
    session.add(hero2)
    session.commit()


# READ
with Session(engine) as session:
    # exec = execute command
    # all = alle Einträge, die einen Match hatten -> hier ist das die komplette Tabelle
    heroes = session.exec(select(Hero)).all()
    print("\nall heroes")
    for hero in heroes:
        print(hero)


with Session(engine) as session:
    # Ersten Eintrag auslesen
    hero = session.exec(select(Hero)).first()
    print("\nfirst hero:", hero)


# UPDATE
with Session(engine) as session:
    hero = session.exec(select(Hero).where(Hero.name == "Spiderboi")).first()
    if hero:
        hero.name = "Spiderkid"

        session.add(hero)
        session.commit()


# DELETE
# with Session(engine) as session:
#     # Einen Einträge löschen
#     hero = session.exec(select(Hero).where(Hero.name == "Spiderkid")).first()
#     if hero:
#         session.delete(hero)
#         session.commit()


with Session(engine) as session:
    # Alle Einträge löschen
    session.exec(delete(Hero))
    session.commit()


# Komplette Datenbank löschen
import os

db_url = "sqlite:///./heroes.db"  # Modify this to your actual database path

# Extract the actual file path from the database URL
db_path = db_url.replace("sqlite:///", "")

# Delete the database file
if os.path.exists(db_path):
    print("path to delete:", db_path)
    os.remove(db_path)
    print(f"Database {db_path} deleted.")
else:
    print(f"Database {db_path} does not exist.")
        