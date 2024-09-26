# Definieren der Dictionaries
#dic1 = {1: 10, 2: 20}
#dic2 = {3: 30, 4: 40}
#dic3 = {5: 50, 6: 60}

dic1 = {1: 10, 2: 20}
dic2 = {1: 30, 4: 40}
dic3 = {1: 50, 6: 60}

# Neues Dictionary erstellen
result = {}

# Funktion zum Hinzufügen eines Dictionaries in das result-Dictionary
def add_to_result(source_dict):
    for key, value in source_dict.items():
        if key not in result:
            result[key] = value
        else:
            print(f"Schlüssel {key} existiert bereits im result Dictionary!")

# Hinzufügen von dic1, dic2 und dic3
add_to_result(dic1)
add_to_result(dic2)
add_to_result(dic3)

# Ergebnis ausgeben
print("Ergebnis:", result)

"""
Write a Python script to concatenate the following dictionaries to create a new one.

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

Check if the given key already exists in the result dictionary.
"""

"""
def concat_dict(dict1, dict2, dict3) -> dict:
    result = dict1.copy()

    for key, value in dict2.items():
        if key not in result:
            result[key] = value

    for key, value in dict3.items():
        if key not in result:
            result[key] = value

    return result


dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}


res = concat_dict(dic1, dic2, dic3)
print(res)


dic1 = {1: 10, 2: 20}
dic2 = {1: 30, 4: 40}
dic3 = {1: 50, 6: 60}

res = concat_dict(dic1, dic2, dic3)
print(res)

"""