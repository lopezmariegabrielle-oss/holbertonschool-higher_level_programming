#!/usr/bin/python3
"""
Module pour la sérialisation et désérialisation en XML.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Sérialise un dictionnaire en XML et l'enregistre dans un fichier."""
    try:
        root = ET.Element("data")
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

        return True
    except Exception:
        return False


def deserialize_from_xml(filename):
    """Lit un fichier XML et renvoie un dictionnaire Python."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text

        return result
    except Exception as e:
        print(f"Erreur sérialisation : {e}")
        return False