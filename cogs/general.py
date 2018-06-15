import difflib

from discord.ext import commands

class General:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wiki(self, ctx):
        """
            Envoi un lien vers le wiki
        """
        await ctx.send("https://wiki.rpgmakeralliance.com")


    @commands.command(aliases=["questions"])
    async def faq(self, ctx):
        """
            Envoi un lien vers le wiki
        """
        await ctx.send("https://wiki.rpgmakeralliance.com/faq")


    @commands.command(aliases=["v"])
    async def video(self, ctx, video: str):
        videos = {
            "bases":"https://www.youtube.com/watch?v=HKXL-0i7uAM",
            "donjon1": "https://www.youtube.com/watch?v=yTmpdDe77C8",
            "donjon2":"https://www.youtube.com/watch?v=zwNfO6HHfRo",
            "villes":"https://www.youtube.com/watch?v=MgbMOXXk2KE",
            "export":"https://www.youtube.com/watch?v=LFyPmIrvHFM",
            "meilleur":"https://www.youtube.com/watch?v=8RS2_VDglYM"
        }

        if video in videos.keys():
            await ctx.send(videos[video])
        else:
            match = difflib.get_close_matches(video, videos.keys())
            matches = " Recommandation : {}".format(", ".join("`{}`".format(result) for result in match))

            await ctx.author.send("{}, aucune vidéo trouvée pour {}.{}".format(ctx.author.mention, video, matches if match else ""))


def setup(bot):
    bot.add_cog(General(bot))
