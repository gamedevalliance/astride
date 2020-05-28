# Bot Discord pour Game Dev Alliance

Le bot Game Dev Alliance permet d'afficher des textes et des liens fréquemment utilisés sur notre [serveur Discord](https://discord.gg/RrBppaj). Toutes les commandes sont utilisables sur le serveur ou en message privé avec le bot.

Ecrivez `!help <commande>` pour recevoir un MP avec des informations sur n'importe quelle commande ou catégorie.

## Commandes publiques

### Wiki

```
!wiki
```

Cette commande, que l'on peut aussi écrire `!w`, affiche un lien vers le wiki (https://wiki.gamedevalliance.fr/). Il est possible d'afficher un lien vers un article précis du wiki :

```
!wiki faq          => https://wiki.gamedevalliance.fr/faq
!wiki rpgmaker     => https://wiki.gamedevalliance.fr/rpgmaker
```

### Afficher un texte

```
!texte <nom>
```

Affiche un texte préparé par les modérateurs. N'oubliez pas qu'il existe d'autres écritures plus rapides de `!texte`. Ainsi, ces trois lignes affichent le même résultat :

```
!texte code
!tag code
!t code
```

Si le nom que vous écrivez n'existe pas, le bot vous recommandera un nom similaire parmi ceux enregistrés.

```
!t list
```

Affiche la liste de tous les textes actuellement enregistrés.

![](https://i.imgur.com/9RBSt11.png)

### Challenge de la semaine

Au cours d'un challenge de la semaine, le bot peut automatiquement récupérer les participations contenant le \[NomDuChallenge], en indiquant sa réussite d'un emoji 👍, et ce jusqu'au dimanche soir à minuit. Ensuite, il présente toutes les participations et enregistre les votes du public le lundi soir à minuit. Le bot affiche alors un podium et le challenge est terminé.

Les participations sont enregistrées par le bot pour conserver un historique des challenges.

```
!challenge
!c
```

Donne le nom du challenge actuel.

### Vidéos

```
!video <nom>
```

Affiche une vidéo de la [chaîne Game Dev Alliance](https://www.youtube.com/c/AurelienVideos). On peut aussi écrire plus simplement `!v`. Voici toutes les commandes disponibles :

```
!v bases            => "Les bases de RPG Maker en 30 minutes"
!v donjon1          => "Créer un donjon sur RPG Maker : monstres et énigmes"
!v donjon2          => "Créer un donjon sur RPG Maker : le boss final"
!v villes           => "Créer une ville de RPG"
!v export           => "Exporter son jeu RPG Maker : le guide ultime"
!v meilleur         => "Quel est le meilleur RPG Maker ?"
!v mapping          => "Créer un jeu plus beau - Tutoriel Mapping RPG Maker"
!v live             => Live en cours
!v rediffusions     => Playlist des rediffusions
```

En cas d'erreur de frappe, le bot recommandera un nom de vidéo similaire parmi ceux qui existent.

## Commandes d'administration

Les commandes suivantes sont réservées aux modérateurs.

### Gestion des textes

Il est possible de stocker ses propres textes, et de les nommer afin de les afficher rapidement plus tard. Toutes les commandes commencent par `!texte`, que l'on peut aussi écrire `!t` ou `!tag`.

#### Ajouter un texte

```
!t add <nom> <contenu>
```

Le nom doit être en un seul mot (ou bien entre guillemets), tandis que le contenu est libre. Exemple :

```
!t add site Notre site est https://gamedevalliance.fr
!t add "site Unity" Le site officiel de Unity est https://unity3d.com
```

Dans le premier cas, le nom `site` ne contient pas d'espace, donc les guillemets ne sont pas nécessaires.

#### Modifier un texte

```
!t edit <nom> <contenu>
```

Remplace le contenu d'un texte existant.

#### Supprimer un texte

```
!t remove <nom>
```

### Challenge de la semaine

#### Lancer un challenge

```
!challenge set NomDuChallenge
!c s NomDuChallenge
```

Lance un nouveau challenge de la semaine. Il ne faut pas mettre les crochets autour du nom : le bot le fait automatiquement. Habituellement, c'est la seule commande nécessaire pour organiser un challenge. Cependant, des commandes de debug sont disponibles :

#### Définir une durée

```
!challenge duration 2
```

Change la durée en semaines du challenge actuel et des prochains. Il n'est donc pas nécessaire d'utiliser la commande à chaque challenge.

#### Ajouter une participation

```
!challenge add 698379911806845008
```

Ajoute un message aux participations manuellement d'après son ID. Utile si le bot a manqué un message parce qu'il était éteint par exemple. Le message doit tout de même avoir un format valide pour que la commande fonctionne.

#### Terminer le challenge

```
!challenge end
!c e
```

Met fin à la période de soumission prématurément et lance les votes.

```
!challenge end_votes
!c ev
```

Met fin à la période de votes prématurément et affiche les résultats.
