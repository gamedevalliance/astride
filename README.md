# Bot Discord pour RPG Maker Alliance

Le bot RPG Maker Alliance permet d'afficher des textes et des liens fréquemment utilisés sur le [serveur Discord](https://discord.gg/RrBppaj). Il existe quatre catégories :

```
video
wiki
faq
texte
```

Ecrivez `!help <commande>` pour avoir plus d'informations sur n'importe quelle commande ou catégorie.

## Vidéos

La catégorie `!video` affiche une vidéo de la [chaîne RPG Maker Alliance](https://www.youtube.com/c/AurelienVideos). On peut aussi écrire plus simplement `!v`. Voici toutes les commandes disponibles :

```
!video bases
!video donjon1
!video donjon2
!video villes
!video export
!video meilleur
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
!texte add <nom> <texte>
```

Le nom doit être en un mot, tandis que le texte stocké est libre. Exemple :

```
!texte add SiteOfficiel Le site officiel de RPG Maker est http://www.rpgmakerweb.com/
```

### Modifier un texte

Cette commande remplace un texte déjà existant :

```
!texte edit <nom> <texte>
```

### Afficher un texte

Afficher un texte déjà enregistré est très simple :

```
!texte <nom>
```

N'oubliez pas qu'il existe des écritures alternatives de `!texte` pour écrire plus vite. Ainsi, ces trois lignes affichent le même résultat :

```
!texte SiteOfficiel
!t SiteOfficiel
!tag SiteOfficiel
```

Si le nom que vous écrivez n'existe pas, le bot vous recommandera un nom similaire parmi ceux enregistrés.

### Supprimer un texte

Il suffit de connaître son nom pour supprimer un texte enregistré :

```
!texte remove <nom>
```

### Liste des textes

Cette commande affiche le nom de tous les textes actuellement enregistrés :

```
!texte list
```
