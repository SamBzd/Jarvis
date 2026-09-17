# Sessions récentes

FIFO global limité aux dix dernières clôtures. Les entrées sont classées de la plus récente à la plus ancienne et contiennent chacune 80 à 120 mots.

<!-- sessions:start -->
## 2026-09-17 — stamp-app — Issue 6 API catalogues finalisée

- Contexte : Implémentation de l’API sources, tarifs et archivage sur Stamp App.
- Réalisé : Tarifs en centimes, publication/démotion, archivage clientes/catalogues, tests métier et documentation livrés. Quatre commits poussés sur codex/issue-6-api-catalogues.
- Décisions : Main reste stable : l’issue 7 a été créée depuis l’issue 6 ; le merge attend l’adaptation de l’interface aux centimes.
- État : Branche active codex/issue-7-commandes-kits, arbre propre. npm run check, docker compose config et deux audits API indépendants réussis.
- Prochaine action : Implémenter l’issue 7 : création et validation des commandes kit.

## 2026-09-16 — stamp-app — Issue 5 : schéma cible et import clientes

- Contexte : Implémentation de l’issue 5 sur une branche dédiée, sans intervention sur la base de production.
- Réalisé : Migration cible, schéma catalogue/kit, snapshots, outil d’import atomique des clientes et documentation livrés.
- Décisions : Les suppressions physiques sont bloquées ; la création et le règlement complets des kits restent dans l’issue 7.
- État : Dépôt propre sur main, synchronisé au commit de fusion 09339d4. La PR #17 est fusionnée ; la branche dédiée peut être supprimée ultérieurement.
- Prochaine action : Supprimer la branche codex/issue-5-schema-import-clients si elle n’est plus utile, puis choisir le prochain lot.

## 2026-09-16 — stamp-app — Issue 5 : schéma cible et import clientes

- Contexte : Implémentation de l’issue 5 sur une branche dédiée, sans intervention sur la base de production.
- Réalisé : Migration cible, schéma catalogue/kit, snapshots, outil d’import atomique des clientes et documentation livrés.
- Décisions : Les suppressions physiques sont bloquées ; la création et le règlement complets des kits restent dans l’issue 7.
- État : Dépôt propre sur main. Le commit bc714f7 est poussé sur codex/issue-5-schema-import-clients ; la PR #17 vers main est ouverte.
- Prochaine action : Relire puis fusionner la PR #17 ; supprimer sa branche après fusion si elle n’est plus utile.

## 2026-09-16 — stamp-app — Alignement du backlog après validation métier

- Contexte : Reprise du projet après fusion du cadrage, puis vérification de la cohérence des lots restants.
- Réalisé : Les onze définitions d’issues ont été relues, corrigées et vérifiées sur GitHub. Un audit indépendant en lecture seule n’a trouvé aucun défaut bloquant.
- Décisions : Le contrat validé reste la référence des futurs lots. L’intégration des deux lots d’interface reste souple ; aucune nouvelle décision produit.
- État : Main propre et alignée sur sa référence distante. Aucun changement de code ni nouveau commit. Aucun accès ou changement de production. Les validations portaient sur le backlog, pas sur une implémentation.
- Prochaine action : Commencer le prochain lot de schéma et d’outillage après instruction de Sam ; conserver les autorisations opérationnelles séparées.

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
