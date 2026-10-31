#!/usr/bin/env python3
"""Vérifie que api/openapi.yaml est un contrat OpenAPI valide et que chaque PUT /…/{uuid} est rejouable (200 et 201)."""
import pathlib
import sys

import yaml
from openapi_spec_validator import validate

CONTRAT = pathlib.Path(__file__).resolve().parent.parent / "api" / "openapi.yaml"


def main():
    spec = yaml.safe_load(CONTRAT.read_text(encoding="utf-8"))
    validate(spec)
    erreurs = []
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
