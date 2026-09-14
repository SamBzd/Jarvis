# Sessions récentes

FIFO global limité aux dix dernières clôtures. Les entrées sont classées de la plus récente à la plus ancienne et contiennent chacune 80 à 120 mots.

<!-- sessions:start -->
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
