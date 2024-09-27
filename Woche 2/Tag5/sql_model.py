from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine, select


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
engine = create_engine("sqlite:///heroes.db")  # -> wir verwenden SQLITE
# Registriert alle Tabellen, die wir in unserem Skript erstellen und erstellt diese in der Datenbank, wenn sie nicht existieren.
SQLModel.metadata.create_all(engine)


## Wir gehen die CRUD Operation durch...

# CREATE
# with Session(engine) as session:
#     session.add(hero1)
#     session.add(hero2)
#     session.commit()


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
