# Sessions récentes

FIFO global limité aux dix dernières clôtures. Les entrées sont classées de la plus récente à la plus ancienne et contiennent chacune 80 à 120 mots.

<!-- sessions:start -->
## 2026-09-17 — stamp-app — Issue 8 — catalogue et archivage

- Contexte : Session Stamp App consacrée à l’issue 8, rebasée après l’intégration des issues 6 et 7.
- Réalisé : Interface catalogue et archivage clientes livrés ; PR #20 rebasée, conflits documentaires résolus et retours de revue corrigés ; validations locales réussies : 72 tests backend, 5 tests frontend, build Vue et Compose.
- Décisions : Les retours pertinents ont été corrigés : avertissement de sortie, verrou de défilement partagé, création concurrente et message d’archivage.
- État : Branche codex/issue-8-interface-catalogues synchronisée avec origin ; .agents/ est non suivie et préexistante.
- Prochaine action : Revoir puis merger la PR #20 ; démarrer ensuite l’issue 9 depuis main à jour.

## 2026-09-17 — stamp-app — Issue 7 — commandes kits

- Contexte : Travail sur la branche codex/issue-7-commandes-kits, basée sur l’issue 6.
- Réalisé : Le backend commandes kits A/B/C est livré : composition, snapshots, tarifs, rubans, option, suppléments, règlement, suppression, stocks et bilan.
- Décisions : L’issue 8 partira de l’issue 6 ; l’issue 9 attendra l’intégration de 7 et 8.
- État : Trois commits sont poussés : 7f9d6f5, aff54d3 et 628ba89. Arbre propre ; npm run check et docker compose config passent. Audit indépendant sans défaut concret.
- Prochaine action : Créer l’issue 8 depuis 15d43b5 ; préparer l’issue 9 quand les issues 7 et 8 seront intégrées.

## 2026-09-17 — stamp-app — Issue 7 — commandes kits

- Contexte : Travail sur la branche codex/issue-7-commandes-kits, basée sur l’issue 6.
- Réalisé : Le backend des commandes kits A/B/C est implémenté : composition, snapshots, tarifs, rubans, option, suppléments, règlement et suppression.
- Décisions : L’issue 8 partira de l’issue 6 ; l’issue 9 attendra l’intégration de 7 et 8.
- État : Les changements sont non committés. Les contrôles npm run check et docker compose config passent ; l’audit indépendant n’a trouvé aucun défaut concret.
- Prochaine action : Relire puis committer l’issue 7, créer l’issue 8 depuis le commit 15d43b5, et préparer l’issue 9 après intégration.

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
<!-- sessions:end -->
