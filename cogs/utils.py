import inspect

from discord.ext import commands
from .utilities import checks

class Utils:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, hidden=True, aliases=['eval'])
    @checks.is_princesseuh()
    async def debug(self, ctx, *, code: str):
        code = code.strip('` ')
        codeblock = '```py\n{}\n```'
        result = None

        env = {
            'bot': self.bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message
        }

        env.update(globals())

        try:
            result = eval(code, env)
            if inspect.isawaitable(result):
                result = await result
        except Exception as e:
            await ctx.send(codeblock.format(type(e).__name__ + ': ' + str(e)))
            return

        await ctx.send(codeblock.format(result))


def setup(bot):
    bot.add_cog(Utils(bot))
