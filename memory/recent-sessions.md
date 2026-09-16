# Sessions récentes

FIFO global limité aux dix dernières clôtures. Les entrées sont classées de la plus récente à la plus ancienne et contiennent chacune 80 à 120 mots.

<!-- sessions:start -->
## 2026-09-16 — stamp-app — Fondations DevOps et cadrage métier

- Contexte : Stabilisation de main avant les changements métier catalogues et commandes kits.
- Réalisé : Les règles métier ont été documentées et fusionnées dans main. Les issues #4 à #14 et le tableau GitHub ont été créés. Un modèle de PR et une checklist NAS ont été ajoutés via la PR #15.
- Décisions : Main est protégé par PR et CI. Le flux du tableau est À préparer, Prêt, En cours, En revue, Terminé.
- État : Branche codex/devops-foundations propre, commit 0f21985 poussé. PR #15 ouverte vers main, CI réussie.
- Prochaine action : Relire puis fusionner la PR #15 ; démarrer ensuite l’issue #4 de conception métier.

## 2026-09-16 — stamp-app — Migration SQLite fusionnée et démarrage local

- Contexte : Finalisation de la migration SQLite versionnée et préparation de la reprise sur main.
- Réalisé : La PR #1 est fusionnée dans main. La branche chore/database-migrations est conservée. L'application a été lancée localement avec db/dev.db puis arrêtée.
- Décisions : Les remarques sur les collations et la reconstruction de tables avec clés étrangères sont reconnues mais reportées avant leur premier besoin concret.
- État : main est synchronisée avec origin/main et l'arbre de travail est propre. Aucun serveur de développement ne tourne.
- Prochaine action : Créer une branche depuis main pour la prochaine amélioration fonctionnelle, après avoir défini son besoin et sa priorité.

## 2026-09-15 — stamp-app — Migrations SQLite et PR de revue

- Contexte : Stabilisation de Stamp App sur la branche de migrations SQLite.
- Réalisé : Framework de migrations, tests CLI, documentation, trois commits et PR #1 créés puis poussés.
- Décisions : La conversion de la base historique du NAS reste hors périmètre. Les nouvelles features partent de main ; les changements de schéma attendent la fusion des migrations.
- État : Branche chore/database-migrations propre et synchronisée avec origin. La PR #1 est ouverte, sans merge. La revue Codex GitHub est bloquée par une connexion Codex Cloud à finaliser.
- Prochaine action : Connecter Codex Cloud à GitHub, relancer la revue de la PR, puis choisir la prochaine feature et créer sa branche depuis main.

## 2026-09-14 — stamp-app — Stabilisation et socle déployable

- Contexte : Remise à plat demandée avant toute reprise des fonctionnalités et corrections.
- Réalisé : Historique Git rationalisé et références utiles conservées. Base de développement portable et déploiement générique validés puis synchronisés.
- Décisions : main devient la base active ; la production historique reste archivée. Les données réelles et la cible d’exploitation restent hors périmètre.
- État : main est propre et synchronisée avec origin/main au commit 34df395. Les services de validation sont arrêtés et le volume de test vierge est conservé.
- Prochaine action : Ajouter des migrations versionnées et des procédures de sauvegarde et restauration, puis une CI et une validation depuis un clone vierge.

## 2026-09-14 — stamp-app — Documentation de fondation clarifiée

- Contexte : Reprise d’un projet ancien avant une amélioration à définir, avec priorité à une documentation fiable sans changement fonctionnel.
- Réalisé : Les essais techniques non validés ont été annulés. La documentation distingue la production, la refonte abandonnée et les informations à confirmer. L’ancien plan a été archivé.
- Décisions : La branche de production reflète l’installation en service. L’application est locale, utilisée depuis un Mac et hébergée sur un NAS. La base locale est obsolète et doit être préservée.
- État : La branche documentaire contient des modifications non committées. La base locale reste le seul changement non documentaire et n’a pas été touchée.
- Prochaine action : Relire puis committer uniquement la documentation, avant de préparer la réunion et l’inspection contrôlée de la production.
<!-- sessions:end -->
