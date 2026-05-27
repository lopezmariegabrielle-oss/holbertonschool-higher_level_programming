#!/usr/bin/python3
"""
Module pour la sérialisation et la désérialisation de base avec JSON.
"""
import json


def serialize_and_save_to_file(data, filename):
    """Sérialise un dictionnaire et le sauvegarde dans un fichier JSON."""
    with open(filename, "w") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Charge et désérialise les données d'un fichier JSON."""
    with open(filename, "r") as file:
        return json.load(file)
