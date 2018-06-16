# Bot Discord pour RPG Maker Alliance

Le bot RPG Maker Alliance permet d'afficher des textes et des liens fréquemment utilisés sur notre [serveur Discord](https://discord.gg/RrBppaj). Toutes les commandes sont utilisables sur le serveur ou en message privé avec le bot. Il existe quatre catégories :

```
video
wiki
faq
texte
```

Ecrivez `!help <commande>` pour recevoir un MP avec des informations sur n'importe quelle commande ou catégorie.

## Vidéos

La catégorie `!video` affiche une vidéo de la [chaîne RPG Maker Alliance](https://www.youtube.com/c/AurelienVideos). On peut aussi écrire plus simplement `!v`. Voici toutes les commandes disponibles :

```
!video bases
!video donjon1
!video donjon2
!video villes
!video export
!video meilleur
!video mapping
!video live
!video rediffusions
```

En cas d'erreur de frappe, le bot recommandera une vidéo similaire parmi celles qui existent.

## Wiki

```
!wiki
```

Cette commande affiche un lien vers l'[Encyclopédie du making](https://wiki.rpgmakeralliance.com/).

## Questions fréquentes

```
!faq
```

Cette commande affiche un lien vers la [page des questions fréquentes](https://wiki.rpgmakeralliance.com/faq) sur l'Encyclopédie.

## Textes personnalisés

Il est possible de stocker ses propres textes, et de les nommer afin de les afficher rapidement plus tard. Toutes les commandes commencent par `!texte`, que l'on peut aussi écrire `!t` ou `!tag`.

### Ajouter un texte

```
!texte add <nom> <contenu>
```

Le nom doit être en un mot, tandis que le contenu est libre. Exemple :

```
!texte add SiteOfficiel Le site officiel de RPG Maker est http://www.rpgmakerweb.com/
```

### Modifier un texte

```
!texte edit <nom> <contenu>
```

Remplace le contenu d'un texte existant.

### Afficher un texte

```
!texte <nom>
```

N'oubliez pas qu'il existe d'autres écritures plus rapides de `!texte`. Ainsi, ces trois lignes affichent le même résultat :

```
!texte SiteOfficiel
!t SiteOfficiel
!tag SiteOfficiel
```

Si le nom que vous écrivez n'existe pas, le bot vous recommandera un nom similaire parmi ceux enregistrés.

### Supprimer un texte

```
!texte remove <nom>
```

### Liste des textes

```
!texte list
```

Affiche le nom de tous les textes actuellement enregistrés.
