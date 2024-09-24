"""
Schreiben Sie ein Python-Programm, das prüft, ob ein bestimmter Wert in einer Gruppe von Werten enthalten ist.
Testdaten :
3 -> [1, 5, 8, 3] : Wahr
-1 -> [1, 5, 8, 3] : Falsch
"""


def check_value_in_group(value, group):
    if type(group) != list and type(group) != tuple:
        raise TypeError("group must be a list")
    if value is None:
        raise TypeError("value must exist")
    return value in group


arr = [1, "3", 8, 3]

if check_value_in_group("3", arr):
    print("3 is in the group")
    # mein code wird mit der 3 oder liste mehr operationen druchführen...
    # ...
else:
    print("3 is not in the group")
    # mein programm stoppt hier
