# Boomerang Terrain — repères pour Claude

- **Boomerang** (boomerang.sn) est une agence de campagnes terrain au Sénégal. **Aucun lien avec TAAGG** :
  autre entreprise, autre base Odoo, autres données. Ne rien reprendre ni écrire dans `taagg-odoo`.
- Babacar travaille en français, seul avec Claude : explications simples, sans jargon, petites étapes
  (à chaque étape : ce qui marche, comment le tester, ce qui reste).
- **Aucun secret dans le dépôt** (clés, mots de passe, numéros réels restent sur le serveur).
- Ordre de travail : contrat `api/openapi.yaml` d'abord, puis le module Odoo `boomerang_terrain`, puis l'appli Flutter.
  Après toute modification du contrat : `python3 scripts/verifier_contrat.py`.
- Les agents lisent et écrivent peu : grandes icônes, couleurs (vert fait, orange à faire, rouge problème),
  bouton « écouter » (voix enregistrées en français et en wolof), presque rien à taper.
- L'appli marche **hors connexion** : tout objet créé sur le téléphone a un identifiant `uuid` choisi par le
  téléphone et part par un `PUT` qu'on peut rejouer sans créer de doublon.
- Odoo Community 20 : droits dans `security/ir.access.csv` (modèle `ir.access`), `ir.config_parameter.get_str/get_int`.
- Données personnelles : loi sénégalaise 2008-12 (CDP). Accord de l'agent pour selfie et GPS ;
  durées de conservation dans `docs/decisions.md`.
- Décisions prises et questions ouvertes : `docs/decisions.md`.
