#!/usr/bin/python3
"""
Module pour convertir des données d'un fichier CSV vers le format JSON.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convertit un fichier CSV en fichier JSON nommé data.json."""
    try:
        with open(csv_filename, "r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            data_list = list(csv_reader)

        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data_list, file, indent=4)

        return True

    except Exception:
        return False
