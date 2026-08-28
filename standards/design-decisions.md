# Décisions de conception

Ce document consigne les choix durables du cerveau global. Il ne sert pas de journal de projet.

## Contrat global et projets

- `AGENTS.md` global porte l'identité et les invariants comportementaux de Jarvis.
- Les projets portent leurs règles produit et techniques dans leur propre `AGENTS.md`.
- La priorité globale souhaitée est un contrat de comportement, pas une garantie technique : Codex concatène ensuite les instructions projet.
- Aucun lanceur strict n'est imposé en v1. Il ne sera envisagé qu'après un conflit réel démontrant son utilité.

## Modèles

- Sam choisit manuellement le modèle de la session principale.
- La configuration globale ne fixe donc pas le modèle principal.
- Tout agent délégué utilise par défaut `gpt-5.6-terra` avec un effort `medium`.
- Un autre modèle ou effort nécessite une validation explicite de Sam avant la délégation.

## Mémoire

- Le dépôt Git privé est le support partagé entre appareils.
- La mémoire globale reste en Markdown, petite et inspectable.
- Elle contient uniquement des métadonnées opérationnelles partageables, jamais le contenu technique des projets.
- Le FIFO conserve dix clôtures de 80 à 120 mots.
- À la clôture explicite, seuls le FIFO et la date de dernière session peuvent être modifiés, committés et poussés automatiquement.
- Une coupure brutale ne crée aucun fichier de récupération ; Sam utilise `/resume`.

## Synchronisation

- Une salutation adressée à Jarvis tente une synchronisation entrante avec `git pull --ff-only`.
- Un dépôt sale, une divergence ou un échec réseau bloque la synchronisation sans résolution automatique.
- Aucun dépôt projet n'est tiré automatiquement.
- Une mise à jour du contrat global récupérée après le lancement ne prend effet qu'à la session suivante.

## Installation

- Le dépôt standard est `~/jarvis`.
- Le contrat global est relié au répertoire Codex par un lien symbolique.
- L'installation respecte `CODEX_HOME` et refuse de masquer ou d'écraser un contrat existant.
- La configuration des sous-agents est fournie comme fragment manuel afin de préserver la configuration personnelle existante.

## Portabilité

- La v1 cible Linux avec Bash, Git et Python 3.10 ou supérieur sans dépendance externe.
- La compatibilité Windows native reste à confirmer ; aucun comportement multi-plateforme n'est promis avant test réel.

## Skills et plugins

- Les règles permanentes restent dans le contrat, pas dans une skill.
- Une skill est créée seulement après stabilisation d'un workflow répété.
- Aucun plugin n'est installé par anticipation.
- Toute capacité externe fait l'objet d'une revue de provenance, permissions, dépendances et données partagées.
