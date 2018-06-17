from discord.ext import commands


def is_princesseuh():
    return commands.check(lambda ctx: ctx.author.id == 98157796939272192)


def has_roles_or_staff():
    return commands.check(lambda ctx: ctx.author.id in [98157796939272192, 102381101179219968] or commands.has_role("Le staff"))
