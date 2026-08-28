# Mémoire de Jarvis

Cette mémoire est volontairement petite, vérifiable et versionnée. Elle assure la continuité entre les sessions et les appareils sans recopier le contenu des projets.

## Fichiers

- `profile.md` contient uniquement les préférences confirmées de Sam.
- `projects.md` référence les projets connus avec leurs métadonnées opérationnelles minimales.
- `recent-sessions.md` conserve au maximum les dix dernières clôtures, dans l'ordre antéchronologique.

## Données autorisées

- informations que Sam pourrait lui-même partager ;
- identifiants stables et noms de projets ;
- nature personnelle ou professionnelle ;
- fonctionnement solo ou collaboratif ;
- chemins locaux par appareil et chemin des instructions projet ;
- remote Git sans credential ;
- date de dernière session ;
- titre et résumé court du contexte, du réalisé, des décisions, de l'état et de la prochaine action.

## Données interdites

- secrets, tokens, mots de passe, clés ou URL authentifiées ;
- données client ou informations internes non partageables ;
- code, configuration métier, architecture interne ou détails d'implémentation ;
- vulnérabilités non publiques ;
- copie complète d'une conversation.

## Autorisations d'écriture

La clôture explicite peut mettre à jour automatiquement :

1. `recent-sessions.md` ;
2. le champ `Dernière session` du projet concerné dans `projects.md`.

Toute autre modification requiert une validation explicite de Sam. La lecture doit être ciblée : une entrée projet et au maximum deux résumés pertinents suffisent normalement.

Le script de clôture applique quelques contrôles heuristiques contre des secrets usuels et les URL authentifiées. Ces contrôles ne garantissent pas l'absence de toute donnée sensible : Jarvis doit respecter la politique de mémoire avant de préparer le résumé.
