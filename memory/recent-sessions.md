# Sessions récentes

FIFO global limité aux dix dernières clôtures. Les entrées sont classées de la plus récente à la plus ancienne et contiennent chacune 80 à 120 mots.

<!-- sessions:start -->
## 2026-10-03 — stamp-app — Kanban des fournitures

- Contexte : Implémentation et livraison de l’issue #31 sur une branche dédiée.
- Réalisé : Le Kanban Fournitures à cinq colonnes, le bilan mensuel, les notifications et le sélecteur de mois ont été livrés. Les ajustements CodeRabbit de concurrence et d’accessibilité ont été intégrés.
- Décisions : Les cartes n’affichent pas de bouton de déplacement ; elles restent activables au clic, au tactile et au clavier. Seul Terminer reste dans Traité.
- État : La PR #38 est fusionnée ; main et origin/main pointent sur le merge. .agents/ reste non suivi et préexistant.
- Prochaine action : Tester le Kanban sur la cible de déploiement avant la prochaine livraison.

## 2026-09-30 — stamp-app — Workflow fournitures fusionné

- Contexte : Issue #30 finalisée, validée et fusionnée dans main après une PR dédiée.
- Réalisé : Migration 0004 sans backfill, unités persistantes, alertes anonymes, synchronisation transactionnelle et API de workflow livrées. PR #37 fusionnée.
- Décisions : Le Kanban frontend #31, le déploiement NAS et toute migration de données réelles restent hors périmètre.
- État : main est synchronisée avec origin/main au commit b92e262. Seul .agents/ non suivi préexistant demeure dans l’arbre.
- Prochaine action : Préparer la revue fonctionnelle, puis l’issue #31, avant tout déploiement prudent et documenté de main.

## 2026-09-29 — stamp-app — Issue 29 fusionnée sur main

- Contexte : Session Stamp App consacrée à la composition guidée des commandes et au traitement du retour de revue Codex.
- Réalisé : Répartition A/B automatique, contrôles moins/plus, résumé responsive, documentation et tests livrés. La PR 36 a été créée, auditée, corrigée puis fusionnée.
- Décisions : C conserve sa règle d'au moins une feuille par papier. Un dépassement temporaire lors d'une édition indique désormais les feuilles en trop.
- État : main est synchronisée avec origin/main au commit 7e56528. Aucun changement suivi restant ; .agents est non suivi et préexistant.
- Prochaine action : Attendre la prochaine issue ou effectuer une recette métier supplémentaire si nécessaire.

## 2026-09-29 — stamp-app — Issue #28 — bibliothèque de papiers

- Contexte : Implémentation complète de la bibliothèque de papiers et correction du sélecteur de collection, sur la branche dédiée.
- Réalisé : Page Papiers, création, recherche, renommage, archivage et restauration. Doublons normalisés, règles de conservation des papiers archivés et correction documentaire demandée par CodeRabbit.
- Décisions : Le renommage de papier reste exclusivement dans la bibliothèque. La migration v3 refuse les doublons après normalisation Unicode NFC et casse française.
- État : Commits 841b249 et 99d922f poussés sur codex/issue-28-bibliotheque-papiers ; PR #35 ouverte et décrite. La démo locale a été arrêtée. .agents/ reste non suivi et non modifié.
- Prochaine action : Attendre la CI et la revue finale de la PR #35 avant fusion.

## 2026-09-27 — stamp-app — Issue 27 — parcours Clientes fluidifié

- Contexte : Travail sur la branche codex/issue-27-fluidifier-clientes pour traiter l’issue 27 et les reviews CodeRabbit et Codex.
- Réalisé : Ajout des suggestions email, du formatage téléphone avec curseur stable, d’un formulaire compact, d’une recherche locale plus fiable et de mutations sans rechargement global. Tests de régression ajoutés.
- Décisions : Conserver le sens métier Favori et le libellé visible unique « Favori » ; ne modifier ni l’API, ni le schéma, ni le déploiement.
- État : Trois commits poussés. PR #34 fusionnée dans main via a28e9b3. Validations npm run check et docker compose config réussies. Branche locale propre hors .agents non suivi.
- Prochaine action : Repartir d’une main actualisée pour la prochaine issue sans supprimer automatiquement la branche de travail.

## 2026-09-22 — stamp-app — Issue 26 UI et navigation

- Contexte : Stamp App : main a été mise à jour après la fusion de la PR #33, avec une base de développement locale réinitialisée pour la démonstration.
- Réalisé : Le socle visuel et la navigation macOS sont livrés. Les corrections CodeRabbit ont été intégrées et poussées.
- Décisions : La refonte UI plus large est reportée après l’implémentation des parcours métier restants.
- État : main est synchronisée avec origin/main. Le dossier .agents demeure non suivi et préservé.
- Prochaine action : Poursuivre les fonctionnalités métier, puis planifier la passe UI globale.

## 2026-09-21 — stamp-app — Issue 12 fusionnée et epic UX structurée

- Contexte : La recette métier confirme le socle fonctionnel mais révèle une refonte UX nécessaire avant déploiement.
- Réalisé : Audit UX/UI consigné dans l’issue 25, avec découpage dans les issues 26 à 31. Recette reproductible, couverture renforcée et correction de l’historique cliente livrées par la PR 32. Revue traitée avec un test des libellés kits A, B, C et hors-kit.
- Décisions : Direction visuelle atelier macOS chaleureux avec navigation générique avant la future mascotte. Epic déploiement mise en attente pendant la refonte UX/UI.
- État : main est synchronisée sur 05caa23. Seul le dossier local non suivi .agents reste à préserver.
- Prochaine action : Démarrer l’issue 26, socle visuel et navigation, sur une nouvelle branche dédiée.

## 2026-09-18 — stamp-app — Clôture après livraison du bilan des commandes

- Contexte : Session consacrée à l’issue onze de Stamp App, dans le périmètre convenu avec Sam.
- Réalisé : Implémentation, documentation et tests terminés. Les contrôles backend, frontend, build et configuration Docker ont réussi. Un audit indépendant en lecture seule n’a trouvé aucun défaut actionnable.
- Décisions : Sam indique que la PR est fusionnée et que main est actualisée localement. Aucune opération supplémentaire sur le projet pendant la clôture.
- État : Ce workspace reste sur la branche de l’issue, avec le travail committé. Main locale reste antérieure. Aucun changement suivi restant ; dossier préexistant non suivi préservé.
- Prochaine action : À la reprise, vérifier la branche main et sa synchronisation avant de choisir la prochaine issue. Aucune validation du déploiement réel effectuée.

## 2026-09-18 — stamp-app — Issue #11 — bilan des commandes

- Contexte : Branche codex/issue-11-bilan-commandes créée par l’automatisation planifiée pour travailler hors de main.
- Réalisé : Implémentation locale du bilan historique, adaptation de l’interface, tests ciblés et documentation ajoutées ; aucun changement n’est commité.
- Décisions : Le bilan expose les montants en centimes, utilise le prix appliqué historique des kits et conserve le montant hors-kit enregistré.
- État : Modifications dans backend, frontend, tests et documentation ; npm run check échoue encore sur app.test.js, catalogue-api.test.js et commandes-kit-api.test.js. Le dossier .agents reste non suivi et préexistant.
- Prochaine action : Diagnostiquer les trois échecs backend, relancer npm run check et docker compose config, puis revoir le diff avant tout commit.

## 2026-09-17 — stamp-app — Issue 10 stocks fusionnée

- Contexte : Stamp App sur main après fusion de la PR #22.
- Réalisé : Les stocks utilisent les snapshots de commandes, avec provenance historique, rubans, quantités base/finales, affichage responsive et tests de concurrence réseau.
- Décisions : Les homonymes historiques affichent désormais les références catalogue et collection. CodeRabbit n’a produit aucun commentaire actionnable.
- État : main est alignée sur origin/main au commit 6a4668a. Seul .agents/ non suivi, préexistant, reste local. npm run check, docker compose config et recette navigateur ont réussi.
- Prochaine action : Recette fonctionnelle globale puis planification de la livraison v2 ; aucune modification du NAS n’a été réalisée.
<!-- sessions:end -->
