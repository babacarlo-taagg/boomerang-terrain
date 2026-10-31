# Décisions et questions ouvertes

*Mis à jour le 31 octobre 2026.*

## Décidé avec Babacar

| Sujet | Décision |
|---|---|
| Entreprise | Boomerang est indépendante de TAAGG : base Odoo à part, dépôts à part |
| Dépôt | `boomerang-terrain` : maquettes, contrat de l'API, module Odoo, appli |
| Technologie de l'appli | Flutter (Android d'entrée de gamme, hors connexion, photo, micro, GPS) |
| Téléphones | Chaque agent a son propre téléphone Android |
| Taille | Environ 100 hôtesses par campagne |
| Connexion | Numéro de téléphone + code à 4 chiffres. Le bureau donne un code provisoire depuis Odoo (aussi pour remettre à zéro un code oublié) ; à la première connexion l'agent choisit son propre code |
| Voix | Chaque phrase de l'appli a une voix française et une voix wolof, enregistrées ou déposées par le bureau dans Odoo, puis téléchargées par l'appli |
| Paie | À la journée |

## Propositions par défaut (valables tant que Babacar ne dit pas autre chose)

| Sujet | Proposition |
|---|---|
| Retard | Au-delà de 15 minutes après l'heure de début (réglable par campagne) |
| Distance de pointage | Pointage accepté à moins de 200 m du lieu (réglable par lieu). Plus loin, le pointage est gardé mais marqué « à vérifier » pour le superviseur |
| Code faux | 5 essais, puis blocage 15 minutes |
| Conservation | Selfies et positions GPS : 3 mois après la fin de la campagne. Messages vocaux : 6 mois. Photos de campagne et chiffres : 2 ans |
| Client | Reçoit le PDF et le fichier Excel, pas d'accès en ligne |
| Stock | Suivi simple reçu / restant par agent et par jour, sans le module Inventaire d'Odoo |
| Formation (vidéos, quiz) | Après la V1 |

## Questions ouvertes

1. Serveur : la base Odoo 20 de Boomerang est-elle sur le même serveur Hetzner que TAAGG (nom de site à part) ou sur un autre ? Est-elle déjà installée ?
2. Tarif journalier : le même pour toutes les hôtesses d'une campagne ? Superviseur à un autre tarif ? Prime de transport ?
3. Le module Odoo va-t-il dans ce dépôt (`odoo/boomerang_terrain/`) ou dans un dépôt Odoo de Boomerang à part ?
