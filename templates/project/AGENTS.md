# <Nom du projet> — Instructions des agents

Ce fichier définit uniquement le contrat technique et documentaire du projet. Il complète les règles globales de l'orchestrateur sans redéfinir son identité, sa mémoire, ses modèles ou ses autorisations sensibles.

## 1. Produit et architecture

- <Finalité du produit.>
- <Utilisateurs principaux.>
- <Composants et technologies structurantes.>
- <Contraintes de déploiement ou d'exploitation.>

## 2. Documentation et sources de vérité

- `docs/README.md` : index et ordre de lecture.
- <Documents durables propres au projet.>

Ordre de priorité par défaut :

1. code, configuration, tests et état Git réels ;
2. décisions explicitement validées ;
3. architecture et documentation métier ;
4. journal ou historique.

Signaler toute contradiction au lieu de choisir silencieusement une version.

## 3. Protocole avant intervention

1. lire les instructions et documents pertinents ;
2. vérifier la branche et l'état Git ;
3. préserver les changements préexistants ;
4. inspecter les fichiers impliqués et leurs consommateurs ;
5. confirmer les ambiguïtés qui changeraient matériellement le résultat.

## 4. Conventions techniques

- <Conventions de langage et framework.>
- <Séparation des responsabilités.>
- <Règles métier indispensables.>
- <Contraintes de sécurité et de compatibilité.>

## 5. Validation et définition de terminé

1. couvrir le comportement demandé et les cas limites convenus ;
2. exécuter les tests, builds ou validations pertinents ;
3. inspecter le diff final et les changements hors périmètre ;
4. mettre à jour la documentation durable affectée ;
5. communiquer validations, limites, risques et état Git final.
