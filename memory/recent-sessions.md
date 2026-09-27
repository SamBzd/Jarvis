# Sessions récentes

FIFO global limité aux dix dernières clôtures. Les entrées sont classées de la plus récente à la plus ancienne et contiennent chacune 80 à 120 mots.

<!-- sessions:start -->
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

## 2026-09-17 — stamp-app — Issue 9 commandes livrée et fusionnée

- Contexte : Stamp App, branche main après fusion de la PR #21.
- Réalisé : L’interface commandes kits et hors-kit de l’issue 9 est intégrée. Les retours Codex et CodeRabbit ont été corrigés : erreurs de détail isolées, fermeture pendant chargement et navigation radio clavier.
- Décisions : Aucune migration ni déploiement. Le NAS reste hors périmètre.
- État : main est synchronisée avec origin/main au commit 7a5eb43. Seul .agents/ non suivi, préexistant, reste local.
- Prochaine action : Recette fonctionnelle sur l’environnement de déploiement avant planification de la livraison v2.

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
<!-- sessions:end -->
