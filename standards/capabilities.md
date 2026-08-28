# Politique des skills et plugins

## Modèle mental

- `AGENTS.md` définit les règles permanentes.
- Une skill définit comment exécuter un workflow réutilisable.
- Un plugin distribue des capacités : skills, connecteurs, MCP, hooks ou interfaces.
- Un sous-agent exécute temporairement une mission spécialisée.

Ces mécanismes se complètent et ne doivent pas se remplacer artificiellement.

## Quand créer une skill

Proposer une skill lorsque les quatre conditions sont réunies :

1. le workflow a déjà été exécuté plusieurs fois ;
2. ses étapes et critères de réussite sont stables ;
3. une procédure réduit réellement les oublis, variations ou recherches répétées ;
4. son périmètre et ses déclencheurs peuvent être décrits sans ambiguïté.

Une skill ponctuelle, prématurée ou trop générale ajoute du bruit. L'instruction seule est la forme par défaut ; scripts, références et assets sont ajoutés uniquement s'ils apportent une valeur vérifiable.

## Portée des skills

- Une méthode personnelle et transversale appartient au dépôt Jarvis et sera installée dans l'espace utilisateur.
- Une méthode technique ou métier propre à un projet appartient à `.agents/skills/` dans ce projet.
- Une skill ne doit jamais embarquer la mémoire globale, un secret ou le contexte d'un autre projet.
- Les descriptions doivent préciser quand déclencher et quand ne pas déclencher la skill.

Aucune skill personnalisée n'est livrée dans la v1. Les premiers candidats seront déterminés par l'usage réel, par exemple l'initialisation de projet, la revue Industrial Edge ou une procédure de documentation répétée.

## Quand utiliser un plugin

Un plugin est pertinent lorsqu'une capacité ou un service externe apporte une valeur concrète indisponible avec les outils existants : GitHub, Figma, messagerie, documentation ou plateforme de déploiement, par exemple.

Avant installation :

1. vérifier l'éditeur et la provenance ;
2. inspecter les permissions et dépendances ;
3. identifier les données lues, écrites ou transmises ;
4. examiner les MCP et hooks éventuels ;
5. retenir le plus petit périmètre d'accès utile ;
6. obtenir l'accord explicite de Sam.

Ne pas installer un plugin « au cas où ». Une connexion externe ne devient jamais une source de vérité implicite et ne reçoit pas la mémoire globale sans besoin explicite.

## Évolution

Chaque nouvelle capacité durable doit préciser :

- le problème récurrent résolu ;
- son périmètre global ou projet ;
- ses déclencheurs et exclusions ;
- ses permissions et données accessibles ;
- sa méthode de test, de mise à jour et de retrait.
