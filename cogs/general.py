import difflib
import aiohttp
import discord

from discord.ext import commands
from .utilities import checks

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    async def on_message(self, message):
        if (message.author.bot or
            isinstance(message.channel, discord.DMChannel) or
            message.channel.category.name == "English"):
            return

        hasHeavyGif = False
        if message.attachments:
            for attach in message.attachments:
                if attach.filename.lower().endswith("gif") and attach.size >= 1048576:
                        hasHeavyGif = True
                        break

        if hasHeavyGif:
            await message.channel.send("{}, les connexions lentes et les forfaits mobiles auront du mal à afficher ton gif. Tu peux convertir ton gif en vidéo en le mettant en ligne sur <https://gfycat.com/>. Si besoin, tu peux facilement capturer des vidéos avec <https://getsharex.com/> afin d'obtenir des animations plus fluides et légères. Merci beaucoup !".format(message.author.mention))


    @commands.command(aliases=["w"])
    async def wiki(self, ctx, link: str = ""):
        """
            Affiche un lien vers l'Encyclopédie.
        """
        if link is None:
            await ctx.send("https://wiki.gamedevalliance.fr")
        else:
            link = "https://wiki.gamedevalliance.fr/" + link
            async with aiohttp.ClientSession() as session:
                async with session.get(link) as r:
                    if r.status == 200:
                        await ctx.send(link)
                    else:
                        await ctx.author.send(link + " n'existe pas!")


    @commands.command(aliases=["v"], brief="Affiche une vidéo de la chaine Youtube de RMA.")
    async def video(self, ctx, video: str):
        """
            Affiche une vidéo de RMA. Vidéos disponibles :
            bases, donjon1, donjon2, villes, export, meilleur, mapping, live, rediffusions, starterpack, pont, jardinrme.
        """
        videos = {
            "bases": "https://www.youtube.com/watch?v=HKXL-0i7uAM",
            "donjon1": "https://www.youtube.com/watch?v=yTmpdDe77C8",
            "donjon2": "https://www.youtube.com/watch?v=zwNfO6HHfRo",
            "villes": "https://www.youtube.com/watch?v=MgbMOXXk2KE",
            "export": "https://www.youtube.com/watch?v=LFyPmIrvHFM",
            "meilleur": "https://www.youtube.com/watch?v=8RS2_VDglYM",
            "mapping": "https://www.youtube.com/watch?v=Y_QFv_WgxGo",
            "live": "https://www.youtube.com/c/AurelienVideos/live",
            "rediffusions": "https://www.youtube.com/playlist?list=PLHKUrXMrDS5veYcSPO0bLSHblMsDlxVJC",
            "starterpack": "https://www.youtube.com/watch?v=-fg5hy7VAwE",
            "pont": "https://www.youtube.com/watch?v=jLjftJnE6dM",
            "jardinrme": "https://www.youtube.com/watch?v=nHwSuBDEDhI"
        }

        if video in videos.keys():
            await ctx.send(videos[video])
        else:
            match = difflib.get_close_matches(video, videos.keys())
            matches = " Recommandation : {}".format(", ".join("`{}`".format(result) for result in match))

            await ctx.author.send("{}, aucune vidéo trouvée pour {}.{}".format(ctx.author.mention, video, matches if match else ""))


    @commands.command(aliases=["s"])
    @checks.has_roles_or_staff()
    async def say(self, ctx, *, content: str):
        ctx.send(content)


def setup(bot):
    bot.add_cog(General(bot))
