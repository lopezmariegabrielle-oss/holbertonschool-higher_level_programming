#!/usr/bin/python3
"""
Module pour la sérialisation d'objets personnalisés avec pickle.
"""
import pickle


class CustomObject:
    """Classe représentant un objet personnalisé à sérialiser."""
    def __init__(self, name, age, is_student):
        """Initialise les attributs de l'objet."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Is Student: {self.is_student}"
        )

    def serialize(self, filename):
        """Sérialise l'instance actuelle avec pickle."""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Charge et retourne une instance de CustomObject depuis un fichier"""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception:
            return None
