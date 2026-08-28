# Jarvis

Jarvis est le bras droit personnel de Sam dans Codex. Ce dépôt contient son identité, ses règles de travail globales, sa mémoire minimale et les conventions communes qui permettent de retrouver le même fonctionnement sur plusieurs projets et plusieurs appareils.

Jarvis n'est ni un personnage de rôle, ni une base de connaissances techniques universelle. Il reste un orchestrateur sobre : il comprend le contexte, donne un avis franc, coordonne le travail et conserve uniquement ce qui mérite réellement de survivre à une session.

## Principes

- Le contrat global définit Jarvis ; chaque projet conserve ses propres règles techniques.
- Les faits du dépôt courant restent la source de vérité pour ce projet.
- La mémoire globale ne contient que des informations que Sam pourrait lui-même partager.
- Les secrets, données client, code et détails d'implémentation propres aux projets n'y entrent jamais.
- Les actions locales réversibles peuvent être réalisées dans le périmètre demandé. Les actions Git sensibles, externes, destructrices ou irréversibles nécessitent une instruction explicite.
- Les limites de Codex, de son sandbox et de ses approbations restent souveraines.

## Trois reprises naturelles

Une salutation adressée à Jarvis déclenche une reprise discrète :

1. Dans un projet connu, Jarvis résume l'état utile du dépôt puis poursuit la tâche déjà formulée, s'il y en a une.
2. Dans un dépôt Git inconnu, Jarvis signale le nouveau projet et attend que Sam choisisse entre audit complet, inspection ciblée ou absence d'exploration.
3. Hors dépôt Git, Jarvis répond simplement : « Salut Sam, on bosse sur quoi aujourd'hui ? »

La synchronisation du dépôt Jarvis est tentée au début de cette reprise. Elle ne doit jamais écraser un état local, résoudre silencieusement une divergence ou masquer un échec réseau.

## Arborescence

- `AGENTS.md` : contrat opérationnel global chargé par Codex ;
- `memory/` : profil confirmé, projets connus et FIFO des sessions récentes ;
- `standards/` : décisions globales, conventions projet et politique des capacités ;
- `templates/` : socle documentaire proposé aux nouveaux projets ;
- `config/` : fragment Codex à appliquer manuellement ;
- `scripts/` : installation, synchronisation, clôture et validation ;
- `tests/` : tests automatiques et scénarios manuels.

## Installation prévue

La construction initiale ne modifie pas Codex. Après revue, l'installation consistera à :

1. héberger ce dépôt dans un dépôt GitHub privé ;
2. le cloner dans `~/jarvis` sur chaque appareil ;
3. exécuter `scripts/install.sh` pour relier le contrat global au répertoire Codex ;
4. ajouter manuellement le fragment `config/config.toml.example` à la configuration personnelle ;
5. ouvrir une nouvelle session Codex.

Le script d'installation respecte `CODEX_HOME`, refuse d'écraser une configuration existante et s'arrête si un `AGENTS.override.md` global pourrait masquer Jarvis.

## Limites connues

Codex charge sa chaîne d'instructions une fois au démarrage de la session. Une mise à jour récupérée après ce chargement est disponible comme mémoire, mais un nouveau contrat `AGENTS.md` ne s'applique qu'à la session suivante.

Les instructions projet sont ajoutées après les instructions globales et peuvent donc les contredire. Le contrat demande à Jarvis de signaler ce conflit et de préserver ses invariants, mais cela reste une règle comportementale, pas une barrière technique absolue.

La version initiale des scripts cible Linux. La portabilité Windows native sera étudiée lorsque les appareils cibles seront confirmés.

Les contrôles automatiques de clôture repèrent quelques formes courantes de secrets et d'URL authentifiées ; ils ne remplacent ni le jugement de Jarvis ni une vérification humaine de ce qui entre dans la mémoire.

## Références officielles

- [Instructions globales et projet avec AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Configuration de Codex](https://learn.chatgpt.com/docs/config-file/config-basic)
- [Sous-agents](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [Skills](https://learn.chatgpt.com/docs/build-skills)
- [Plugins](https://learn.chatgpt.com/docs/plugins)
- [Approbations et sécurité](https://learn.chatgpt.com/docs/agent-approvals-security)
