import difflib

from discord.ext import commands
from .utilities import config, checks

class Textes:
    def __init__(self, bot):
        self.bot = bot
        self.texts = config.JSONAsset(
            'texts.json',
            loop=bot.loop,
            defer_load=True)

    @commands.group(invoke_without_command=True, aliases=["t", "tag"])
    async def texte(self, ctx, *, texte: str):
        """
            Il est possible de stocker ses propres textes afin de les afficher rapidement plus tard. Utilisez add pour stocker un texte et lui donner un nom, puis affichez-le en tapant simplement son nom.
        """
        if texte is None:
            return

        if texte in self.texts:
            await ctx.send(self.texts[texte]['content'])
        else:
            match = difflib.get_close_matches(texte, tuple(self.texts.content()))
            matches = " Recommandation : {}".format(", ".join("`{}`".format(result) for result in match))

            await ctx.author.send("{}, aucun texte trouvé pour {}.{}".format(ctx.author.mention, texte, matches if match else ""))


    @texte.command()
    @checks.has_roles_or_staff()
    async def add(self, ctx, nom: str, *, contenu: str):
        """
            Stocke un nouveau texte. Le nom doit être en un seul mot, tandis que le contenu est libre.
        """
        if not contenu:
            return await ctx.author.send("{}, un texte ne peut pas être vide.".format(ctx.author.mention))

        if nom in self.texts:
            return await ctx.author.send("{}, un texte avec ce nom existe déjà !".format(ctx.author.mention))

        await self.texts.put(
            nom,
            {
                'author': ctx.author.id,
                'content': contenu
            }
        )

        await ctx.author.send("{}, texte {} créé et sauvegardé !".format(ctx.author.mention, nom))

    @texte.command()
    @checks.has_roles_or_staff()
    async def edit(self, ctx, nom: str, *, contenu: str):
        """
            Remplace le contenu d'un texte existant.
        """
        if nom not in self.texts:
            match = difflib.get_close_matches(nom, tuple(self.texts.content()))
            matches = " Recommandation : {}".format(", ".join("`{}`".format(result) for result in match))

            return await ctx.author.send("{}, aucun texte trouvé pour {}.{}".format(ctx.author.mention, nom, matches if match else ""))

        self.texts[nom]['content'] = contenu
        await self.texts.save()

        await ctx.author.send("{}, texte {} édité et sauvegardé !".format(ctx.author.mention, nom))

    @texte.command()
    @checks.has_roles_or_staff()
    async def remove(self, ctx, *, nom: str):
        """
            Supprime un texte désigné par son nom.
        """
        if nom not in self.texts:
            match = difflib.get_close_matches(nom, tuple(self.texts.content()))
            matches = " Recommandation : {}".format(", ".join("`{}`".format(result) for result in match))

            return await ctx.author.send("{}, aucun texte trouvé pour {}.{}".format(ctx.author.mention, nom, matches if match else ""))

        await self.texts.remove(nom)
        await ctx.author.send("{}, texte {} supprimé !".format(ctx.author.mention, nom))

    @texte.command()
    async def list(self, ctx):
        """
            Affiche le nom de tous les textes actuellement enregistrés.
        """
        textes = [texte for texte in self.texts.content()]

        if textes:
            count = len(textes)
            textes = ", ".join("`{}`".format(texte) for texte in textes)
            await ctx.author.send("**Liste des textes pour RMA ({}):**\n{}".format(count, textes))

def setup(bot):
    bot.add_cog(Textes(bot))
