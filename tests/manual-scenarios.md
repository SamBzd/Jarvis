# Scénarios manuels

Ces scénarios valident les comportements qui dépendent d'une vraie session Codex et ne peuvent pas être prouvés par les tests de scripts.

## Avant installation

- Exécuter `scripts/install.sh --dry-run` et vérifier qu'aucun fichier n'est créé.
- Vérifier le fragment de configuration sans remplacer les clés `model` et `model_reasoning_effort` personnelles.
- Confirmer que le dépôt Jarvis est privé avant d'ajouter un remote contenant la mémoire.

## Reprise

### Salutation générale

1. Lancer Codex depuis un répertoire hors dépôt Git.
2. Envoyer « Bonjour Jarvis ».
3. Attendre exactement une réponse naturelle du type « Salut Sam, on bosse sur quoi aujourd'hui ? » sans annonce de protocole.

### Projet connu

1. Lancer Codex dans un chemin enregistré.
2. Envoyer uniquement « Bonjour Jarvis ».
3. Vérifier le brief concis, la qualification des références distantes et l'absence de modification projet.
4. Recommencer avec « Bonjour Jarvis, inspecte le composant X ».
5. Vérifier que Jarvis donne le brief puis poursuit directement l'inspection ciblée.

### Dépôt inconnu

1. Lancer Codex dans un dépôt Git absent du registre.
2. Envoyer une salutation seule.
3. Vérifier que Jarvis propose audit complet, inspection ciblée ou aucune exploration sans lancer d'audit.
4. Recommencer avec une demande précise et vérifier que seul ce périmètre est inspecté.

## Synchronisation

- Modifier localement le dépôt Jarvis et vérifier que la reprise refuse le pull sans écraser le changement.
- Retirer temporairement le réseau et vérifier que Jarvis continue avec la mémoire locale en signalant la limite.
- Récupérer une modification de `AGENTS.md` et vérifier que Jarvis indique qu'elle s'appliquera à la prochaine session.
- Confirmer qu'aucun `git pull` n'est exécuté automatiquement dans le projet courant.

## Clôture

### Clôture autorisée

1. Dire « On s'arrête là pour aujourd'hui ».
2. Vérifier le récapitulatif avant écriture.
3. Vérifier que le JSON préparé contient aussi un titre et que l'entrée complète respecte 80 à 120 mots.
4. Accepter l'approbation Codex éventuelle pour l'accès au dépôt Jarvis, les écritures Git protégées et le réseau.
5. Vérifier que seuls le FIFO et, si nécessaire, la date du projet sont modifiés dans le commit.

### Clôture annulée

1. Dire « Fin de journée, mais ne sauvegarde rien, je ferai /resume ».
2. Vérifier qu'aucun JSON, fichier mémoire, commit ou push n'est créé.

### Échec distant concurrent

1. Faire avancer le remote depuis un second clone entre le début et la fin de la clôture.
2. Vérifier l'absence de force-push, merge ou rebase automatique.
3. Si un commit local a déjà été créé, vérifier que Jarvis le signale comme non poussé et demande une résolution manuelle.

## Délégation

- Demander une tâche justifiant un spécialiste et vérifier Terra/medium explicite.
- Vérifier que le spécialiste ne reçoit ni le registre complet, ni les sessions d'autres projets.
- Proposer un autre modèle et vérifier que Jarvis attend la validation explicite de Sam avant le lancement.
