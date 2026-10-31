# Boomerang Terrain

L'appli mobile des hôtesses et des superviseurs de Boomerang, et ce qui la relie à Odoo.

| Dossier | Contenu | État |
|---|---|---|
| `maquettes/` | Maquette cliquable des écrans (ouvrir `maquette.html` sur un téléphone) | prête à tester |
| `api/openapi.yaml` | Le contrat entre l'appli et Odoo : ce que l'appli demande, ce qu'Odoo répond | version 0.1.0, à relire |
| `docs/decisions.md` | Ce qui est décidé, ce qui reste à trancher | à jour |
| `odoo/boomerang_terrain/` | Le module Odoo (campagnes, agents, missions, pointages, rapports…) | à venir |
| `app/` | L'appli Flutter | à venir |

## Vérifier le contrat

```
pip install openapi-spec-validator
python3 scripts/verifier_contrat.py
```

## Première version (V1)

Connexion par téléphone + code à 4 chiffres, mission du jour, pointage (selfie + GPS), rapport avec
compteurs et photos, stock, signalement d'un problème, jours à payer, côté superviseur l'équipe du jour,
la validation et le remplacement, et dans Odoo le tableau de bord de la campagne.
