from bot import Bot, logging_conf, FormatHelp
import discord
import logging
import logging.config

default_extensions = ["cogs.general", "cogs.texte", "cogs.utils"]

logging.config.dictConfig(logging_conf)
log = logging.getLogger()

help_attrs = dict(hidden=True, aliases=['aide', 'commandes'])
bot = Bot(command_prefix='!', default_extensions=default_extensions, pm_help=True, help_attrs=help_attrs,
          formatter=FormatHelp(),
          command_not_found="Aucune commande nommée `{}`",
          command_has_no_subcommands="Aucune sous-commandes pour {0.name}")


@bot.event
async def on_ready():
    log.info("--> Successfully connected!")
    log.info("------------------------------------------")


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    await bot.process_commands(message)


@bot.event
async def on_command(ctx):
    log.info(u"{0.content} sent by {0.author.name}".format(ctx.message))

    if not isinstance(ctx.channel, discord.abc.PrivateChannel):
        await ctx.message.delete()


@bot.event
async def on_command_error(ctx, err):
    log.error(u"{0.content} sent by {0.author.name}. Error : {1}".format(ctx.message, err))


def get_account():
    with open('account') as f:
        return f.read()


if __name__ == '__main__':
    log.info("--> Connecting..")

    account = get_account()
    bot.run(account)

    log.info("--> That's all, folks!")
