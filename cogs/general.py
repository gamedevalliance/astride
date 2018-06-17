import difflib
import aiohttp

from discord.ext import commands

class General:
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=["w"])
    async def wiki(self, ctx, link: str = ""):
        """
            Affiche un lien vers l'Encyclopédie.
        """
        if link is None:
            await ctx.send("https://wiki.rpgmakeralliance.com")
        else:
            link = "https://wiki.rpgmakeralliance.com/" + link
            async with aiohttp.ClientSession() as session:
                async with session.get(link) as r:
                    if r.status == 200:
                        await ctx.send(link)
                    else:
                        await ctx.author.send(link + " n'existe pas!")


    @commands.command(aliases=["v"])
    async def video(self, ctx, video: str):
        """
            Affiche une vidéo de RMA. Vidéos disponibles : bases, donjon1, donjon2, villes, export, meilleur, mapping, live, rediffusions.
        """
        videos = {
            "bases":"https://www.youtube.com/watch?v=HKXL-0i7uAM",
            "donjon1": "https://www.youtube.com/watch?v=yTmpdDe77C8",
            "donjon2":"https://www.youtube.com/watch?v=zwNfO6HHfRo",
            "villes":"https://www.youtube.com/watch?v=MgbMOXXk2KE",
            "export":"https://www.youtube.com/watch?v=LFyPmIrvHFM",
            "meilleur":"https://www.youtube.com/watch?v=8RS2_VDglYM",
            "mapping":"https://www.youtube.com/watch?v=Y_QFv_WgxGo",
            "live":"https://www.youtube.com/c/AurelienVideos/live",
            "rediffusions":"https://www.youtube.com/playlist?list=PLHKUrXMrDS5veYcSPO0bLSHblMsDlxVJC"
        }

        if video in videos.keys():
            await ctx.send(videos[video])
        else:
            match = difflib.get_close_matches(video, videos.keys())
            matches = " Recommandation : {}".format(", ".join("`{}`".format(result) for result in match))

            await ctx.author.send("{}, aucune vidéo trouvée pour {}.{}".format(ctx.author.mention, video, matches if match else ""))


def setup(bot):
    bot.add_cog(General(bot))
