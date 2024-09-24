"""
Berechne die Summe aller Zahlen von 1 bis n, die durch 3 teilbar sind. "n" kann dabei eine beliebig ausgewählte Zahl sein. (Hinweis: Lässt sich mit Modulo-Operator (%) lösen.)

Erstelle dazu zwei Dateien, eine mit einer Funktion, die die Summe berechnet und eine, die die Funktion aufruft und das Ergebnis ausgibt.

"""

import Tag2_berechnung


def summe(n):
    return Tag2_berechnung.sum_from_range(n)


if __name__ == "__main__":
    print(summe(10))
