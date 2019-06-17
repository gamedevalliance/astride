from discord.ext import commands
import logging

log = logging.getLogger()


class Bot(commands.Bot):
    def __init__(self, default_extensions, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for ext in default_extensions:
            try:
                self.load_extension(ext)
                log.info("extension {} successfully loaded".format(ext))
            except Exception as e:
                log.error(
                    'Failed to load extension {}. {}: {}'
                    .format(ext, type(e).__name__, e))


# class FormatHelp():
#    def get_ending_note(self):
#        command_name = self.context.invoked_with
#        return "Tapez {0}{1} <commande> pour plus d'informations sur une commande spécifique.".format(self.clean_prefix, command_name)


# This is ugly.
logging_conf = {
    "version": 1,
    "formatters": {
        "long": {
            "format": u"[%(asctime)s] %(levelname)s %(message)s",
            "datefmt": u"%m/%d %H:%M:%S"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "long",
            "stream": "ext://sys.stdout"
        },
        "logfile": {
            "class": "logging.FileHandler",
            "formatter": "long",
            "filename": "client.log",
            "encoding": "utf-8"
        }
    },
    "root": {
        "handlers": ["console", "logfile"],
        "level": "INFO"
    },
    "loggers": {
        "discord": {
            "level": "CRITICAL"
        }
    },
    "disable_existing_loggers": False
}
