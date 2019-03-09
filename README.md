# Bot Discord pour Game Dev Alliance

Le bot Game Dev Alliance permet d'afficher des textes et des liens fréquemment utilisés sur notre [serveur Discord](https://discord.gg/RrBppaj). Toutes les commandes sont utilisables sur le serveur ou en message privé avec le bot. Il existe trois catégories :

```
video
wiki
texte
```

Ecrivez `!help <commande>` pour recevoir un MP avec des informations sur n'importe quelle commande ou catégorie.

## Vidéos

```
!video <nom>
```

La catégorie `!video` affiche une vidéo de la [chaîne Game Dev Alliance](https://www.youtube.com/c/AurelienVideos). On peut aussi écrire plus simplement `!v`. Voici toutes les commandes disponibles :

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

## Wiki

```
!wiki
```

Cette commande, que l'on peut aussi écrire `!w`, affiche un lien vers l'Encyclopédie du making (https://wiki.rpgmakeralliance.com/). Il est possible d'afficher un lien vers un article précis du wiki :

```
!wiki rpgmaker       => https://wiki.rpgmakeralliance.com/rpgmaker
!wiki rpgmaker/faq   => https://wiki.rpgmakeralliance.com/rpgmaker/faq
!wiki gamemaker      => https://wiki.rpgmakeralliance.com/gamemaker
```

## Textes personnalisés

Il est possible de stocker ses propres textes, et de les nommer afin de les afficher rapidement plus tard. Toutes les commandes commencent par `!texte`, que l'on peut aussi écrire `!t` ou `!tag`.

### Afficher un texte

```
!texte <nom>
```

N'oubliez pas qu'il existe d'autres écritures plus rapides de `!texte`. Ainsi, ces trois lignes affichent le même résultat :

```
!texte jam3
!tag jam3
!t jam3
```

Si le nom que vous écrivez n'existe pas, le bot vous recommandera un nom similaire parmi ceux enregistrés.


### Liste des textes

```
!t list
```

Affiche le nom de tous les textes actuellement enregistrés.

![](https://i.imgur.com/9RBSt11.png)

### Gestion des textes

*Les commandes suivantes sont réservées aux modérateurs.*

#### Ajouter un texte

```
!t add <nom> <contenu>
```

Le nom doit être en un seul mot ou bien entre guillemets, tandis que le contenu est libre. Exemple :

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
