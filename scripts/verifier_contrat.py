#!/usr/bin/env python3
"""Vérifie que api/openapi.yaml est un contrat OpenAPI valide, sans texte coupé, que chaque PUT /…/{uuid} est rejouable (200 et 201)."""
import pathlib
import sys

import yaml
from openapi_spec_validator import validate

CONTRAT = pathlib.Path(__file__).resolve().parent.parent / "api" / "openapi.yaml"


def cles_vides(objet, chemin=""):
    """Une virgule non protégée dans un texte entre accolades crée une clé vide : on la signale."""
    if isinstance(objet, dict):
        for cle, valeur in objet.items():
            if valeur is None:
                yield f"{chemin}/{cle} : texte coupé par une virgule, le mettre entre apostrophes"
            yield from cles_vides(valeur, f"{chemin}/{cle}")
    elif isinstance(objet, list):
        for i, valeur in enumerate(objet):
            yield from cles_vides(valeur, f"{chemin}[{i}]")


def main():
    spec = yaml.safe_load(CONTRAT.read_text(encoding="utf-8"))
    validate(spec)
    erreurs = list(cles_vides(spec))
    for chemin, operations in spec["paths"].items():
        put = operations.get("put")
        if put and chemin.endswith("{uuid}") and not {"200", "201"} <= set(put["responses"]):
            erreurs.append(f"PUT {chemin} doit répondre 201 la première fois et 200 si déjà reçu")
    if erreurs:
        print("\n".join(erreurs))
        sys.exit(1)
    print(f"Contrat {spec['info']['version']} valide : {len(spec['paths'])} routes.")


if __name__ == "__main__":
    main()
